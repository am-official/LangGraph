# A06 · Approval needs permission

Require an eligible reviewer role before resuming a protected graph interrupt.

## Skills and purpose
This lab teaches **authorization before interrupt resume** through an observable execution path. Why is an approve button insufficient without server-side identity and resource authorization?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"request": "Publish", "reviewer_role": "viewer", "decision": "approve"}`. Expected fields: `{"authorized": false, "approved": false, "pending": true}`.
2. Input `{"request": "Publish", "reviewer_role": "reviewer", "decision": "approve"}`. Expected fields: `{"authorized": true, "approved": true}`.
3. Input `{"request": "Publish", "reviewer_role": "reviewer", "decision": "reject"}`. Expected fields: `{"approved": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
