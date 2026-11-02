# B19 · A graph inside a graph

Compose a reusable normalization graph as a node in a parent workflow.

## Skills and purpose
This lab teaches **compiled subgraph composition** through an observable execution path. When should child and parent share a state schema, and when is an adapter preferable?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"text": " one   two "}`. Expected fields: `{"normalized": "one two", "answer": "ONE TWO"}`.
2. Input `{"text": "tools"}`. Expected fields: `{"answer": "TOOLS"}`.
3. Input `{"text": "state graph"}`. Expected fields: `{"answer": "STATE GRAPH"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
