# A10 · An exportable graph

Invoke a graph exported for local HTTP serving and a future managed deployment workflow.

## Skills and purpose
This lab teaches **graph exports and functional HTTP validation** through an observable execution path. Why does a manifest or a listening port not establish a working managed deployment?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"request": "hello"}`. Expected fields: `{"answer": "Graph response: hello"}`.
2. Input `{"request": "state"}`. Expected fields: `{"answer": "Graph response: state"}`.
3. Input `{"request": "tools"}`. Expected fields: `{"answer": "Graph response: tools"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
