# B08 · A bounded tool node

Run an allowlisted word-count tool inside an explicit graph, without executing supplied source code.

## Skills and purpose
This lab teaches **tool schemas and controlled graph execution** through an observable execution path. Does wrapping a function as a tool provide authorization or resource isolation by itself?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"text": "one two"}`. Expected fields: `{"words": 2}`.
2. Input `{"text": "single"}`. Expected fields: `{"words": 1}`.
3. Input `{"text": "a b c"}`. Expected fields: `{"words": 3}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
