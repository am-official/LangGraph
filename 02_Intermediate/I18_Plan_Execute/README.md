# I18 · Execute an explicit plan

Validate a plan of allowlisted transformations, execute one step per graph loop, and record progress.

## Skills and purpose
This lab teaches **bounded plan execution** through an observable execution path. Why must a model-produced plan be validated independently before tool execution?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": "abc", "plan": ["upper", "reverse"]}`. Expected fields: `{"value": "CBA", "cursor": 2, "executed": ["upper", "reverse"]}`.
2. Input `{"value": "one", "plan": ["upper"]}`. Expected fields: `{"value": "ONE"}`.
3. Input `{"value": "abc", "plan": ["reverse", "reverse"]}`. Expected fields: `{"value": "abc", "cursor": 2}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
