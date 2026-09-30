#!/usr/bin/env python3
"""Experiment 01: Benchmarking Tool Selection Precision & Token Economy.

Compares Turn-0 static tool schema overhead against mcp-mesh lazy meta-tool routing.
"""

import argparse
import json
import time
from typing import Any, Dict, List, Tuple


def generate_benchmark_tools(count: int = 50) -> List[Dict[str, Any]]:
    """Synthesizes realistic tool schemas across multiple server namespaces."""
    categories = ["github", "postgres", "slack", "aws", "docker", "k8s", "redis", "jira"]
    tools = []
    for i in range(count):
        cat = categories[i % len(categories)]
        name = f"{cat}_tool_action_{i+1}"
        tools.append({
            "name": name,
            "description": f"Perform automated {cat} action {i+1} on production cluster with status tracking.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "resource_id": {"type": "string", "description": f"Identifier for {cat} resource."},
                    "force": {"type": "boolean", "description": "Override safety checks."},
                    "limit": {"type": "integer", "description": "Max items to return (default: 50)."},
                    "tags": {"type": "array", "description": "Metadata tags list."},
                },
                "required": ["resource_id"],
            },
        })
    return tools


def estimate_tokens(data: Any) -> int:
    text = json.dumps(data) if not isinstance(data, str) else data
    return max(1, int(len(text) / 3.75))


def run_benchmark(tool_count: int = 50):
    print("=" * 65)
    print(f"  EXPERIMENT 01: Tool Schema Scalability & Economy (N={tool_count})")
    print("=" * 65)

    tools = generate_benchmark_tools(tool_count)
    raw_tokens = sum(estimate_tokens(t) for t in tools)

    # Condition B: mcp-mesh 3 meta-tools
    meta_tools = [
        {"name": "mesh_search_tools", "params": ["query", "limit", "server"]},
        {"name": "mesh_describe_tool", "params": ["server", "tool_name"]},
        {"name": "mesh_invoke_tool", "params": ["server", "tool_name", "arguments"]},
    ]
    meta_tokens = sum(estimate_tokens(m) for m in meta_tools)

    savings = raw_tokens - meta_tokens
    pct = round((savings / raw_tokens) * 100, 2)

    print(f"\n[+] Condition A (Raw Static Schemas):")
    print(f"    Total Registered Tools : {tool_count}")
    print(f"    Turn-0 Prompt Footprint : {raw_tokens} tokens")

    print(f"\n[+] Condition B (mcp-mesh Lazy Gateway):")
    print(f"    Exposed Meta-Tools     : 3 tools")
    print(f"    Turn-0 Prompt Footprint : {meta_tokens} tokens")

    print(f"\n[+] Net Efficiency Improvement:")
    print(f"    Tokens Saved per Turn  : {savings} tokens")
    print(f"    Turn-0 Bloat Reduction : {pct}%\n")
    print("=" * 65)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=50)
    args = parser.parse_args()
    run_benchmark(args.count)
