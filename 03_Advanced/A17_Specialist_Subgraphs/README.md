# A17 · Reusable specialist graphs

Compose separate analysis and review subgraphs, then synthesize their state outputs in a parent graph.

## Skills and purpose
This lab teaches **specialist subgraph contracts** through an observable execution path. What coupling appears when all specialist graphs share one large state schema?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"document": "one two"}`. Expected fields: `{"analysis": "Words: 2"}`.
2. Input `{"document": "one"}`. Expected fields: `{"analysis": "Words: 1"}`.
3. Input `{"document": "a b c"}`. Expected fields: `{"analysis": "Words: 3"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
