# A04 · Reject a lost update

Update a record only when the caller holds the current version, using an immediate SQLite transaction.

## Skills and purpose
This lab teaches **optimistic version checks** through an observable execution path. When should a client retry automatically, and when must it reconcile the conflicting edit?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"key": "a", "value": "first", "expected_version": 0}`. Expected fields: `{"version": 1}`.
2. Input `{"key": "b", "value": "second", "expected_version": 0}`. Expected fields: `{"version": 1}`.
3. Input `{"key": "c", "value": "third", "expected_version": 0}`. Expected fields: `{"version": 1}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
