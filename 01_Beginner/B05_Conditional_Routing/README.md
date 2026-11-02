# B05 · Route by policy

Choose a billing or technical path using a deterministic routing node.

## Skills and purpose
This lab teaches **conditional edges and routing invariants** through an observable execution path. How do explicit routes differ from an unrestricted model selecting side effects?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"request": "Refund please"}`. Expected fields: `{"route": "billing"}`.
2. Input `{"request": "App crashed"}`. Expected fields: `{"route": "technical"}`.
3. Input `{"request": "Missing invoice"}`. Expected fields: `{"route": "billing"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
