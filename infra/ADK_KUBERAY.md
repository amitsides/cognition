# Infrastructure of ADK, A2A, GKE, KubeRay

This document outlines the architectural blueprint and core implementation pattern for deploying a distributed, multi-agent AI system on a scalable cloud-native infrastructure using Google's Agent Stack and Ray on Kubernetes.

## 1. Project Overview and Key Technologies

This project utilizes a Sequential Agent model to orchestrate a workflow where specialized sub-agents are deployed as remote microservices. This provides robust scaling and decoupling of business logic.

| Acronym | Full Name | Role in the Project |
|---------|-----------|---------------------|
| **ADK** | Agent Development Kit | The core framework for developing, orchestrating, and testing the agent's internal logic and workflow (e.g., SequentialAgent). |
| **A2A** | Agent-to-Agent Protocol | The open standard communication protocol that enables the main agent to securely call the remote sub-agents as distinct, decoupled services over the network. |
| **GKE** | Google Kubernetes Engine | The managed Kubernetes service on Google Cloud, providing the robust and scalable container orchestration environment for all agent services. |
| **KubeRay** | Ray Operator on GKE | A Kubernetes operator that manages the lifecycle of Ray clusters, enabling agents to be deployed and scaled efficiently using the Ray Serve component. |

## 2. Distributed Agent Architecture

The system consists of one **Coordinator Agent** (the ADK SequentialAgent) and multiple **Specialist Agents** (remote services).

### 2.1. The Coordinator: ADK SequentialAgent

The `PipelineOrchestratorAgent` is a local ADK agent that defines the sequence of tasks. Instead of embedding the logic of its sub-agents locally, it uses `RemoteA2aAgent` components.

### 2.2. The Specialists: RemoteA2aAgent on Ray Serve

Each specialist agent (`DataCollector`, `ModelExecutor`, `ResultFormatter`) is developed using the ADK and exposed as an A2A Server. For deployment, they are packaged into containers and served via Ray Serve within a KubeRay-managed cluster on GKE.

This decouples their lifecycle, allowing independent scaling, language flexibility, and versioning.

## 3. Conceptual Python Implementation (ADK & A2A)

The following Python code illustrates the architectural pattern used for orchestration.

### main_orchestrator.py

This script defines the orchestrating agent and connects to the remote sub-agents via their A2A endpoint URLs.

```python
from google.adk.agents import SequentialAgent, RemoteA2aAgent
from google.adk.core import Agent

# --- 1. Define Remote A2A Sub-Agents ---
# These agents are deployed separately on the KubeRay-managed GKE cluster.
# The URL points to the exposed Ray Serve service for each agent's A2A endpoint.

DATA_COLLECTOR_URL = "http://data-collector-service.agent-namespace/a2a/DataCollector"
MODEL_EXECUTOR_URL = "http://model-executor-service.agent-namespace/a2a/ModelExecutor"
RESULT_FORMATTER_URL = "http://result-formatter-service.agent-namespace/a2a/ResultFormatter"

data_collector_agent = RemoteA2aAgent(
    name="DataCollector",
    description="Fetches and preprocesses input data.",
    url=DATA_COLLECTOR_URL,
    input_schema=..., # Define expected input schema
    output_key="raw_data",
)

model_executor_agent = RemoteA2aAgent(
    name="ModelExecutor",
    description="Executes the core ML model on the processed data.",
    url=MODEL_EXECUTOR_URL,
    input_key="raw_data", # Consumes output from the previous agent
    output_key="model_output",
)

result_formatter_agent = RemoteA2aAgent(
    name="ResultFormatter",
    description="Formats the model output into a human-readable report.",
    url=RESULT_FORMATTER_URL,
    input_key="model_output", # Consumes output from the previous agent
    output_key="final_report",
)

# --- 2. Define the Orchestrator (Sequential Agent) ---
class PipelineOrchestratorAgent(SequentialAgent):
    """
    The main agent that executes the workflow by calling remote A2A services
    in a fixed, sequential order.
    """
    def __init__(self):
        super().__init__(
            name="PipelineOrchestratorAgent",
            description="Manages the end-to-end distributed agent pipeline.",
            sub_agents=[
                data_collector_agent,
                model_executor_agent,
                result_formatter_agent,
            ],
            # The final result of the pipeline is stored in 'final_report'
            default_output_key="final_report",
        )

# --- 3. Example Execution (Local Testing) ---
# NOTE: In production, this agent is also deployed as an A2A server 
# and invoked via a client, but this shows the local orchestration.
if __name__ == '__main__':
    orchestrator = PipelineOrchestratorAgent()
    
    # The initial input to the first agent
    initial_input = {"user_query": "Analyze Q3 market trends for tech stock."}

    print("Starting distributed agent pipeline...")
    # The ADK Runner handles the Sequential execution and state sharing 
    # (via input_key/output_key) between the remote A2A calls.
    result = orchestrator.run(initial_input) 
    
    print("\n--- Pipeline Complete ---")
    print(f"Final Output: {result.output['final_report']}")
```

## 4. GKE and KubeRay Deployment Model

The scalability and resilience of the system are ensured by deploying the A2A services using KubeRay on GKE.

### 4.1. Packaging and Service

- **Containerization**: Each Specialist Agent is bundled into a separate Docker container with the ADK and its dependencies, exposing an A2A-compliant endpoint (e.g., on port 8000).

- **Ray Serve Configuration**: Each container runs as a Ray Serve Deployment, which provides high-performance model serving, dynamic routing, and load balancing across multiple worker replicas.

### 4.2. KubeRay Custom Resource

The deployment to GKE is managed declaratively using a `RayService` Custom Resource Definition (CRD) provided by KubeRay.

```yaml
# Simplified RayService CRD for a single agent (e.g., DataCollector)
apiVersion: ray.io/v1alpha1
kind: RayService
metadata:
  name: data-collector-agent
spec:
  # ... RayCluster Configuration (Head and Worker Nodes) ...
  serveConfigV2: |
    applications:
      - name: data-collector-a2a
        route_prefix: "/a2a/DataCollector"  # A2A Endpoint exposed here
        import_path: "data_collector_app.serve_entrypoint:A2A_Deployment"
        deployments:
          - name: DataCollectorAgentDeployment
            num_replicas: 2 # Scale-out capability via Ray Serve
            user_config:
              agent_name: DataCollector
              # ... other deployment settings ...
  # ... other RayService configurations ...
```

### 4.3. Advantages of the Infrastructure

| Feature | GKE + KubeRay Benefit | ADK + A2A Benefit |
|---------|----------------------|-------------------|
| **Scalability** | Ray Serve provides autoscaling and efficient resource utilization (CPU/GPU) for individual agent deployments, managed by KubeRay. | Allows for the easy addition of new, independent specialist agents without modifying the orchestrator's core logic. |
| **Decoupling** | Each specialist agent is a separate microservice, ensuring failure in one agent doesn't bring down the entire system. | A2A Protocol defines a strict, standardized contract for communication, regardless of the underlying runtime framework. |
| **Orchestration** | Kubernetes ensures the service endpoints are reliably addressable via GKE Service objects. | ADK SequentialAgent provides a high-level, human-readable abstraction for the end-to-end distributed workflow. |

## Summary

This infrastructure pattern combines:

- **ADK** for high-level agent development and orchestration
- **A2A Protocol** for standardized, language-agnostic inter-agent communication
- **Ray Serve** for high-performance, scalable agent serving
- **KubeRay** for declarative Ray cluster management on Kubernetes
- **GKE** for robust, managed container orchestration

The result is a production-ready, cloud-native multi-agent system that scales independently per agent, maintains fault isolation, and provides a clean separation between orchestration logic and specialist execution.