# A09 · Stop an overlong graph

Compare successful termination with GraphRecursionError when a graph exceeds its configured step budget.

## Skills and purpose
This lab teaches **GraphRecursionError as a resource guard** through an observable execution path. Why does a graph step limit not replace a wall-clock timeout, token budget, or tool authorization?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"target": 2, "budget": 10}`. Expected fields: `{"status": "completed", "executed_steps": 2}`.
2. Input `{"target": 10, "budget": 3}`. Expected fields: `{"status": "budget_exhausted"}`.
3. Input `{"target": 1, "budget": 5}`. Expected fields: `{"status": "completed"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
