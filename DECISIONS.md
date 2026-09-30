# ⚖️ Architecture Decision Records (ADRs)

This document formalizes the technical, architectural, and operational decisions made across **Existential Cloud AI Studio**. Every entry follows the standard ADR structure (Context, Decision, Consequences).

---

## Index of Architecture Decisions

* [ADR-001: Core Language Stack & Runtimes](#adr-001-core-language-stack--runtimes)
* [ADR-002: Zero-External-Dependency Standard for CLI Utilities](#adr-002-zero-external-dependency-standard-for-cli-utilities)
* [ADR-003: Model Context Protocol (MCP) as Primary Interoperability Fabric](#adr-003-model-context-protocol-mcp-as-primary-interoperability-fabric)
* [ADR-004: Frontier Model Priority: Gemini Native + Open Model Fallback](#adr-004-frontier-model-priority-gemini-native--open-model-fallback)
* [ADR-005: Specification-First Engineering Gateways](#adr-005-specification-first-engineering-gateways)

---

### ADR-001: Core Language Stack & Runtimes
* **Date**: 2026-09-30
* **Status**: Accepted
* **Context**: We need runtime environments that maximize developer adoption, execution speed, agent tooling ergonomics, and AI library maturity.
* **Decision**: We standardize on a two-language studio tier:
  1. **Python (3.10+)**: Primary runtime for AI engines, data pipelines, document generation, and scientific/eval harnesses. Managed via `uv`.
  2. **TypeScript (Node.js 20+ / Bun)**: Primary runtime for browser extensions, web interfaces, and high-performance official MCP protocol transports.
* **Consequences**: Avoids multi-language fragmentation (Rust/Go reserved only for specialized performance bottlenecks if strictly needed later).

---

### ADR-002: Zero-External-Dependency Standard for CLI Utilities
* **Date**: 2026-09-30
* **Status**: Accepted
* **Context**: Many open-source AI developer tools fail to achieve viral adoption because installing them requires 500MB of heavy dependencies (Torch, LangChain, bloated web scrapers), which frequently break on differing OS platforms.
* **Decision**: All standalone CLI tools authored by the studio must function out of the box using **Python standard library only** (e.g., `urllib`, `re`, `json`, `argparse`, `dataclasses`, `unittest`). Optional rich visual dependencies (like `rich` or `textual`) must remain strictly optional enhancements that gracefully degrade to plain ANSI text.
* **Consequences**: Guarantees zero installation friction, instant execution, and bulletproof cross-platform compatibility across Windows, macOS, and Linux.

---

### ADR-003: Model Context Protocol (MCP) as Primary Interoperability Fabric
* **Date**: 2026-09-30
* **Status**: Accepted
* **Context**: Building proprietary API clients or point-to-point plugins for individual IDEs (Cursor, VS Code, JetBrains) causes massive maintenance overhead.
* **Decision**: Every major tool or capability engineered in the studio must provide an official **MCP Server interface**. This allows any MCP-compatible client (Claude Desktop, Cursor, Antigravity, Cline) to instantly utilize our tools with zero custom glue code.
* **Consequences**: Maximizes studio reach while outsourcing UI integration to established IDEs.

---

### ADR-004: Frontier Model Priority: Gemini Native + Open Model Fallback
* **Date**: 2026-09-30
* **Status**: Accepted
* **Context**: Agent tools require reliable function calling, fast inference, and cost-effective context processing.
* **Decision**: We prioritize **Google Gemini 2.0 / 2.5** (via the modern `google-genai` SDK) for long-context comprehension, multimodal tasks, and low-latency agent loops, while maintaining clean adapter interfaces to local models (via Ollama/vLLM) and OpenAI-compatible endpoints.
* **Consequences**: Leverages Gemini's million-token context advantage while ensuring our tools remain completely open-weights friendly.

---

### ADR-005: Specification-First Engineering Gateways
* **Date**: 2026-09-30
* **Status**: Accepted
* **Context**: "Vibe coding" without disciplined architecture leads to chaotic agent hallucinations, orphaned code, and lack of long-term maintainability.
* **Decision**: No project repository may be initialized without an approved `PROJECT_SPEC.md` containing: Problem Definition, User Personas, Architecture Diagram, 5-stage Roadmap, and Testing Strategy.
* **Consequences**: Enforces world-class engineering rigor while preserving rapid agentic development velocity.
