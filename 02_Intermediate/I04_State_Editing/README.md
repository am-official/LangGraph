# I04 · Edit a saved state

Update an intermediate checkpoint as a named node, then execute the remaining step.

## Skills and purpose
This lab teaches **update_state with as_node** through an observable execution path. Why does the node attribution influence which steps run after a state edit?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": 3, "edited": 20}`. Expected fields: `{"before_edit": 6, "result": 21, "original_snapshot_unchanged": true}`.
2. Input `{"value": 0, "edited": 0}`. Expected fields: `{"result": 1}`.
3. Input `{"value": 8, "edited": 4}`. Expected fields: `{"result": 5}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
