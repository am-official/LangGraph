# B12 · Architecture you can inspect

Export graph structure as Mermaid and Graphviz while running the same compiled workflow.

## Skills and purpose
This lab teaches **compiled graph inspection** through an observable execution path. Why is a graph diagram evidence of structure but not evidence of successful deployment?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": 4}`. Expected fields: `{"result": 9, "edge_count": 3}`.
2. Input `{"value": 0}`. Expected fields: `{"nodes": ["__end__", "__start__", "double", "offset"]}`.
3. Input `{"value": 7}`. Expected fields: `{"result": 15}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
