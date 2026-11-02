# A07 · A timeout is an outcome

Bound an async operation with wait_for and record a timeout without pretending it succeeded.

## Skills and purpose
This lab teaches **async cancellation and timeout reporting** through an observable execution path. What happens if the underlying library ignores cancellation or performs a side effect before timeout?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"delay_ms": 0, "timeout_ms": 50}`. Expected fields: `{"status": "success"}`.
2. Input `{"delay_ms": 30, "timeout_ms": 2}`. Expected fields: `{"status": "timeout"}`.
3. Input `{"delay_ms": 0, "timeout_ms": 20}`. Expected fields: `{"answer": "Operation completed."}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
