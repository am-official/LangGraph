# B03 · Update only what changes

Apply a partial state update and verify that unrelated fields survive.

## Skills and purpose
This lab teaches **partial node state updates** through an observable execution path. Why return only changed fields instead of rebuilding all state in every node?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"title": "note", "owner": "Ada"}`. Expected fields: `{"normalized": "NOTE", "owner": "Ada"}`.
2. Input `{"title": "state", "owner": "Lin"}`. Expected fields: `{"normalized": "STATE"}`.
3. Input `{"title": " tools ", "owner": "Sam"}`. Expected fields: `{"title": "tools", "owner": "Sam"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
