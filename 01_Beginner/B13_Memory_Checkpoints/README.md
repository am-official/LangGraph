# B13 · The last state is available

Save a graph state in an in-memory checkpointer and read it by thread ID.

## Skills and purpose
This lab teaches **checkpointer and thread configuration** through an observable execution path. What failure destroys an in-memory checkpoint even when a thread ID is stable?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"initial": 2}`. Expected fields: `{"count": 3, "saved_count": 3, "has_checkpoint": true}`.
2. Input `{"initial": 0}`. Expected fields: `{"count": 1}`.
3. Input `{"initial": 8}`. Expected fields: `{"saved_count": 9}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
