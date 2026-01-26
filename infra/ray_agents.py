#!/usr/bin/env python3
"""
Ray Agent Deployment Script for GKE-KubeRay

This script reads a multi-agent system JSON specification and deploys
each agent as a Ray Actor/Serve deployment on a KubeRay-managed cluster.

Usage:
    python deploy_agents.py --config agents.json --namespace agent-system
"""

import json
import argparse
import yaml
from typing import List, Dict, Any
from pathlib import Path
import subprocess
import tempfile


class RayAgentDeployer:
    """Deploys agents from JSON specification to GKE KubeRay cluster."""
    
    def __init__(self, config_path: str, namespace: str = "default", 
                 ray_version: str = "2.9.0"):
        self.config_path = Path(config_path)
        self.namespace = namespace
        self.ray_version = ray_version
        self.agents = []
        
    def load_agents(self) -> List[Dict[str, Any]]:
        """Load agent specifications from JSON file."""
        with open(self.config_path, 'r') as f:
            self.agents = json.load(f)
        print(f"✓ Loaded {len(self.agents)} agents from {self.config_path}")
        return self.agents
    
    def generate_agent_serve_code(self, agent: Dict[str, Any]) -> str:
        """Generate Ray Serve deployment code for an agent."""
        name = agent['name']
        prompt = agent['prompt']
        description = agent['description']
        
        serve_code = f'''
import ray
from ray import serve
from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class AgentRequest(BaseModel):
    """A2A compatible request format."""
    input: dict
    context: dict = {{}}
    metadata: dict = {{}}

class AgentResponse(BaseModel):
    """A2A compatible response format."""
    output: dict
    context: dict = {{}}
    metadata: dict = {{}}

@serve.deployment(
    name="{name}",
    route_prefix="/a2a/{name}",
    num_replicas=2,
    ray_actor_options={{"num_cpus": 1, "num_gpus": 0}}
)
@serve.ingress(app)
class {name}Agent:
    """
    {description}
    """
    
    def __init__(self):
        self.name = "{name}"
        self.prompt = """{prompt}"""
        self.description = """{description}"""
        logger.info(f"Initialized {{self.name}} agent")
    
    @app.post("/")
    async def handle_request(self, request: AgentRequest) -> AgentResponse:
        """
        Main A2A endpoint handler.
        
        This is a template implementation. Replace with actual agent logic
        that uses the prompt to process inputs.
        """
        logger.info(f"{{self.name}} received request: {{request.input}}")
        
        try:
            # TODO: Implement actual agent logic here
            # This could call LLM APIs, run inference, execute tools, etc.
            result = self._process(request.input, request.context)
            
            response = AgentResponse(
                output=result,
                context=request.context,
                metadata={{
                    "agent_name": self.name,
                    "status": "success"
                }}
            )
            
            logger.info(f"{{self.name}} completed processing")
            return response
            
        except Exception as e:
            logger.error(f"{{self.name}} error: {{str(e)}}")
            return AgentResponse(
                output={{"error": str(e)}},
                context=request.context,
                metadata={{
                    "agent_name": self.name,
                    "status": "error"
                }}
            )
    
    def _process(self, input_data: dict, context: dict) -> dict:
        """
        Core processing logic guided by the agent's prompt.
        
        Args:
            input_data: Input data to process
            context: Contextual information from previous agents
            
        Returns:
            Processed output as dictionary
        """
        # Placeholder implementation
        # In production, this would use the prompt to guide LLM calls,
        # execute specialized logic, etc.
        
        return {{
            "processed_by": self.name,
            "input_received": input_data,
            "prompt_guidance": self.prompt[:100] + "...",
            "result": "Agent processing complete"
        }}
    
    @app.get("/health")
    async def health(self):
        """Health check endpoint."""
        return {{"status": "healthy", "agent": self.name}}

# Deployment entrypoint
agent_deployment = {name}Agent.bind()
'''
        return serve_code
    
    def generate_dockerfile(self, agent_name: str) -> str:
        """Generate Dockerfile for agent container."""
        dockerfile = f'''FROM rayproject/ray:{self.ray_version}-py310

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir \\
    fastapi \\
    pydantic \\
    uvicorn \\
    aiohttp \\
    requests

# Copy agent code
COPY {agent_name}_serve.py /app/

# Expose Ray Serve port
EXPOSE 8000

# Set Ray Serve configuration
ENV RAY_SERVE_ENABLE_EXPERIMENTAL_STREAMING=1

# Start Ray and deploy the agent
CMD ["serve", "run", "{agent_name}_serve:agent_deployment", "--host", "0.0.0.0", "--port", "8000"]
'''
        return dockerfile
    
    def generate_rayservice_yaml(self, agent: Dict[str, Any]) -> Dict[str, Any]:
        """Generate KubeRay RayService CRD for an agent."""
        name = agent['name'].lower().replace('_', '-')
        
        rayservice = {
            'apiVersion': 'ray.io/v1',
            'kind': 'RayService',
            'metadata': {
                'name': f'{name}-service',
                'namespace': self.namespace,
                'labels': {
                    'app': 'ray-agent',
                    'agent': name
                }
            },
            'spec': {
                'serviceUnhealthySecondThreshold': 300,
                'deploymentUnhealthySecondThreshold': 300,
                'serveConfigV2': self._generate_serve_config(agent),
                'rayClusterConfig': {
                    'rayVersion': self.ray_version,
                    'enableInTreeAutoscaling': True,
                    'headGroupSpec': {
                        'rayStartParams': {
                            'dashboard-host': '0.0.0.0',
                            'num-cpus': '0'
                        },
                        'template': {
                            'spec': {
                                'containers': [{
                                    'name': 'ray-head',
                                    'image': f'gcr.io/PROJECT_ID/{name}-agent:latest',
                                    'imagePullPolicy': 'Always',
                                    'ports': [
                                        {'containerPort': 6379, 'name': 'gcs'},
                                        {'containerPort': 8265, 'name': 'dashboard'},
                                        {'containerPort': 10001, 'name': 'client'},
                                        {'containerPort': 8000, 'name': 'serve'}
                                    ],
                                    'resources': {
                                        'limits': {'cpu': '2', 'memory': '4Gi'},
                                        'requests': {'cpu': '1', 'memory': '2Gi'}
                                    }
                                }]
                            }
                        }
                    },
                    'workerGroupSpecs': [{
                        'replicas': 2,
                        'minReplicas': 1,
                        'maxReplicas': 5,
                        'groupName': 'worker-group',
                        'rayStartParams': {},
                        'template': {
                            'spec': {
                                'containers': [{
                                    'name': 'ray-worker',
                                    'image': f'gcr.io/PROJECT_ID/{name}-agent:latest',
                                    'imagePullPolicy': 'Always',
                                    'resources': {
                                        'limits': {'cpu': '2', 'memory': '4Gi'},
                                        'requests': {'cpu': '1', 'memory': '2Gi'}
                                    }
                                }]
                            }
                        }
                    }]
                }
            }
        }
        
        return rayservice
    
    def _generate_serve_config(self, agent: Dict[str, Any]) -> str:
        """Generate Ray Serve configuration YAML string."""
        name = agent['name']
        
        serve_config = f'''
applications:
  - name: {name.lower()}-app
    route_prefix: /a2a/{name}
    import_path: {name}_serve:agent_deployment
    runtime_env:
      working_dir: "."
    deployments:
      - name: {name}
        num_replicas: 2
        max_concurrent_queries: 100
        ray_actor_options:
          num_cpus: 1
          num_gpus: 0
'''
        return serve_config.strip()
    
    def generate_k8s_service(self, agent: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Kubernetes Service for agent endpoint."""
        name = agent['name'].lower().replace('_', '-')
        
        service = {
            'apiVersion': 'v1',
            'kind': 'Service',
            'metadata': {
                'name': f'{name}-service',
                'namespace': self.namespace,
                'labels': {
                    'app': 'ray-agent',
                    'agent': name
                }
            },
            'spec': {
                'type': 'ClusterIP',
                'selector': {
                    'ray.io/node-type': 'head',
                    'ray.io/cluster': f'{name}-service'
                },
                'ports': [{
                    'name': 'serve',
                    'port': 8000,
                    'targetPort': 8000,
                    'protocol': 'TCP'
                }]
            }
        }
        
        return service
    
    def write_deployment_files(self, output_dir: str = "./deployment"):
        """Generate all deployment files for agents."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        print(f"\n🔧 Generating deployment files in {output_path}/")
        
        for agent in self.agents:
            agent_name = agent['name']
            agent_dir = output_path / agent_name
            agent_dir.mkdir(exist_ok=True)
            
            # Generate Ray Serve code
            serve_code = self.generate_agent_serve_code(agent)
            serve_file = agent_dir / f"{agent_name}_serve.py"
            serve_file.write_text(serve_code)
            print(f"  ✓ {agent_name}_serve.py")
            
            # Generate Dockerfile
            dockerfile = self.generate_dockerfile(agent_name)
            dockerfile_path = agent_dir / "Dockerfile"
            dockerfile_path.write_text(dockerfile)
            print(f"  ✓ Dockerfile")
            
            # Generate RayService YAML
            rayservice = self.generate_rayservice_yaml(agent)
            rayservice_file = agent_dir / f"{agent_name}_rayservice.yaml"
            with open(rayservice_file, 'w') as f:
                yaml.dump(rayservice, f, default_flow_style=False)
            print(f"  ✓ {agent_name}_rayservice.yaml")
            
            # Generate K8s Service YAML
            service = self.generate_k8s_service(agent)
            service_file = agent_dir / f"{agent_name}_service.yaml"
            with open(service_file, 'w') as f:
                yaml.dump(service, f, default_flow_style=False)
            print(f"  ✓ {agent_name}_service.yaml")
            
            # Generate build script
            build_script = self._generate_build_script(agent_name)
            build_file = agent_dir / "build_and_push.sh"
            build_file.write_text(build_script)
            build_file.chmod(0o755)
            print(f"  ✓ build_and_push.sh")
        
        # Generate master deployment script
        deploy_all = self._generate_deploy_all_script()
        deploy_file = output_path / "deploy_all.sh"
        deploy_file.write_text(deploy_all)
        deploy_file.chmod(0o755)
        print(f"  ✓ deploy_all.sh")
        
        print(f"\n✅ All deployment files generated successfully!")
    
    def _generate_build_script(self, agent_name: str) -> str:
        """Generate build and push script for agent container."""
        script = f'''#!/bin/bash
set -e

PROJECT_ID="${{GCP_PROJECT_ID:-your-project-id}}"
REGION="${{GCP_REGION:-us-central1}}"
IMAGE_NAME="{agent_name.lower()}-agent"
TAG="${{IMAGE_TAG:-latest}}"

echo "Building {agent_name} agent container..."
docker build -t $IMAGE_NAME:$TAG .

echo "Tagging for GCR..."
docker tag $IMAGE_NAME:$TAG gcr.io/$PROJECT_ID/$IMAGE_NAME:$TAG

echo "Pushing to GCR..."
docker push gcr.io/$PROJECT_ID/$IMAGE_NAME:$TAG

echo "✓ {agent_name} agent container built and pushed successfully!"
echo "Image: gcr.io/$PROJECT_ID/$IMAGE_NAME:$TAG"
'''
        return script
    
    def _generate_deploy_all_script(self) -> str:
        """Generate master deployment script for all agents."""
        agent_names = [agent['name'] for agent in self.agents]
        
        script = f'''#!/bin/bash
set -e

NAMESPACE="{self.namespace}"

echo "🚀 Deploying all agents to GKE KubeRay cluster..."
echo "Namespace: $NAMESPACE"

# Create namespace if it doesn't exist
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

# Deploy each agent
'''
        
        for agent_name in agent_names:
            script += f'''
echo ""
echo "📦 Deploying {agent_name}..."
cd {agent_name}

# Build and push container
./build_and_push.sh

# Apply Kubernetes resources
kubectl apply -f {agent_name}_rayservice.yaml -n $NAMESPACE
kubectl apply -f {agent_name}_service.yaml -n $NAMESPACE

cd ..
echo "✓ {agent_name} deployed"
'''
        
        script += '''
echo ""
echo "✅ All agents deployed successfully!"
echo ""
echo "Monitor deployments with:"
echo "  kubectl get rayservices -n $NAMESPACE"
echo "  kubectl get pods -n $NAMESPACE"
echo ""
echo "Check agent health:"
'''
        
        for agent_name in agent_names:
            agent_lower = agent_name.lower().replace('_', '-')
            script += f'echo "  curl http://{agent_lower}-service.{self.namespace}:8000/health"\n'
        
        return script
    
    def deploy_to_cluster(self, auto_build: bool = False):
        """Deploy agents to the GKE KubeRay cluster."""
        print(f"\n🚀 Starting deployment to GKE cluster...")
        print(f"   Namespace: {self.namespace}")
        
        # Check if kubectl is available
        try:
            subprocess.run(['kubectl', 'version', '--client'], 
                          check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print("❌ Error: kubectl not found. Please install kubectl.")
            return
        
        # Create namespace
        print(f"\n📁 Creating namespace {self.namespace}...")
        subprocess.run([
            'kubectl', 'create', 'namespace', self.namespace,
            '--dry-run=client', '-o', 'yaml'
        ], capture_output=True)
        subprocess.run([
            'kubectl', 'apply', '-f', '-'
        ], input=subprocess.STDOUT, capture_output=True)
        
        if auto_build:
            print("\n🔨 Building and pushing containers...")
            deploy_script = Path("./deployment/deploy_all.sh")
            if deploy_script.exists():
                subprocess.run(['bash', str(deploy_script)], check=True)
            else:
                print("❌ Error: deploy_all.sh not found. Run write_deployment_files() first.")
        else:
            print("\n⚠️  Skipping container build (auto_build=False)")
            print("   To deploy, run: ./deployment/deploy_all.sh")


def main():
    parser = argparse.ArgumentParser(
        description='Deploy Ray agents to GKE KubeRay cluster from JSON specification'
    )
    parser.add_argument(
        '--config',
        type=str,
        required=True,
        help='Path to agents JSON configuration file'
    )
    parser.add_argument(
        '--namespace',
        type=str,
        default='agent-system',
        help='Kubernetes namespace for agent deployment'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./deployment',
        help='Output directory for generated deployment files'
    )
    parser.add_argument(
        '--ray-version',
        type=str,
        default='2.9.0',
        help='Ray version to use'
    )
    parser.add_argument(
        '--deploy',
        action='store_true',
        help='Automatically deploy to cluster after generating files'
    )
    parser.add_argument(
        '--build',
        action='store_true',
        help='Build and push containers before deploying'
    )
    
    args = parser.parse_args()
    
    # Initialize deployer
    deployer = RayAgentDeployer(
        config_path=args.config,
        namespace=args.namespace,
        ray_version=args.ray_version
    )
    
    # Load agents from JSON
    deployer.load_agents()
    
    # Generate deployment files
    deployer.write_deployment_files(output_dir=args.output_dir)
    
    # Deploy if requested
    if args.deploy:
        deployer.deploy_to_cluster(auto_build=args.build)
    else:
        print("\n💡 To deploy, run:")
        print(f"   cd {args.output_dir} && ./deploy_all.sh")
        print("\n   Or use: python deploy_agents.py --config {args.config} --deploy --build")


if __name__ == '__main__':
    main()