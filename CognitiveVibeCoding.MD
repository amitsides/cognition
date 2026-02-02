# Cognitive Vibe Coding Framework

## The Paradigm Shift

You are not writing code. You are evolving a cognitive organism under architectural gravity.

---

## I. Core Principles

### The Prime Law
> No code may be written before ontology placement and invariant alignment.

### The 5-Second Rule
Before any prompt, ask: **"Where does this belong in the system's ontology?"**

If you cannot answer in 5 seconds, you are about to create entropy.

---

## II. Cognitive Layer Architecture

```
/00_foundation   → invariants, ontology, trajectory
/01_models       → schemas, contracts, datatypes
/02_mechanisms   → algorithms, reasoning engines
/03_interfaces   → APIs, CLI, adapters
/04_agents       → autonomous logic units
/05_evaluation   → metrics, tests, scoring
/06_experiments  → unstable sandboxes
/07_memory       → session logs, decisions
/08_theory       → markdown knowledge corpus
```

These are cognitive strata. Cross-layer contamination is architectural damage.

---

## III. Artifact Types

| Type       | Purpose                              |
|------------|--------------------------------------|
| Model      | Defines structure of reality         |
| Mechanism  | Performs transformation or reasoning |
| Interface  | Connects system to outside world     |
| Agent      | Autonomous decision unit             |
| Evaluation | Measures correctness or performance  |
| Experiment | Unsafe sandbox for exploration       |
| Theory     | Externalized cognition (MD corpus)   |
| Memory     | Temporal reasoning record            |
| Invariant  | Architectural law                    |

---

## IV. Repository Invariants

1. Experiments never depend on core layers
2. Core layers never depend on experiments
3. All outputs must map to a declared schema
4. Evaluation code cannot import generation logic
5. Agents do not directly modify models
6. Mechanisms are stateless unless justified
7. Every artifact must have ontology placement
8. No hidden side-effects across layers

**Violation = Entropy**

---

## V. Role-Constrained Operations

| Role                | Allowed Scope        |
|---------------------|----------------------|
| Model Architect     | Schemas only         |
| Mechanism Engineer  | Logic only           |
| Evaluation Engineer | Metrics/tests only   |
| Agent Designer      | Decision loops       |
| Theory Synthesizer  | MD corpus usage      |

No role may violate layer boundaries.

---

## VI. Ontology (RDF/Turtle)

```turtle
@prefix vc:   <http://vibecoding.ai/ontology#> .
@prefix repo: <http://vibecoding.ai/repo#> .
@prefix cog:  <http://vibecoding.ai/cognition#> .
@prefix arch: <http://vibecoding.ai/architecture#> .
@prefix eval: <http://vibecoding.ai/evaluation#> .
@prefix mem:  <http://vibecoding.ai/memory#> .
@prefix md:   <http://vibecoding.ai/markdown#> .

# Core System
vc:VibeCodingSystem a owl:Class ;
    rdfs:comment "Human-AI co-cognitive software construction process." .

# Cognitive Layers
cog:CognitiveLayer a owl:Class .
repo:FoundationLayer   a cog:CognitiveLayer .
repo:ModelLayer        a cog:CognitiveLayer .
repo:MechanismLayer    a cog:CognitiveLayer .
repo:InterfaceLayer    a cog:CognitiveLayer .
repo:AgentLayer        a cog:CognitiveLayer .
repo:EvaluationLayer   a cog:CognitiveLayer .
repo:ExperimentLayer   a cog:CognitiveLayer .
repo:MemoryLayer       a cog:CognitiveLayer .
repo:TheoryLayer       a cog:CognitiveLayer .

# Invariants
arch:Invariant a owl:Class ;
    rdfs:comment "Non-negotiable architectural law." .

arch:forbidsDependencyOn a owl:ObjectProperty ;
    rdfs:domain arch:Invariant ;
    rdfs:range cog:CognitiveLayer .

# Knowledge Units
md:MarkdownKnowledgeUnit a owl:Class .
md:KnowledgeDomain a owl:Class .
md:AlgorithmicPattern    a md:KnowledgeDomain .
md:CognitiveModel        a md:KnowledgeDomain .
md:FailurePattern        a md:KnowledgeDomain .
md:SecurityPattern       a md:KnowledgeDomain .
md:EvaluationStrategy    a md:KnowledgeDomain .
md:ArchitecturalStyle    a md:KnowledgeDomain .

# Roles
vc:Role a owl:Class .
vc:MechanismEngineer   a vc:Role .
vc:ModelArchitect      a vc:Role .
vc:EvaluationEngineer  a vc:Role .
vc:AgentDesigner       a vc:Role .
vc:TheorySynthesizer   a vc:Role .

# Trajectory
arch:Trajectory a owl:Class .
arch:currentState          a owl:DatatypeProperty .
arch:nextCapability        a owl:DatatypeProperty .
arch:architecturalDirection a owl:DatatypeProperty .
arch:debtItem              a owl:DatatypeProperty .

# Prime Law
vc:OntologyPlacementLaw a arch:Invariant ;
    rdfs:comment "Every artifact must map to a cognitive layer and ontology class before implementation." .
```

---

## VII. Operational Protocol

### Before Any Task

```
Role: [choose role]
Target Layer: [layer]
Ontology Class: [class]
Relevant Invariants: [list]

Task: [delta, not feature]

Constraints:
- Obey invariants
- No cross-layer leakage
- Schema compliance required
- No hidden state
```

### After Each Session

Create: `/07_memory/session_YYYY_MM_DD.md`

Record:
- What was added
- Why
- Which invariant was stressed
- Potential future conflicts

---

## VIII. Experiment Graduation

An experiment graduates to core ONLY if:

- [ ] Passes evaluation metrics
- [ ] Matches model schemas
- [ ] Obeys all invariants

Until then, it remains epistemically unsafe.

---

## IX. Trajectory Management

Maintain `/00_foundation/TRAJECTORY.md` with:

1. **Current State** - What the system can do now
2. **Next Capability** - Immediate target
3. **Architectural Direction** - Long-term convergence
4. **Structural Debt** - Known violations to resolve

Coding without trajectory = random walk.

---

## X. SPARQL Navigation

```sparql
# Find artifact's layer
SELECT ?layer WHERE {
  ?artifact vc:belongsToLayer ?layer .
}

# List invariants for a layer
SELECT ?inv WHERE {
  ?inv arch:forbidsDependencyOn repo:MechanismLayer .
}

# Find relevant theory
SELECT ?doc WHERE {
  ?doc md:belongsToDomain md:EvaluationStrategy .
}
```

---

## XI. Mental Model

You are:
- Growing a cognitive organism
- Stabilizing architectural gravity
- Converting knowledge into mechanisms
- Evolving intelligence over time

If something feels chaotic, the violation is **architectural**, not technical.

---

## XII. What This Stabilizes

| Concept          | Effect                        |
|------------------|-------------------------------|
| Invariants       | Stops architectural drift     |
| Cognitive Layers | Prevents file sprawl          |
| Knowledge Units  | Converts notes into theory    |
| Roles            | Prevents cross-layer pollution|
| Experiment Rules | Protects core integrity       |
| Trajectory       | Ensures long-term direction   |
| Session Logs     | Builds temporal memory        |

---

This document is the orientation field. Everything in the repository exists inside its gravity.
