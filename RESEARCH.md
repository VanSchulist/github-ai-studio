# 🔬 Studio Research & Technical Intelligence

This living research log tracks developments across frontier models, protocol specifications, agent architectures, and developer tooling in 2025–2026. Every studio project originates from evidence recorded here.

---

## 🌐 1. The Model Context Protocol (MCP) Landscape

### Overview & Mechanics
Anthropic's open-source **Model Context Protocol (MCP)** has emerged as the universal USB-C cable for AI models, providing a standardized JSON-RPC 2.0 transport (via `stdio` or Server-Sent Events / SSE) that allows LLMs to query external data sources (Resources), invoke executable tools (Tools), and access pre-configured system context (Prompts).

### Key Technical Challenges Identified
1. **Tool Namespace Pollution & Token Bloat**: When an agent connects to 10+ MCP servers, sending complete JSON schemas for 50+ tools in every turn exhausts 15k–30k tokens before any user prompt is processed, causing severe attention degradation.
2. **Lack of Dynamic Tool Discovery**: Most clients load all tools statically at initialization. There is no standard "two-tier" tool discovery where an agent first searches an index of tools and loads schemas lazily on demand.
3. **Execution Sandbox & Permission Blindspots**: MCP clients execute tools with the host process's full user privileges. An agent executing a tool has no fine-grained boundary between benign read operations and catastrophic filesystem writes.

---

## 🧠 2. Frontier LLM Capabilities & Agentic Benchmarks

### Gemini API (2.0 / 2.5 Architecture)
* **Native Tool Calling**: Gemini 2.0 Flash / Pro features optimized native function-calling latency (sub-500ms TTFT) with support for strict JSON schema enforcement (`response_schema`).
* **Long Context Advantage (2M+ Tokens)**: While Gemini easily handles 1M+ tokens, empirical tests show that retrieving needles from complex, unstructured code repositories drops in precision beyond 200k tokens unless aided by structural AST maps or graph-augmented indices.
* **Multimodal Streaming**: Gemini Live API over WebSockets enables bidirectional streaming audio/video with native voice activity detection (VAD), opening greenfield opportunities for voice-driven pairing agents.

### Reasoning Models & Agentic Coding
* Reasoning-heavy models (Claude 3.7 Sonnet hybrid thinking, DeepSeek-R1) generate extensive internal scratchpads.
* The bottleneck for coding agents has shifted from **raw generation quality** to **context management and verification loops**:
  * Can the agent locate the exact lines needing edits without hallucinating line drifts?
  * Can the agent autonomously run unit tests, read compiler errors, and self-heal before requesting human review?

---

## 🛠️ 3. Developer Tooling & Agentic Coding Gaps (2025–2026)

Based on systematic monitoring of developer communities (X, Reddit r/ExperiencedDevs, GitHub discussions):

1. **Context Window Decay ("Agent Rot")**:
   * Coding agents in multi-turn sessions (Cursor, Claude Code, Cline, Antigravity) degrade in coherence after 10–15 turns. 
   * Root cause: the context window fills with raw terminal logs, outdated file snapshots, and redundant intermediate tool outputs.
2. **Phantom Code & Duplicate Utilities**:
   * Agents frequently hallucinate new utility files (`helpers.py`, `utils.js`) across separate turns instead of reusing existing architecture.
3. **Deterministic Evaluation Gap**:
   * Developers building agents have no standardized, lightweight test framework to verify whether their agent's prompt updates improved or broke tool-calling reliability across 50 multi-turn test scenarios.
