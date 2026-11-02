# I20 · Test behavior, not topology alone

Evaluate a routing graph against labeled cases and inspect per-example failures.

## Skills and purpose
This lab teaches **behavioral evaluation for graph workflows** through an observable execution path. Which failures can remain invisible if you test only whether a graph compiles?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"cases": [{"request": "refund", "expected": "billing"}]}`. Expected fields: `{"accuracy": 1.0, "failures": 0}`.
2. Input `{"cases": [{"request": "crash", "expected": "billing"}]}`. Expected fields: `{"accuracy": 0.0, "failures": 1}`.
3. Input `{"cases": [{"request": "hello", "expected": "technical"}]}`. Expected fields: `{"accuracy": 1.0}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
