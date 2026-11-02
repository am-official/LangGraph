# I15 · Edit without duplicating turns

Use message IDs to replace one turn and remove another while retaining reducer semantics.

## Skills and purpose
This lab teaches **message replacement and RemoveMessage** through an observable execution path. Why can blind list concatenation duplicate edited assistant turns?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"original": "draft", "replacement": "final"}`. Expected fields: `{"revised_count": 2, "replaced_content": "final", "remaining_ids": ["reply"], "remaining_count": 1}`.
2. Input `{"original": "a", "replacement": "b"}`. Expected fields: `{"replaced_content": "b"}`.
3. Input `{"original": "old", "replacement": "new"}`. Expected fields: `{"remaining_count": 1}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
