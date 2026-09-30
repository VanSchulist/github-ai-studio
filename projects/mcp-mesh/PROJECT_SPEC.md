# 📐 Project Specification: `mcp-mesh` (Flagship Project)

> **Document Status**: APPROVED & ACTIVE  
> **Version**: 1.0.0  
> **Author**: Van Schulist (@VanSchulist / Existential Cloud)  
> **Repository Target**: `VanSchulist/mcp-mesh`  
> **Architecture Classification**: Core Studio Flagship (Ecosystem Anchor)

---

## 1. Project Title & Executive Summary
* **Project Name**: `mcp-mesh`
* **Subtitle**: The Dynamic Model Context Protocol Gateway & Lazy Tool Router
* **One-Sentence Description**: A high-performance, zero-external-dependency MCP gateway that transparently aggregates dozens of upstream MCP servers and eliminates tool namespace bloat by indexing tools and loading full JSON schemas lazily on demand.

---

## 2. Problem Statement
The open-source Model Context Protocol (MCP) has established itself as the standard for connecting LLMs to external systems (databases, APIs, filesystems). However, real-world agent deployments face a critical architectural bottleneck:

1. **Context Window Token Bloat**:
   * Each connected MCP server registers multiple tools with rich JSON schemas (parameter descriptions, types, nested object definitions, enum constraints).
   * Connecting an agent to 10+ MCP servers (e.g., GitHub, Postgres, Slack, Memory, Filesystem, Terminal, Web Search) injects **40 to 100+ full tool schemas** directly into the system prompt on Turn 0.
   * This consumes between **15,000 to 40,000 tokens** before the user even types their first prompt.
2. **Attention Degradation & Retrieval Confusion ("Lost in the Middle")**:
   * LLMs suffer from severe attention drift and parameter hallucination when choosing from dozens of simultaneously exposed tool schemas.
   * Tool selection accuracy drops sharply, leading to misrouted calls, invalid JSON parameter construction, or failure to trigger tools entirely.
3. **Client Configuration Fragility**:
   * MCP clients (Cursor, Claude Desktop, Antigravity, Cline) require configuring and spawning individual stdio child processes for every single server. Managing 10 distinct server processes per client causes process leaks, port collisions, and configuration hell.

---

## 3. Target Users & Personas
1. **Agentic Coding Developers**: Developers using Claude Code, Cursor, Cline, or Antigravity who connect multiple MCP servers and want to cut prompt latency and API token costs by 80–90%.
2. **Autonomous Agent Engineers**: Teams building multi-agent workflows where agents need access to hundreds of organizational tools without blowing token limits or degrading inference quality.
3. **MCP Server Maintainers**: Developers who want to test, aggregate, and benchmark their custom MCP servers behind an ergonomic gateway.

---

## 4. Existing Solutions & Competitive Landscape
| Solution | Approach | Limitations |
| :--- | :--- | :--- |
| **Direct Client Config** (Default) | Client connects to every server directly via stdio; all tools loaded statically. | Token bloat scales linearly with tools; Turn-0 context exhaustion; severe attention degradation. |
| **Custom Prompt Instructions** | Telling the LLM in system prompt "only use tool X if necessary". | Does not reduce token consumption at all; JSON schemas are still passed in full. |
| **Heavy Orchestration Gateways** | Multi-GB Docker containers, Python frameworks with heavy dependencies (Torch, LangChain). | High latency, complex deployment, breaks on cross-platform setups, impossible to run as a lightweight stdio subprocess. |

---

## 5. Differentiation & Value Proposition
* **Zero External Dependencies**: Implemented in 100% pure Python standard library (`json`, `subprocess`, `argparse`, `sys`, `dataclasses`, `re`, `typing`). Instant execution on any machine with Python 3.10+ without `pip install` headaches.
* **Two-Tier Meta-Tool Protocol (Lazy Routing)**:
  * Instead of publishing 100 schemas to the LLM, `mcp-mesh` publishes only **two ergonomic meta-tools**:
    1. `search_tools(query: str, category?: str)`: Queries the embedded semantic index and returns ultra-compact summaries (10–20 tokens each) of relevant candidate tools.
    2. `invoke_tool(server: str, tool_name: str, arguments: dict)`: Lazily activates and forwards execution directly to the designated downstream server.
  * Optional **Smart Dynamic Pass-Through**: Dynamically surfaces full schemas only for actively queried tools during multi-turn sessions.
* **Token Savings of 85–95%**: Slashes Turn-0 tool schema footprint from 25,000+ tokens to under 800 tokens.
* **Transparent Stdio Multiplexing**: Connects to the host client as a single standard MCP stdio server while multiplexing child processes in the background.

---

## 6. MVP Scope (v1.0.0)
- [x] **Config Parser**: Reads standard JSON client configuration files (`mcp_mesh.json` or Claude/Cursor `mcpServers` format).
- [x] **Downstream Server Manager**: Spawns and manages downstream MCP server stdio processes with clean shutdown.
- [x] **Schema Registry & Compact Indexer**: Introspects downstream tools via `tools/list`, constructs a fast keyword/token BM25-style index, and builds compact signatures.
- [x] **JSON-RPC 2.0 Protocol Engine**: Compliant implementation of the Model Context Protocol specification over standard input/output (`stdio`).
- [x] **Meta-Tool Provider**:
  - Exposes `mesh_search_tools` for discovering relevant capabilities.
  - Exposes `mesh_describe_tool` for inspecting full schema if needed.
  - Exposes `mesh_invoke_tool` for proxying execution to downstream servers.
- [x] **Diagnostic CLI & Savings Meter**: Terminal CLI command `mcp-mesh stats` displaying total tools aggregated, downstream health, and estimated token savings.
- [x] **100% Unit Test Coverage**: Automated test suite testing registry, indexer, JSON-RPC parsing, and simulated server execution.

---

## 7. Non-Goals (Out of Scope for MVP)
* No cloud-hosted multi-tenant SaaS (must run 100% locally on developer machines).
* No heavy vector database requirements (no Chroma, Pinecone, or FAISS; semantic keyword matching with token overlap scoring is sufficient and instant).
* No GUI browser desktop application in core repository (visual web dashboard will be Satellite 1).

---

## 8. Architecture & System Flow

```text
 ┌────────────────────────────────────────────────────────┐
 │                    AI Client / IDE                     │
 │          (Claude Desktop, Cursor, Antigravity)         │
 └───────────────────────────┬────────────────────────────┘
                             │ stdio (JSON-RPC 2.0)
                             │ Only 2-3 Meta-Tools Exposed!
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │                   mcp-mesh Gateway                     │
 │  ┌──────────────────────────────────────────────────┐  │
 │  │      JSON-RPC 2.0 Parser & Stdio Transport       │  │
 │  └────────────────────────┬─────────────────────────┘  │
 │                           ▼                            │
 │  ┌──────────────────────────────────────────────────┐  │
 │  │        Tool Indexer & Token-Savings Registry      │  │
 │  │   (Keyword BM25, Categorization, Token Metrics)  │  │
 │  └────────────────────────┬─────────────────────────┘  │
 │                           ▼                            │
 │  ┌──────────────────────────────────────────────────┐  │
 │  │    Process Multiplexer & Upstream Stdio Router   │  │
 │  └────────────────────────┬─────────────────────────┘  │
 └───────────────────────────┼────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼ stdio             ▼ stdio             ▼ stdio
 ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
 │ Downstream    │   │ Downstream    │   │ Downstream    │
 │ Server 1      │   │ Server 2      │   │ Server 3      │
 │ (GitHub MCP)  │   │ (Postgres)    │   │ (Filesystem)  │
 └───────────────┘   └───────────────┘   └───────────────┘
```

---

## 9. Technology Stack
* **Language**: Python 3.10+
* **Dependencies**: 0 external packages (Standard Library: `json`, `sys`, `os`, `re`, `subprocess`, `argparse`, `dataclasses`, `typing`, `unittest`, `time`, `math`).
* **Packaging**: `pyproject.toml` (standard PEP 621 metadata, entry point CLI: `mcp-mesh`).
* **License**: MIT Open Source License.

---

## 10. Repository Structure
```text
mcp-mesh/
├── README.md               # Hero documentation, architecture diagrams, quickstart
├── LICENSE                 # MIT License
├── pyproject.toml          # PEP 621 packaging metadata
├── main.py                 # Standalone direct entry point
├── mcp_mesh/
│   ├── __init__.py         # Package export & version (1.0.0)
│   ├── core.py             # JSON-RPC 2.0 types, Protocol envelopes, Errors
│   ├── indexer.py          # Fast TF-IDF / Token-matching Tool Indexer & schema compression
│   ├── registry.py         # Downstream server registration & process supervisor
│   ├── proxy.py            # The MCP Stdio Server implementation & meta-tool handlers
│   └── cli.py              # CLI commands: start, list, stats, inspect
├── examples/
│   ├── mcp_mesh_config.json    # Example configuration connecting mock/real servers
│   └── mock_downstream_mcp.py  # Standalone mock downstream server for testing
└── tests/
    ├── __init__.py
    ├── test_core.py        # Protocol and JSON-RPC message tests
    ├── test_indexer.py     # Search relevancy and token metric tests
    ├── test_registry.py    # Server registration and discovery tests
    └── test_proxy.py       # End-to-end stdio routing and execution tests
```

---

## 11. Testing & Verification Strategy
1. **Unit Testing**:
   * Test JSON-RPC 2.0 serialization, request parsing, and error codes (`-32600`, `-32601`, `-32602`).
   * Test keyword search ranking and schema compression ratio calculation.
   * Test multi-server namespace conflict handling (e.g., both Server A and Server B exposing a tool named `search`).
2. **Integration Testing**:
   * Spawn a real mock downstream MCP server via `subprocess`, send `mesh_search_tools` and `mesh_invoke_tool` requests through the proxy, and assert valid execution responses.
3. **Performance & Token Benchmark**:
   * Measure Turn-0 token payload before and after `mcp-mesh` aggregation across 50 simulated tools.

---

## 12. Security & Isolation Considerations
* **No Network Exposure by Default**: Operates purely over local Unix sockets or process `stdio` pipes.
* **Execution Validation**: Arguments forwarded to downstream tools are validated against downstream JSON types before process forwarding.
* **Process Isolation**: Child server processes are terminated cleanly on gateway shutdown via SIGTERM / Windows process termination.

---

## 13. Project Roadmap & Satellite Generation
* **Phase 1: Core Engine & CLI (MVP v1.0.0)** - *Current*
  * Pure Python stdio multiplexer, search indexer, token meter, full test suite.
* **Phase 2: Benchmark Suite (`mcp-mesh-eval`)** - *Satellite 1*
  * Automated harness testing token reduction vs tool invocation success across September 2026 models (GPT-6 Astra, Claude Sonnet 5.5, Gemini 3.8 Flash, DeepSeek-V4.1-Flash).
* **Phase 3: Visualizer (`mcp-mesh-ui`)** - *Satellite 2*
  * Interactive terminal UI and web dashboard charting real-time tool calls, token savings, and downstream latencies.
* **Phase 4: Community Registry (`mcp-registry-cli`)** - *Satellite 3*
  * Zero-config 1-command installer for popular community MCP servers.
