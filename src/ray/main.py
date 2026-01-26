"""
distributed_agents.py

Minimal, complete example of stateful distributed AI agents built on Ray.
Dependencies:
    pip install "ray[default]" numpy

Run:
    python distributed_agents.py
"""

import ray
import numpy as np
import time
import uuid
from typing import List, Dict, Any

# -------------------------
# Utilities / Simple Embedder
# -------------------------
class SimpleEmbedder:
    """
    A tiny deterministic "embedder" used for demonstration.
    Replace with a real model embedder (OpenAI / sentence-transformers / etc.)
    """
    def __init__(self, dim=64, seed=0):
        self.dim = dim
        rng = np.random.RandomState(seed)
        # A deterministic projection matrix
        self.proj = rng.randn(dim, 256)

    def text_to_vector(self, text: str) -> np.ndarray:
        # Create a simple hash-based vector (deterministic)
        h = abs(hash(text)) % (10**9)
        rng = np.random.RandomState(h)
        vec = rng.randn(self.dim).astype(np.float32)
        # normalize
        vec = vec / (np.linalg.norm(vec) + 1e-8)
        return vec

# -------------------------
# Memory Agent (stateful)
# -------------------------
@ray.remote
class MemoryAgent:
    def __init__(self, name: str, embed_dim: int = 64):
        self.name = name
        self.id = str(uuid.uuid4())
        self.store: List[Dict[str, Any]] = []  # list of dicts: {text, vec, ts}
        self.embedder = SimpleEmbedder(dim=embed_dim, seed=hash(self.id) & 0xffff)
        print(f"[MemoryAgent:{self.name}] initialized with id {self.id}")

    def add(self, text: str, metadata: Dict[str, Any] = None):
        vec = self.embedder.text_to_vector(text)
        entry = {"text": text, "vec": vec, "ts": time.time(), "meta": metadata or {}}
        self.store.append(entry)
        return {"status": "ok", "stored": text}

    def query(self, text: str, top_k: int = 3):
        if not self.store:
            return []
        qvec = self.embedder.text_to_vector(text)
        # compute cosine similarity
        sims = []
        for item in self.store:
            sim = float(np.dot(qvec, item["vec"]) / ((np.linalg.norm(item["vec"]) + 1e-8)))
            sims.append(sim)
        idx = np.argsort(sims)[::-1][:top_k]
        results = [{"text": self.store[i]["text"], "score": float(sims[i]), "meta": self.store[i]["meta"]} for i in idx]
        return results

    def dump(self):
        # return raw memory contents (for inspection)
        return [{"text": x["text"], "ts": x["ts"], "meta": x["meta"]} for x in self.store]

# -------------------------
# Reasoner Agent
# -------------------------
@ray.remote
class ReasonerAgent:
    def __init__(self, name: str, memory_agent: ray.actor.ActorHandle):
        self.name = name
        self.memory_agent = memory_agent
        print(f"[ReasonerAgent:{self.name}] created and linked to memory agent {memory_agent}")

    def perceive_and_act(self, observation: str):
        """
        Perceive: store observation in memory
        Act: retrieve related memories and "reason" to produce an action (text)
        """
        # Store observation
        ray.get(self.memory_agent.add.remote(observation, {"source": self.name}))
        # Query memory for related context
        related = ray.get(self.memory_agent.query.remote(observation, top_k=3))
        # Very simple "reasoning": summarize by concatenation / scoring
        introspection = f"Reasoner({self.name}) got observation: '{observation}'"
        if related:
            introspection += " | related memories:\n"
            for r in related:
                introspection += f"  - ({r['score']:.3f}) {r['text']}\n"
        # Create an "action" (for demo purpose, return a planned step)
        action = f"[PLAN by {self.name}] based on '{observation}' -> propose: '{self._propose(observation, related)}'"
        return {"introspection": introspection, "action": action, "related": related}

    def _propose(self, observation: str, related: List[Dict[str, Any]]):
        # mock proposal logic: choose strongest related memory or propose new idea
        if related and related[0]["score"] > 0.1:
            return f"extend '{related[0]['text']}'"
        else:
            return f"investigate '{observation}'"

# -------------------------
# Evaluator Agent
# -------------------------
@ray.remote
class EvaluatorAgent:
    def __init__(self, name: str):
        self.name = name
        print(f"[EvaluatorAgent:{self.name}] ready")

    def score_actions(self, actions: List[str]) -> List[Dict[str, Any]]:
        """
        Score actions on a toy heuristic: shorter is better, presence of keyword 'investigate' is higher novelty.
        Returns list with {action, score}
        """
        scored = []
        for a in actions:
            score = 1.0 / (len(a) + 1)
            if "investigate" in a:
                score += 0.2
            scored.append({"action": a, "score": float(score)})
        # sort descending by score
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored

# -------------------------
# Meta-Agent (coordinator)
# -------------------------
@ray.remote
class MetaAgent:
    def __init__(self, name: str, reasoners: List[ray.actor.ActorHandle], evaluator: ray.actor.ActorHandle):
        self.name = name
        self.reasoners = reasoners
        self.evaluator = evaluator
        print(f"[MetaAgent:{self.name}] initialized with {len(reasoners)} reasoner(s)")

    def coordinate_task(self, task: str):
        """
        Broadcast task to all reasoners, collect proposals, ask evaluator to rank, then pick winner.
        """
        # 1) ask reasoners to perceive and act
        futures = [r.perceive_and_act.remote(task) for r in self.reasoners]
        results = ray.get(futures)

        # 2) collect actions and introspections
        actions = [res["action"] for res in results]
        introspections = [res["introspection"] for res in results]

        # 3) evaluate actions
        scored = ray.get(self.evaluator.score_actions.remote(actions))

        # 4) choose top action
        top = scored[0] if scored else None

        return {
            "task": task,
            "introspection": introspections,
            "actions_scored": scored,
            "chosen": top,
            "raw_results": results
        }

# -------------------------
# Example run / demo
# -------------------------
def demo_run(n_reasoners: int = 3):
    print("\n=== Starting Ray (demo) ===")
    # initialize Ray - use local if already running
    try:
        ray.init(ignore_reinit_error=True)
    except Exception as e:
        print("[Warning] ray.init() raised:", e)
        ray.init()

    print("[main] Ray initialized.")

    # Create memory agents and reasoners
    memory_agents = [MemoryAgent.remote(name=f"Mem-{i}") for i in range(n_reasoners)]
    reasoners = [ReasonerAgent.remote(name=f"R-{i}", memory_agent=memory_agents[i]) for i in range(n_reasoners)]
    evaluator = EvaluatorAgent.remote(name="Eval-1")
    meta = MetaAgent.remote(name="Meta-1", reasoners=reasoners, evaluator=evaluator)

    # Seed some memories in each memory agent to simulate prior knowledge
    seed_texts = [
        "The system should prioritize safety checks before deploying.",
        "We experimented with lightweight retrieval-augmented generation.",
        "Memory sharding reduces latency for localized queries.",
        "Investigate anomalies in the telemetry pipeline.",
        "Autoscaling may increase cost but reduces latency peaks."
    ]
    # Distribute seeds across memory agents
    for i, mem in enumerate(memory_agents):
        for t in seed_texts[i::len(memory_agents)]:
            ray.get(mem.add.remote(t, {"seed_for": f"mem-{i}"}))

    # Main coordination tasks
    tasks = [
        "Optimize response latency for user queries",
        "Reduce cost of the cluster while preserving QoS",
        "Investigate telemetry spikes in the past hour",
    ]

    for task in tasks:
        print("\n>>> MetaAgent coordinating task:", task)
        result = ray.get(meta.coordinate_task.remote(task))
        print("--- INTROSPECTIONS ---")
        for intr in result["introspection"]:
            print(intr)
        print("\n--- ACTIONS SCORED ---")
        for s in result["actions_scored"]:
            print(f"score={s['score']:.4f} action={s['action']}")
        print("\n--- CHOSEN ACTION ---")
        print(result["chosen"])
        time.sleep(0.5)

    # Inspect memory contents
    print("\n=== Inspecting memories ===")
    for i, mem in enumerate(memory_agents):
        mem_dump = ray.get(mem.dump.remote())
        print(f"[Memory {i}] entries: {len(mem_dump)}")
        for e in mem_dump:
            print("  -", e["text"])

    # Cleanup
    print("\n=== Demo complete ===")
    # It is okay to leave Ray running; uncomment the next line to shut it down automatically:
    # ray.shutdown()


if __name__ == "__main__":
    demo_run(n_reasoners=3)
