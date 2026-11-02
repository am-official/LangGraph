# B20 · Configuration outside state

Inject a trusted multiplier through Runtime context rather than copying it into mutable graph state.

## Skills and purpose
This lab teaches **Runtime context versus mutable state** through an observable execution path. Why should authorization context come from a trusted caller rather than user-supplied state?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"value": 4, "factor": 3}`. Expected fields: `{"answer": 12, "context_in_state": false}`.
2. Input `{"value": 0, "factor": 5}`. Expected fields: `{"answer": 0}`.
3. Input `{"value": 7, "factor": 2}`. Expected fields: `{"answer": 14}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
