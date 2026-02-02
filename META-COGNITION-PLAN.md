# META-COGNITION-PLAN.md
## Repository Self-Model & Architectural Cognition Engine

---

## Frontmatter

```yaml
project: instrumental-reasoning-ai
version: 1.0.0
phase: meta-cognition-system
waves: 6
total_tasks: 21
autonomous: partial
estimated_complexity: high
```

---

## Phase Goal

Build a system that allows the repository to model itself, evaluate structural integrity, detect architectural drift, and propose corrective evolution strategies.

---

## must_haves (Goal-Backward Derivation)

- [ ] Repository transformed into queryable cognitive graph
- [ ] All artifacts classified by ontology type
- [ ] Invariant violations detected automatically
- [ ] CCI (Cognitive Coherence Index) computed
- [ ] Theory corpus consulted for remediation
- [ ] Temporal patterns identified from memory
- [ ] Structured refactor proposals generated

---

## Wave 1: Foundation Layer
**depends_on:** none
**parallel:** true

### Task 1.1: Define Graph Schema

```xml
<task id="1.1">
  <name>Define Cognitive Graph Schema</name>
  <layer>00_foundation</layer>
  <ontology_class>Model</ontology_class>
  <files_modified>
    - /00_foundation/schemas/cognitive-graph.schema.json
  </files_modified>
  <description>
    Define the schema for RepoCognitionGraph with node types:
    - FileNode (source files)
    - LayerNode (cognitive layers/folders)
    - KnowledgeNode (theory MD files)
    - MemoryNode (session logs)
    - ConstraintNode (invariants)

    Edge types:
    - DependencyEdge (imports)
    - EvaluationEdge (test coverage)
    - TemporalEdge (session sequences)
    - ViolationEdge (constraint breaches)
  </description>
  <verification>
    - Schema validates with JSON Schema Draft 7+
    - All node/edge types documented
    - Example graph instance validates
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 1.2: Define Ontology Classification Schema

```xml
<task id="1.2">
  <name>Define Artifact Ontology Schema</name>
  <layer>00_foundation</layer>
  <ontology_class>Model</ontology_class>
  <files_modified>
    - /00_foundation/schemas/ontology-classification.schema.json
  </files_modified>
  <description>
    Define classification schema for artifact types:
    - Model, Mechanism, Interface, Agent
    - Evaluation, Experiment, Theory, Memory, Invariant

    Include:
    - Classification rules (file patterns, content markers)
    - Confidence scoring
    - Anomaly flagging for unclassified
  </description>
  <verification>
    - Schema covers all 9 ontology types
    - Classification rules are deterministic
    - Anomaly detection criteria defined
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 1.3: Define Invariants as Executable Rules

```xml
<task id="1.3">
  <name>Codify Repository Invariants</name>
  <layer>00_foundation</layer>
  <ontology_class>Invariant</ontology_class>
  <files_modified>
    - /00_foundation/invariants/rules.json
    - /00_foundation/invariants/README.md
  </files_modified>
  <description>
    Transform natural language invariants into executable rules:

    1. experiments_no_core_deps: Experiments cannot import from layers 00-05
    2. core_no_experiment_deps: Core layers cannot import from 06_experiments
    3. eval_no_generation: Evaluation cannot import mechanism internals
    4. agents_no_model_mutation: Agents cannot directly modify model files
    5. mechanisms_stateless: Mechanisms cannot have module-level mutable state
    6. schema_binding: All outputs reference declared schemas
    7. ontology_placement: All files must map to ontology class
    8. no_cross_layer_side_effects: No hidden mutations across layers
  </description>
  <verification>
    - All 8 invariants codified
    - Each rule has detection logic spec
    - Rules are composable for violation detection
  </verification>
  <autonomous>true</autonomous>
</task>
```

---

## Wave 2: Graph Construction Mechanisms
**depends_on:** Wave 1
**parallel:** true

### Task 2.1: File System Scanner

```xml
<task id="2.1">
  <name>Build Repository Scanner</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/graph/scanner.py
  </files_modified>
  <description>
    Stateless mechanism that:
    - Walks repository directory tree
    - Extracts file metadata (path, type, size, modified)
    - Identifies cognitive layer from path
    - Outputs FileNode and LayerNode candidates

    Input: repo_root path
    Output: List[RawFileRecord]
  </description>
  <verification>
    - Scans repository without side effects
    - Correctly identifies all cognitive layers
    - Handles symlinks, ignores .git
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 2.2: Dependency Extractor

```xml
<task id="2.2">
  <name>Build Import Dependency Extractor</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/graph/dependency_extractor.py
  </files_modified>
  <description>
    Stateless mechanism that:
    - Parses source files for import statements
    - Resolves relative/absolute imports to file paths
    - Supports: Python, TypeScript, JavaScript
    - Outputs DependencyEdge candidates

    Input: FileNode
    Output: List[DependencyEdge]
  </description>
  <verification>
    - Extracts imports from Python files
    - Extracts imports from TS/JS files
    - Resolves paths correctly
    - No false positives from comments/strings
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 2.3: Ontology Classifier

```xml
<task id="2.3">
  <name>Build Ontology Classification Engine</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/graph/ontology_classifier.py
  </files_modified>
  <description>
    Stateless mechanism that classifies artifacts:

    Classification rules:
    - /00_foundation/** → Invariant/Model (by content)
    - /01_models/** → Model
    - /02_mechanisms/** → Mechanism
    - /03_interfaces/** → Interface
    - /04_agents/** → Agent
    - /05_evaluation/** → Evaluation
    - /06_experiments/** → Experiment
    - /07_memory/** → Memory
    - /08_theory/** or *.md → Theory

    Content analysis for edge cases.
    Flag unclassified as ontological anomalies.
  </description>
  <verification>
    - Classifies files by path pattern
    - Content analysis for ambiguous cases
    - Returns confidence score
    - Flags anomalies correctly
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 2.4: Graph Builder

```xml
<task id="2.4">
  <name>Build Cognitive Graph Assembler</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/graph/builder.py
  </files_modified>
  <description>
    Orchestrates graph construction:

    1. Run scanner → RawFileRecords
    2. Run classifier → Classified nodes
    3. Run dependency extractor → Edges
    4. Assemble into RepoCognitionGraph
    5. Validate against schema

    Output: RepoCognitionGraph (JSON or NetworkX)
  </description>
  <verification>
    - Produces valid graph per schema
    - All nodes have ontology classification
    - All edges reference valid nodes
    - Graph is serializable
  </verification>
  <autonomous>true</autonomous>
</task>
```

---

## Wave 3: Violation Detection & Metrics
**depends_on:** Wave 2
**parallel:** true

### Task 3.1: Invariant Violation Detector

```xml
<task id="3.1">
  <name>Build Invariant Violation Detector</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/analysis/violation_detector.py
  </files_modified>
  <description>
    Analyzes RepoCognitionGraph against invariant rules:

    For each invariant:
    - Query graph for violation patterns
    - Cross-layer dependencies (layer index comparison)
    - Eval→Generation imports (ontology type check)
    - Agent→Model mutations (write detection)
    - Stateful mechanisms (AST analysis)

    Output: List[ViolationReport]

    ViolationReport:
    - invariant_id
    - source_node
    - target_node (if applicable)
    - severity: critical | warning | info
    - evidence: string
  </description>
  <verification>
    - Detects all 8 invariant violation types
    - No false positives on compliant code
    - Severity correctly assigned
    - Evidence is actionable
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 3.2: CCI Metric Calculator

```xml
<task id="3.2">
  <name>Build Cognitive Coherence Index Calculator</name>
  <layer>05_evaluation</layer>
  <ontology_class>Evaluation</ontology_class>
  <files_modified>
    - /05_evaluation/metrics/cci.py
  </files_modified>
  <description>
    Computes Cognitive Coherence Index from graph:

    Metrics (0-1 scale each):
    1. cross_layer_ratio: 1 - (cross_layer_edges / total_edges)
    2. schema_coverage: classified_nodes / total_nodes
    3. test_coverage: tested_mechanisms / total_mechanisms
    4. theory_utilization: referenced_theory / total_theory
    5. violation_density: 1 - (violations / max_possible)
    6. memory_stability: 1 - (churn_zones / total_zones)

    CCI = weighted_average(metrics)

    Output: CCIReport with breakdown
  </description>
  <verification>
    - All 6 metrics computed correctly
    - CCI in range [0, 1]
    - Breakdown shows contribution
    - Identifies weakest metric
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 3.3: Entropy Source Identifier

```xml
<task id="3.3">
  <name>Build Entropy Source Identifier</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/analysis/entropy_identifier.py
  </files_modified>
  <description>
    Identifies sources of architectural entropy:

    Entropy signals:
    - High fan-out nodes (dependency explosion)
    - High fan-in nodes (god modules)
    - Unclassified nodes (ontological gaps)
    - Circular dependencies
    - Layer boundary violations
    - Orphan nodes (no connections)

    Output: List[EntropySource] with location and type
  </description>
  <verification>
    - Detects all entropy signal types
    - Ranks by severity
    - Provides actionable locations
  </verification>
  <autonomous>true</autonomous>
</task>
```

---

## Wave 4: Theory & Memory Integration
**depends_on:** Wave 3
**parallel:** true

### Task 4.1: Theory Consultation Engine

```xml
<task id="4.1">
  <name>Build Theory Consultation Engine</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/theory/consultation_engine.py
  </files_modified>
  <description>
    Searches /08_theory for relevant knowledge:

    Input: ViolationReport or EntropySource

    Process:
    1. Extract keywords from issue
    2. Search theory files by domain:
       - AlgorithmicPattern
       - CognitiveModel
       - FailurePattern
       - SecurityPattern
       - EvaluationStrategy
       - ArchitecturalStyle
    3. Rank by relevance
    4. Extract remediation guidance

    Output: List[TheoryMatch] with excerpts
  </description>
  <verification>
    - Searches all theory domains
    - Relevance ranking is sensible
    - Returns actionable excerpts
    - Handles empty theory corpus gracefully
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 4.2: Temporal Memory Analyzer

```xml
<task id="4.2">
  <name>Build Temporal Memory Analyzer</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/memory/temporal_analyzer.py
  </files_modified>
  <description>
    Analyzes /07_memory for historical patterns:

    Detects:
    - Repeated violation zones (same file/module)
    - Frequently refactored modules
    - Decisions causing later instability
    - Churn hotspots over time

    Input: RepoCognitionGraph + session logs
    Output: TemporalAnalysis with:
    - hotspot_modules
    - recurring_violations
    - causal_chains (decision → instability)
  </description>
  <verification>
    - Parses session log format
    - Identifies recurring patterns
    - Links decisions to outcomes
    - Works with sparse memory
  </verification>
  <autonomous>true</autonomous>
</task>
```

---

## Wave 5: Proposal Generation
**depends_on:** Wave 4
**parallel:** false

### Task 5.1: Refactor Proposal Generator

```xml
<task id="5.1">
  <name>Build Refactor Proposal Generator</name>
  <layer>02_mechanisms</layer>
  <ontology_class>Mechanism</ontology_class>
  <files_modified>
    - /02_mechanisms/proposals/generator.py
  </files_modified>
  <description>
    Synthesizes all analysis into structured proposals:

    Input:
    - ViolationReports
    - CCIReport
    - EntropySources
    - TheoryMatches
    - TemporalAnalysis

    Output per issue:
    ```
    STRUCTURAL ISSUE: {description}
    LOCATION: {file:line or module}
    ONTOLOGY CLASS: {current → suggested}
    INVARIANT VIOLATED: {invariant_id}
    THEORY PATTERN MATCH: {theory_file: excerpt}
    HISTORICAL SIGNAL: {from temporal analysis}
    PROPOSED REFACTOR STRATEGY: {actionable steps}
    RISK LEVEL: {critical | high | medium | low}
    ```

    Proposals are evolution strategies, not patches.
  </description>
  <verification>
    - All fields populated for each issue
    - Strategies are architectural, not tactical
    - Risk levels reflect invariant severity
    - Proposals are actionable
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 5.2: Report Formatter

```xml
<task id="5.2">
  <name>Build Cognition Report Formatter</name>
  <layer>03_interfaces</layer>
  <ontology_class>Interface</ontology_class>
  <files_modified>
    - /03_interfaces/reports/cognition_report.py
  </files_modified>
  <description>
    Formats analysis into consumable reports:

    Formats:
    - Markdown (human readable)
    - JSON (machine readable)
    - SARIF (IDE integration)

    Sections:
    1. Executive Summary (CCI score, critical issues)
    2. Invariant Violations (grouped by type)
    3. Entropy Analysis (hotspots visualization)
    4. Refactor Proposals (prioritized)
    5. Temporal Insights (historical context)
  </description>
  <verification>
    - All 3 formats produced correctly
    - Markdown renders properly
    - JSON validates against schema
    - SARIF compatible with VS Code
  </verification>
  <autonomous>true</autonomous>
</task>
```

---

## Wave 6: Agent & Integration
**depends_on:** Wave 5
**parallel:** true

### Task 6.1: Cognition Agent

```xml
<task id="6.1">
  <name>Build Autonomous Cognition Agent</name>
  <layer>04_agents</layer>
  <ontology_class>Agent</ontology_class>
  <files_modified>
    - /04_agents/cognition_agent.py
  </files_modified>
  <description>
    Autonomous agent that orchestrates the full pipeline:

    Loop:
    1. Build cognitive graph
    2. Run violation detection
    3. Compute CCI
    4. Identify entropy sources
    5. Consult theory
    6. Analyze temporal memory
    7. Generate proposals
    8. Format and output report

    Triggers:
    - On-demand (CLI invocation)
    - Pre-commit hook
    - Scheduled (CI/CD)

    Does NOT directly modify files (read-only analysis).
  </description>
  <verification>
    - Full pipeline executes end-to-end
    - Agent is stateless between runs
    - No file modifications occur
    - Clean error handling
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 6.2: CLI Interface

```xml
<task id="6.2">
  <name>Build CLI Interface</name>
  <layer>03_interfaces</layer>
  <ontology_class>Interface</ontology_class>
  <files_modified>
    - /03_interfaces/cli/cognition_cli.py
  </files_modified>
  <description>
    Command-line interface for the system:

    Commands:
    - `cognition scan` - Build graph and basic analysis
    - `cognition violations` - List invariant violations
    - `cognition cci` - Compute and display CCI
    - `cognition entropy` - Identify entropy sources
    - `cognition propose` - Generate refactor proposals
    - `cognition report [--format md|json|sarif]` - Full report

    Flags:
    - `--path` - Repository root
    - `--output` - Output file
    - `--verbose` - Detailed logging
  </description>
  <verification>
    - All commands functional
    - Help text accurate
    - Exit codes meaningful
    - Output formats correct
  </verification>
  <autonomous>true</autonomous>
</task>
```

### Task 6.3: Session Memory Writer

```xml
<task id="6.3">
  <name>Build Session Memory Writer</name>
  <layer>07_memory</layer>
  <ontology_class>Memory</ontology_class>
  <files_modified>
    - /07_memory/session_writer.py
  </files_modified>
  <description>
    Records analysis sessions to memory:

    After each cognition run, writes:
    /07_memory/session_YYYY_MM_DD_HH_MM.md

    Contents:
    - CCI score and trend
    - Violations found
    - Proposals generated
    - Invariants stressed
    - Entropy sources identified

    This builds temporal coherence for future analysis.
  </description>
  <verification>
    - Sessions recorded with timestamp
    - Format parseable by temporal analyzer
    - No duplicate sessions
    - Atomic writes
  </verification>
  <autonomous>true</autonomous>
</task>
```

---

## Verification Criteria (Full System)

```yaml
functional:
  - Repository scanned and graph built
  - All artifacts classified by ontology
  - Invariant violations detected with zero false negatives
  - CCI computed with all 6 metrics
  - Theory consultation returns relevant matches
  - Temporal analysis identifies patterns
  - Proposals are structured and actionable
  - CLI commands all functional

architectural:
  - Mechanisms are stateless
  - Evaluation code imports no generation logic
  - Agent does not modify repository
  - All outputs conform to declared schemas
  - No cross-layer violations in implementation

quality:
  - Test coverage > 80% for mechanisms
  - Documentation for all public interfaces
  - Error messages are actionable
  - Performance: full scan < 30s for 1000 files
```

---

## Dependency Graph

```
Wave 1 (Foundation)
├── 1.1 Graph Schema
├── 1.2 Ontology Schema
└── 1.3 Invariant Rules
       │
       ▼
Wave 2 (Graph Construction)
├── 2.1 Scanner
├── 2.2 Dependency Extractor
├── 2.3 Ontology Classifier
└── 2.4 Graph Builder ←── depends on 2.1, 2.2, 2.3
       │
       ▼
Wave 3 (Analysis)
├── 3.1 Violation Detector
├── 3.2 CCI Calculator
└── 3.3 Entropy Identifier
       │
       ▼
Wave 4 (Intelligence)
├── 4.1 Theory Consultation
└── 4.2 Temporal Analyzer
       │
       ▼
Wave 5 (Synthesis)
├── 5.1 Proposal Generator ←── depends on all Wave 3, 4
└── 5.2 Report Formatter
       │
       ▼
Wave 6 (Integration)
├── 6.1 Cognition Agent
├── 6.2 CLI Interface
└── 6.3 Session Memory Writer
```

---

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| Import parsing incomplete | Start with Python, expand iteratively |
| Theory corpus empty | Graceful degradation, document need |
| Memory logs unstructured | Define format, migrate existing |
| False positive violations | Tunable confidence thresholds |
| Performance at scale | Incremental graph updates |

---

## Success State

When complete, the repository gains:

- **Self-structural awareness** - Knows its own shape
- **Architectural immune response** - Detects violations automatically
- **Theory-grounded evolution** - Uses knowledge for remediation
- **Long-term coherence** - Learns from history

The repository becomes a **self-regulating cognitive organism**.

---

## Prime Directive

> The system must treat the repository itself as data, reason about its structural health, and guide its evolution.

This is meta-intelligence engineering.
