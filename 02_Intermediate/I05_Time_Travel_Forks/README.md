# I05 · Compare two futures

Create two forks from one intermediate checkpoint and compare their outcomes without changing the original snapshot.

## Skills and purpose
This lab teaches **branching from immutable checkpoint history** through an observable execution path. How would you distinguish exploratory forks from the production thread that may perform side effects?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"initial": 2, "branch_a": 10, "branch_b": 30}`. Expected fields: `{"original": 5, "branches": [11, 31], "saved_origin": 4}`.
2. Input `{"initial": 0, "branch_a": 0, "branch_b": 1}`. Expected fields: `{"branches": [1, 2]}`.
3. Input `{"initial": 4, "branch_a": 2, "branch_b": 2}`. Expected fields: `{"branches": [3, 3]}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
