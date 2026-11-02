# I10 · Retry the right failure

Inject transient failures and let a bounded graph RetryPolicy recover.

## Skills and purpose
This lab teaches **RetryPolicy and transient errors** through an observable execution path. Why can retries duplicate an external side effect even if the final graph state looks correct?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"failures": 0, "value": "one"}`. Expected fields: `{"attempts": 1, "answer": "ONE"}`.
2. Input `{"failures": 1, "value": "two"}`. Expected fields: `{"attempts": 2}`.
3. Input `{"failures": 2, "value": "three"}`. Expected fields: `{"attempts": 3}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
