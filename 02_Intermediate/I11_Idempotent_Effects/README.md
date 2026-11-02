# I11 · One operation, one receipt

Use a unique operation key and verify repeated graph execution does not duplicate a stored effect.

## Skills and purpose
This lab teaches **idempotency keys and stored receipts** through an observable execution path. How should the system respond when one idempotency key is reused for different input?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"operation": "a", "value": "one"}`. Expected fields: `{"same_receipt": true, "second_created": false}`.
2. Input `{"operation": "b", "value": "two"}`. Expected fields: `{"same_receipt": true}`.
3. Input `{"operation": "c", "value": "three"}`. Expected fields: `{"second_created": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
