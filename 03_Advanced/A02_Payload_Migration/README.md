# A02 · Evolve persisted application state

Migrate an application payload inside a graph with explicit version checks and idempotent transformations.

## Skills and purpose
This lab teaches **versioned payload migration** through an observable execution path. Why must application-state migration be distinguished from serializer and dependency compatibility?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"schema_version": 1, "count": 3}`. Expected fields: `{"schema_version": 2, "count": 30, "idempotent": true}`.
2. Input `{"schema_version": 2, "count": 30}`. Expected fields: `{"migrated": false, "count": 30}`.
3. Input `{"schema_version": 1, "count": 0}`. Expected fields: `{"second_count": 0}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
