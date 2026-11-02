# B06 · Merge updates deliberately

Append findings with a list reducer and compare the result with overwrite semantics.

## Skills and purpose
This lab teaches **Annotated reducers and accumulation** through an observable execution path. When should repeated updates append, replace, deduplicate, or reject?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"seed": "a", "finding": "b"}`. Expected fields: `{"findings": ["a", "b"], "count": 2}`.
2. Input `{"seed": "same", "finding": "same"}`. Expected fields: `{"findings": ["same", "same"]}`.
3. Input `{"seed": "first", "finding": "last"}`. Expected fields: `{"count": 2}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
