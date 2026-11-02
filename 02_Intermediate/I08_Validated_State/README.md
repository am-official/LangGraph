# I08 · Validate before orchestration

Enforce a Pydantic input boundary before creating and executing the graph.

## Skills and purpose
This lab teaches **Pydantic validation at the graph boundary** through an observable execution path. Why is a TypedDict annotation insufficient for hostile external input?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"quantity": 3, "unit_price": 2.5}`. Expected fields: `{"total": 7.5}`.
2. Input `{"quantity": 1, "unit_price": 0}`. Expected fields: `{"total": 0.0}`.
3. Input `{"quantity": 100, "unit_price": 1}`. Expected fields: `{"total": 100.0}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
