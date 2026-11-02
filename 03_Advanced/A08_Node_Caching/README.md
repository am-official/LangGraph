# A08 · Cache the right state

Cache a pure node by its complete input and verify identical inputs avoid repeated execution.

## Skills and purpose
This lab teaches **CachePolicy and pure-node input keys** through an observable execution path. What authorization or freshness bug appears when a tenant or data version is omitted from a cache key?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": "hello"}`. Expected fields: `{"answer": "HELLO", "node_calls": 1, "same_output": true}`.
2. Input `{"value": "cache"}`. Expected fields: `{"node_calls": 1}`.
3. Input `{"value": "state"}`. Expected fields: `{"answer": "STATE"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
