# B02 · A state contract

Inspect declared fields and observe which state values a node updates.

## Skills and purpose
This lab teaches **typed state versus runtime validation** through an observable execution path. TypedDict documents a contract but does not validate every value at runtime. Where should validation occur?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"quantity": 3, "price": 4.5}`. Expected fields: `{"total": 13.5}`.
2. Input `{"quantity": 1, "price": 0}`. Expected fields: `{"total": 0.0}`.
3. Input `{"quantity": 2, "price": 1.25}`. Expected fields: `{"quantity": 2, "price": 1.25, "total": 2.5}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
