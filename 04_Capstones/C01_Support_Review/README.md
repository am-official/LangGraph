# C01 · Support with a review boundary

Route support requests, pause financial work for approval, and keep a durable thread history.

## Skills and purpose
This lab teaches **durable support routing and review** through an observable execution path. What additional identity and payment-system controls are required before any real financial action?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"thread": "a", "request": "refund please", "action": "submit"}`. Expected fields: `{"route": "review", "pending": true, "financial_transaction_executed": false}`.
2. Input `{"thread": "b", "request": "app crashes", "action": "submit"}`. Expected fields: `{"route": "technical", "pending": false}`.
3. Input `{"thread": "c", "request": "refund order", "action": "submit"}`. Expected fields: `{"approved": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
