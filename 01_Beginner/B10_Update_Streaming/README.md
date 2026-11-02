# B10 · Read node updates

Inspect the updates stream as each graph node returns a state delta.

## Skills and purpose
This lab teaches **updates stream deltas** through an observable execution path. How do node updates differ from snapshots of the entire state?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": 3}`. Expected fields: `{"events": [{"double": {"value": 6}}, {"offset": {"value": 7}}], "answer": "7"}`.
2. Input `{"value": 0}`. Expected fields: `{"answer": "1", "event_count": 2}`.
3. Input `{"value": 10}`. Expected fields: `{"answer": "21"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
