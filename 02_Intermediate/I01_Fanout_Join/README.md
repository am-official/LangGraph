# I01 · Two branches, one result

Run independent analysis branches with a reducer and join before composing the result.

## Skills and purpose
This lab teaches **parallel branches and explicit join** through an observable execution path. Why is a reducer necessary for concurrent findings updates?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"document": "one two"}`. Expected fields: `{"answer": "characters=7, words=2", "branches": 2}`.
2. Input `{"document": "solo"}`. Expected fields: `{"branches": 2}`.
3. Input `{"document": "a b c"}`. Expected fields: `{"answer": "characters=5, words=3"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
