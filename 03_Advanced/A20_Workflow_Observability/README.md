# A20 · Measure every stage

Instrument a graph with stage events, errors, and wall-clock durations without logging input content.

## Skills and purpose
This lab teaches **node-level observability and privacy** through an observable execution path. Why should monitoring distinguish the primary failure, fallback behavior, and final user-visible outcome?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"text": "one", "inject_failure": false}`. Expected fields: `{"status": "success", "answer": "ONE"}`.
2. Input `{"text": "two", "inject_failure": true}`. Expected fields: `{"status": "error", "answer": null}`.
3. Input `{"text": "three", "inject_failure": false}`. Expected fields: `{"sensitive_input_logged": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
