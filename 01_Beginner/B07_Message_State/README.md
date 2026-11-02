# B07 · Messages with identity

Use add_messages to preserve role and message identity through a graph.

## Skills and purpose
This lab teaches **add_messages and message roles** through an observable execution path. Why does message identity matter when editing conversation state?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"message": "hello"}`. Expected fields: `{"count": 2}`.
2. Input `{"message": "tools?"}`. Expected fields: `{"messages": [{"id": "question", "role": "human", "content": "tools?"}, {"id": "reply", "role": "ai", "content": "Local response: tools?"}]}`.
3. Input `{"message": "state?"}`. Expected fields: `{"count": 2}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
