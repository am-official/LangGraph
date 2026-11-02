# A16 · A functional workflow

Use LangGraph entrypoint and task decorators to express a checkpoint-capable functional workflow.

## Skills and purpose
This lab teaches **functional entrypoint and task boundaries** through an observable execution path. When is a functional API clearer than an explicitly declared StateGraph?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": 4}`. Expected fields: `{"result": 9}`.
2. Input `{"value": 0}`. Expected fields: `{"result": 1}`.
3. Input `{"value": 10}`. Expected fields: `{"result": 21}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
