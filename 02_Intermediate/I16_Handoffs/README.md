# I16 · A scoped specialist handoff

Use Command to hand a validated task to a named specialist and keep the handoff reason in state.

## Skills and purpose
This lab teaches **explicit specialist handoffs** through an observable execution path. What context should be transferred to a specialist, and what should remain private?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"request": "refund please"}`. Expected fields: `{"specialist": "billing"}`.
2. Input `{"request": "app crashed"}`. Expected fields: `{"specialist": "technical"}`.
3. Input `{"request": "tool error"}`. Expected fields: `{"reason": "Deterministic request category"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
