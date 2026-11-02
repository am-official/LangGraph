# B18 · Update and route together

Use Command to update the route field and choose the next graph node.

## Skills and purpose
This lab teaches **Command update and goto** through an observable execution path. Why should destination names and return annotations agree?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"message": "hello"}`. Expected fields: `{"route": "short"}`.
2. Input `{"message": "This request has more than twenty characters."}`. Expected fields: `{"route": "long"}`.
3. Input `{"message": "12345678901234567890"}`. Expected fields: `{"route": "short"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
