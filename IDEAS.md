# 💡 Studio Idea Backlog & Innovation Incubator

This document stores potential concepts, experiments, and product visions under observation. Ideas here are triaged and do **not** get coded immediately until they pass our formal selection gates.

---

## 🎯 Selection Criteria for Flagship & Satellites

To graduate from an idea into an active project, a concept must score high across 4 pillars:
1. **Real Friction**: Solves a painful, verifiable bottleneck that real developers or users complain about on X/GitHub/Reddit.
2. **Interconnected Architecture**: Can connect naturally to our ecosystem (spawning an MCP server, CLI, or benchmark).
3. **High Build-to-Value Ratio**: Can deliver an impactful MVP in 1–2 weeks, with clear runway for 6 months of iterations.
4. **Authentic Lore**: Fits the **Existential Cloud** brand (human agency vs. algorithmic opacity).

---

## 📋 Categorized Idea Backlog

### Category A: Agentic Coding & Context Optimization
* **Idea A1: `context-lens` (Agent Context Pruner & AST Compactor)**
  * *Concept*: A pre-flight CLI / MCP server that dynamically compresses repository files into an ultra-dense, AST-accurate outline before feeding into LLM prompts, slashing token costs by 60% and eliminating hallucinated line numbers.
  * *Status*: **Candidate for Flagship Project**.
* **Idea A2: `vibe-check` (Codebase Agentic Slop & Drift Scanner)**
  * *Concept*: A linter for codebases written with AI assistants, identifying duplicate helper functions, phantom imports, and verbose hallucinated comments.
  * *Status*: Incubating.

### Category B: Model Context Protocol (MCP) Infrastructure & Gateways
* **Idea B1: `mcp-mesh` (Observable Multi-Server Gateway & Lazy Schema Router)**
  * *Concept*: Solves the MCP namespace pollution problem. An intelligent router that proxies 20+ downstream MCP servers, exposes only a lightweight meta-tool to the agent, and dynamically loads tool schemas on demand.
  * *Status*: **Candidate for Flagship Project**.
* **Idea B2: `mcp-guard` (Zero-Trust Local Execution Sandbox for MCP)**
  * *Concept*: A security middleware intercepting and sandboxing MCP tool calls (filesystem, shell, network), enforcing human-in-the-loop approval policies with diff previews.
  * *Status*: **Candidate for Flagship Project**.

### Category C: Developer Verification & Evaluation Harnesses
* **Idea C1: `agent-eval-harness` (Deterministic Regression Testing for Coding Agents)**
  * *Concept*: A lightweight CLI that runs an agent through 30 multi-turn code refactoring and tool-calling scenarios, measuring prompt stability, error-recovery rate, and cost drift across model versions.
  * *Status*: **Candidate for Flagship Project**.
* **Idea C2: `gemini-live-pair` (Real-Time Voice & Screen Coding Companion)**
  * *Concept*: Leveraging Gemini Live API WebSockets for low-latency voice-interactive pair programming that watches terminal outputs and talks through architecture.
  * *Status*: Research Spike.

### Category D: Digital Survival & Career Armor (Existing Track)
* **Idea D1: `ghost-job-hunter-v2` (Live LinkedIn & Indeed Scraper Extension)**
  * *Concept*: Browser extension integration for `ghost-job-hunter` to overlay Ghost Probability Scores directly onto LinkedIn/Indeed job boards.
  * *Status*: Satellite Roadmap for Q1 2027.
