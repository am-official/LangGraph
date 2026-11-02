# A01 · A job that resumes

Persist work between graph steps and advance a batch one unit at a time.

## Skills and purpose
This lab teaches **durable stepwise execution** through an observable execution path. How do stable job IDs and replay-safe units make restart recovery possible?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"job": "a", "action": "start", "work": ["one", "two"]}`. Expected fields: `{"cursor": 0, "pending": true}`.
2. Input `{"job": "b", "action": "start", "work": ["one"]}`. Expected fields: `{"completed": []}`.
3. Input `{"job": "c", "action": "start", "work": ["a", "b", "c"]}`. Expected fields: `{"cursor": 0}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
