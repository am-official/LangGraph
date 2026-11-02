# I13 · A visible tool-call protocol

Create a model-style tool call, execute it with ToolNode, and route back to a response node.

## Skills and purpose
This lab teaches **ToolNode and tools_condition loop** through an observable execution path. Which part is deterministic protocol scaffolding here, and what would a live model add?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"text": "one two"}`. Expected fields: `{"answer": "Word count: 2", "tool_messages": 1}`.
2. Input `{"text": "one"}`. Expected fields: `{"answer": "Word count: 1"}`.
3. Input `{"text": "a b c"}`. Expected fields: `{"answer": "Word count: 3"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
