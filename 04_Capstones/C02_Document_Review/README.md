# C02 · Evidence before publishing

Retrieve a supplied document collection, draft a cited extract, and apply a coverage gate before recording publication eligibility.

## Skills and purpose
This lab teaches **retrieval provenance and publication gating** through an observable execution path. Why does meeting a source-count threshold not prove that a claim is supported?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"question": "tools", "documents": ["Agents use tools."], "minimum_sources": 1}`. Expected fields: `{"eligible": true}`.
2. Input `{"question": "tools", "documents": ["Agents use tools."], "minimum_sources": 2}`. Expected fields: `{"eligible": false}`.
3. Input `{"question": "!!!", "documents": ["Agents use tools."], "minimum_sources": 1}`. Expected fields: `{"eligible": false, "answer": "No evidence found."}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
