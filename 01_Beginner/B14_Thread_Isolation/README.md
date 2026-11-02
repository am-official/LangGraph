# B14 · Two threads, separate histories

Write two states to one checkpointer and verify that thread IDs select the intended checkpoint.

## Skills and purpose
This lab teaches **thread-scoped checkpoint lookup** through an observable execution path. Why is a thread ID an address for state rather than proof of authorization?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"first": 2, "second": 8}`. Expected fields: `{"first": 3, "second": 9}`.
2. Input `{"first": 0, "second": 0}`. Expected fields: `{"first": 1, "second": 1}`.
3. Input `{"first": 9, "second": 1}`. Expected fields: `{"first": 10, "second": 2}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
