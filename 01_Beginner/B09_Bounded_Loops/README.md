# B09 · Repeat with a stopping rule

Execute a graph loop until the count reaches a validated target.

## Skills and purpose
This lab teaches **graph loops and termination** through an observable execution path. Why validate a business stopping condition as well as setting a recursion limit?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"target": 1}`. Expected fields: `{"count": 1}`.
2. Input `{"target": 3}`. Expected fields: `{"count": 3}`.
3. Input `{"target": 20}`. Expected fields: `{"count": 20}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
