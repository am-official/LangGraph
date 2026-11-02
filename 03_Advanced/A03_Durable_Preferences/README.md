# A03 · A durable memory namespace

Use a graph to save or read tenant-scoped preferences through transactional SQLite storage.

## Skills and purpose
This lab teaches **durable namespaced memory and SQL parameters** through an observable execution path. Why is a correctly scoped storage key not a substitute for verifying the requesting tenant?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"tenant": "a", "user": "u", "action": "save", "preference": "brief"}`. Expected fields: `{"stored": "brief", "found": true}`.
2. Input `{"tenant": "b", "user": "u", "action": "load", "preference": "unused"}`. Expected fields: `{"stored": null, "found": false}`.
3. Input `{"tenant": "c", "user": "v", "action": "save", "preference": "detail"}`. Expected fields: `{"stored": "detail"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
