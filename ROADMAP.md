# 🗺️ Studio Strategic Roadmap

This document outlines the multi-phase engineering trajectory for **Existential Cloud AI Studio**. Every project under our umbrella aligns with these rigorous phased gateways.

---

## 📈 Lifecycle Gateways (The 8 Phases)

```text
Phase 0: Research ──> Phase 1: Prototype ──> Phase 2: MVP ──> Phase 3: Public Release
                                                                      │
Phase 7: Stable   <── Phase 6: Ecosystem <── Phase 5: Iterate <── Phase 4: Feedback
```

* **Phase 0 (Research)**: Literature survey, API protocol analysis, competitive gap audit, problem validation, and `PROJECT_SPEC.md` drafting.
* **Phase 1 (Prototype)**: Rapid, isolated proof-of-concept verifying technical feasibility and core cognitive/data pipelines.
* **Phase 2 (MVP)**: Minimal viable product with complete CLI/SDK, 100% unit test coverage, and single-command local execution.
* **Phase 3 (Public Release)**: v0.1.0 release, public GitHub launch, showcase documentation, and initial community dissemination on X.
* **Phase 4 (Feedback & Telemetry)**: Collecting real developer usage metrics, bug reports, and UX friction points.
* **Phase 5 (Iteration & Hardening)**: Performance optimization, edge-case mitigation, and API stabilization.
* **Phase 6 (Ecosystem Expansion)**: Spawning and interconnecting Satellite projects (MCP servers, visual dashboards, companion CLI tools).
* **Phase 7 (Stable Release)**: v1.0.0 production standard with long-term API stability and comprehensive developer documentation.

---

## 📍 Current Status & Active Focus

* **Current Stage**: **Phase 3 (Flagship Public Release & Satellite 1 Planning)**
* **Current Milestone**: `M1-FLAGSHIP-MVP` (Completed) -> `M1-EXPERIMENT-01` & `M2-SATELLITE-EVAL`
* **Timeline**: Week 1 (October 2026)

---

## 🎯 60-Day Studio Target Milestones

### Month 1: The Core Foundation (October 2026)

- [x] **M0.1 - Studio Infrastructure**: Initialize governance repository (`github-ai-studio`), documentation framework, decision records, and agent rules.
- [x] **M0.2 - Flagship Architectural Evaluation**: Review candidate flagship projects, select `mcp-mesh` as primary anchor, and author formal `PROJECT_SPEC.md`.
- [x] **M1.1 - Flagship Engine Prototype (Phase 1)**: Build the pure-Python zero-dependency MCP stdio gateway, keyword indexer, and lazy router.
- [x] **M1.2 - Flagship MVP Release (Phase 2 & 3)**: Complete CLI, automated test suite (21 unit tests passing), hero README, and publish `VanSchulist/mcp-mesh` v1.0.0 to GitHub.
- [ ] **M1.3 - Experiment Spike 1**: Launch first empirical test in `experiments/` benchmarking Gemini 3.8 Flash & frontier models tool-calling latency vs token footprint under lazy routing.
- [ ] **M1.4 - Satellite Project 1 (`mcp-mesh-eval`)**: Build automated benchmark harness comparing token reduction across frontier models.

### Month 2: Satellite Expansion & Ecosystem Weaving (November 2026)

- [ ] **M2.1 - Satellite Project 2 (`mcp-mesh-ui`)**: Create companion terminal dashboard or lightweight local web visualizer for real-time tool traffic.
- [ ] **M2.2 - Satellite Project 3 (`mcp-registry-cli`)**: Zero-config 1-command installer for popular community MCP servers.
- [ ] **M2.3 - Flagship v1.1.0 Iteration**: Implement dynamic LRU caching for high-frequency tool schemas and telemetry export.
- [ ] **M2.4 - Experiment Spike 2**: Multimodal agentic testing spike evaluating document parsing and code refactoring.

---

## 📊 Milestone Tracking Table

| Milestone ID | Target Date | Scope / Deliverable | Status |
| :--- | :--- | :--- | :--- |
| `M0-STUDIO-INIT` | 2026-09-30 | Establish studio infrastructure & governance docs | **DONE** |
| `M0-FLAGSHIP-PROPOSALS` | 2026-09-30 | 5 candidate flagship specifications and technical dossier | **DONE** |
| `M0-FLAGSHIP-SELECTION` | 2026-09-30 | Select `mcp-mesh` & finalize `PROJECT_SPEC.md` | **DONE** |
| `M1-FLAGSHIP-MVP` | 2026-09-30 | `mcp-mesh` v1.0.0 released on GitHub (100% test pass rate) | **DONE** |
| `M1-EXPERIMENT-01` | 2026-10-07 | Empirical LLM tool-calling benchmark published in `experiments/` | **ACTIVE** |
| `M2-SATELLITE-EVAL` | 2026-10-15 | Companion benchmark harness (`mcp-mesh-eval`) published | PENDING |
| `M2-SATELLITE-UI` | 2026-10-30 | Terminal visualizer (`mcp-mesh-ui`) published | PENDING |
| `M2-ECOSYSTEM-V1` | 2026-11-20 | Interconnected Flagship + Satellites live | PENDING |
