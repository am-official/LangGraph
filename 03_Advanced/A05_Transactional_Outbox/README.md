# A05 · Record intent before dispatch

Commit a local outbox item and dispatch it exactly once to a local receipt ledger.

## Skills and purpose
This lab teaches **transactional outbox and idempotent dispatch** through an observable execution path. Why does local exactly-once recording not automatically guarantee exactly-once delivery to an external provider?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"operation": "a", "payload": "one"}`. Expected fields: `{"same_receipt": true, "external_notification_sent": false}`.
2. Input `{"operation": "b", "payload": "two"}`. Expected fields: `{"delivered_to_local_ledger": true}`.
3. Input `{"operation": "c", "payload": "three"}`. Expected fields: `{"same_receipt": true}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
