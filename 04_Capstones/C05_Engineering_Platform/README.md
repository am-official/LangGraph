# C05 · An observable release workflow

Combine graph execution, labeled evaluation, a release gate, and a durable decision ledger.

## Skills and purpose
This lab teaches **end-to-end evaluation and release observability** through an observable execution path. How would you expand this gate to cover quality, safety, latency, and deployment rollback separately?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"cases": [{"input": "a", "reference": "A"}], "threshold": 1.0}`. Expected fields: `{"score": 1.0, "released": true, "events": ["evaluated", "gated"]}`.
2. Input `{"cases": [{"input": "a", "reference": "wrong"}], "threshold": 0.9}`. Expected fields: `{"released": false}`.
3. Input `{"cases": [{"input": "a", "reference": "A"}, {"input": "b", "reference": "wrong"}], "threshold": 0.9}`. Expected fields: `{"score": 0.5, "released": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
