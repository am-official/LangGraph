# B15 · Checkpoints on disk

Write a graph checkpoint to SQLite and read it through a newly opened saver connection.

## Skills and purpose
This lab teaches **SQLite checkpoint durability** through an observable execution path. Which failures can one local SQLite file survive, and which need backups or replication?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"thread": "a", "initial": 4}`. Expected fields: `{"count": 5, "reopened_count": 5}`.
2. Input `{"thread": "b", "initial": 0}`. Expected fields: `{"reopened_count": 1}`.
3. Input `{"thread": "c", "initial": 10}`. Expected fields: `{"reopened_count": 11}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
