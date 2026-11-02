# B16 · Stop before the node

Persist a static breakpoint, inspect pending work, and continue on the same thread.

## Skills and purpose
This lab teaches **static interrupt_before checkpoints** through an observable execution path. How does resuming a static breakpoint differ from supplying a dynamic interrupt decision?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"thread": "a", "action": "start", "value": 3}`. Expected fields: `{"value": 3, "pending": ["work"]}`.
2. Input `{"thread": "b", "action": "start", "value": 0}`. Expected fields: `{"pending": ["work"]}`.
3. Input `{"thread": "c", "action": "start", "value": 9}`. Expected fields: `{"value": 9}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
