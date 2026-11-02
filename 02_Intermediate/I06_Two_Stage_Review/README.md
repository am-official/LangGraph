# I06 · Two decisions, one policy

Pause twice on separate review nodes and accept only when both decisions approve.

## Skills and purpose
This lab teaches **separate interrupt stages and composite approval** through an observable execution path. When should rejection short-circuit later reviewers rather than collecting all decisions?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"request": "Release", "first": "approve", "second": "approve"}`. Expected fields: `{"approved": true, "observed_pauses": 2}`.
2. Input `{"request": "Release", "first": "approve", "second": "reject"}`. Expected fields: `{"approved": false}`.
3. Input `{"request": "Release", "first": "reject", "second": "approve"}`. Expected fields: `{"approved": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
