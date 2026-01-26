# 🧠 Distributed AI Agents with KubeRay (GKE)

https://cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview#raycluster

## 🌍 Overview

This project transforms **Ray Actors** into **cognitive agents** — autonomous, stateful entities capable of reasoning, memory, and communication across distributed systems.

Traditional distributed training parallelizes data and model computation.  
**This framework parallelizes cognition.**

By leveraging **Ray’s distributed actor model**, each agent maintains its own memory, policy, and communication channel while participating in a shared environment orchestrated by a meta-agent.

---

## 🧩 Core Concepts

| Concept | Description |
|----------|--------------|
| **Agent (Ray Actor)** | A persistent, stateful unit of computation with local memory and policy logic. |
| **Memory** | Each agent stores contextual embeddings, decisions, and local experiences. |
| **Policy / Cognition** | The decision-making logic or LLM-based reasoning function driving agent actions. |
| **Meta-Agent** | A global coordinator that schedules, monitors, and evaluates agents’ performance and collective reasoning. |
| **Environment** | Shared message-passing fabric and state space where agents interact. |

---

## ⚙️ Architecture

```┌───────────────────────────────────────────┐
│          Distributed AI System            │
│───────────────────────────────────────────│
│ Meta-Agent (Orchestrator / Scheduler)     │
│   ├─ Policy Coordination                  │
│   ├─ Resource Control (Ray)               │
│   └─ Collective Reasoning / Reflection    │
│                                           │
│ Agents (Ray Actors):                      │
│   ├─ Reasoner Agent                       │
│   ├─ Retriever Agent                      │
│   ├─ Evaluator Agent                      │
│   └─ Memory Agent                         │
│                                           │
│ Infrastructure Layer (Ray Runtime):       │
│   ├─ Task Scheduling                      │
│   ├─ Actor Communication                  │
│   └─ Distributed State Management         │
└───────────────────────────────────────────┘```
