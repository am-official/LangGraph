# A14 · Stop before spending the budget

Account for declared per-step costs and terminate before a planned step would exceed the cap.

## Skills and purpose
This lab teaches **pre-step budget enforcement** through an observable execution path. How would you reconcile estimated cost with actual billed token usage?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"step_costs": [0.01, 0.02, 0.04], "budget": 0.04}`. Expected fields: `{"spent": 0.03, "cursor": 2, "status": "budget_blocked"}`.
2. Input `{"step_costs": [0.01, 0.02], "budget": 0.03}`. Expected fields: `{"status": "complete", "spent": 0.03}`.
3. Input `{"step_costs": [0.01], "budget": 0}`. Expected fields: `{"cursor": 0, "spent": 0.0}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
