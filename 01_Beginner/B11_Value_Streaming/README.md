# B11 · Read evolving state

Inspect the values stream, including initial state and the snapshots after each update.

## Skills and purpose
This lab teaches **values stream snapshots** through an observable execution path. What does collecting a stream into a list lose compared with rendering events as they arrive?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": 3}`. Expected fields: `{"snapshots": [{"value": 3}, {"value": 6}, {"value": 7}], "snapshot_count": 3}`.
2. Input `{"value": 0}`. Expected fields: `{"final_value": 1}`.
3. Input `{"value": 10}`. Expected fields: `{"final_value": 21}`.

## Scope
The lab inspects collected stream events; it does not claim incremental model-token delivery. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
