# A19 · Evaluate before release

Use a labeled dataset and an explicit quality threshold to gate a local candidate release.

## Skills and purpose
This lab teaches **dataset-driven release gates** through an observable execution path. Why must a release gate account for dataset coverage as well as an aggregate pass rate?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"cases": [{"input": "a", "reference": "A"}], "threshold": 1.0}`. Expected fields: `{"score": 1.0, "released": true}`.
2. Input `{"cases": [{"input": "a", "reference": "wrong"}], "threshold": 0.9}`. Expected fields: `{"score": 0.0, "released": false}`.
3. Input `{"cases": [{"input": "a", "reference": "A"}, {"input": "b", "reference": "wrong"}], "threshold": 0.5}`. Expected fields: `{"score": 0.5, "released": true}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
