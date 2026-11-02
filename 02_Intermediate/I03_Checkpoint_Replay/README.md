# I03 · Replay from a known point

Find an intermediate checkpoint and replay the remaining graph steps from its saved configuration.

## Skills and purpose
This lab teaches **checkpoint history and replay configuration** through an observable execution path. Which operations may run again during replay, and why do external effects need idempotency?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": 3}`. Expected fields: `{"original": 7, "checkpoint_value": 6, "replayed": 7}`.
2. Input `{"value": 0}`. Expected fields: `{"replayed": 1}`.
3. Input `{"value": 8}`. Expected fields: `{"checkpoint_value": 16, "replayed": 17}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
