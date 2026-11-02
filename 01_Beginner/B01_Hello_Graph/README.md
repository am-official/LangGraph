# B01 · Your first graph

Build one node, connect it to the graph boundary, and inspect its state update.

## Skills and purpose
This lab teaches **StateGraph compilation and invocation** through an observable execution path. Why is graph construction separate from graph execution?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"name": "Ada"}`. Expected fields: `{"answer": "Hello, Ada!"}`.
2. Input `{"name": "Lin"}`. Expected fields: `{"answer": "Hello, Lin!"}`.
3. Input `{"name": " Sam "}`. Expected fields: `{"answer": "Hello, Sam!"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
