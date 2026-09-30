# 🧪 Experiment 01: Gemini 2.0 Tool-Calling Latency & Precision Under Schema Bloat

> **Status**: IN PROGRESS  
> **Target Question**: *"How does tool-calling precision, parameter accuracy, and Time-To-First-Token (TTFT) degrade in Gemini 2.0 when exposed to 50+ tool schemas versus 3 lazy gateway meta-tools?"*  
> **Lead Researcher**: Van Schulist (@VanSchulist / Existential Cloud)

---

## 🎯 Hypothesis
1. Presenting 50+ raw JSON schemas to the model at Turn 0 creates severe attention dispersion ("Lost in the Middle"), increasing parameter hallucination and schema invalidation by >30%.
2. Employing a two-tier lazy routing pattern (via `mcp-mesh` meta-tools: `mesh_search_tools` -> `mesh_invoke_tool`) reduces Turn-0 prompt token overhead by >85% and improves tool selection accuracy from ~72% to >95%.

---

## 🔬 Experimental Protocol

### Variable Matrix
* **Independent Variable**: Tool Schema Delivery Mechanism:
  * **Condition A (Baseline - Raw MCP)**: 50 full JSON schemas injected into `tools` parameter at Turn 0.
  * **Condition B (Treatment - `mcp-mesh` Lazy Gateway)**: 3 meta-tools (`mesh_search_tools`, `mesh_describe_tool`, `mesh_invoke_tool`) exposed at Turn 0.
* **Dependent Variables**:
  * Turn-0 Token Overhead (Prompt tokens).
  * Time-To-First-Token (TTFT in milliseconds).
  * Tool Selection Precision (Does the model pick the correct tool across 25 intent queries?).
  * Argument Validation Rate (% of generated arguments matching schema without type errors).

---

## 📊 Dataset & Query Battery
* **Synthetic Tool Suite**: 50 realistic developer tools spanning GitHub, PostgreSQL, Docker, AWS, Slack, and Filesystem (located in `d:\AntiGravity\Test Claude\mcp-mesh\examples\`).
* **Test Queries**: 25 standardized ambiguous, multi-step, and targeted developer intent prompts.

---

## 💻 Running the Experiment
```bash
# Execute local evaluation against mock tools
python experiment.py --runs 10
```
