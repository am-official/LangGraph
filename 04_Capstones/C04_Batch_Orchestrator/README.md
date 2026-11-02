# C04 · A recoverable batch pipeline

Validate a batch, transform each item through Send, and persist a content-addressed result for replay-safe reuse.

## Skills and purpose
This lab teaches **dynamic batch work and idempotent results** through an observable execution path. How would you coordinate two workers racing to create the same job ID?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"job": "a", "values": ["one", "two"]}`. Expected fields: `{"answer": ["ONE", "TWO"], "reused": false}`.
2. Input `{"job": "b", "values": ["solo"]}`. Expected fields: `{"answer": ["SOLO"]}`.
3. Input `{"job": "c", "values": ["a", "a"]}`. Expected fields: `{"answer": ["A", "A"]}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
