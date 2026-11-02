# I02 · Map a changing workload

Fan out a dynamic list of values with Send, then reduce the results deterministically.

## Skills and purpose
This lab teaches **dynamic Send fan-out and reduction** through an observable execution path. How would you preserve stable output ordering when task completion order is nondeterministic?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"values": [1, 2, 3]}`. Expected fields: `{"total": 14, "squares": [{"index": 0, "square": 1}, {"index": 1, "square": 4}, {"index": 2, "square": 9}]}`.
2. Input `{"values": [-2, 0]}`. Expected fields: `{"total": 4}`.
3. Input `{"values": [5]}`. Expected fields: `{"total": 25}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
