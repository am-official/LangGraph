# B04 · A pipeline with clear stages

Normalize a document, tokenize it, then compute a word count through three graph nodes.

## Skills and purpose
This lab teaches **explicit sequential dependencies** through an observable execution path. What can go wrong if a consumer runs before the node producing its input?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"document": "one two"}`. Expected fields: `{"words": 2, "tokens": ["one", "two"]}`.
2. Input `{"document": " one   two "}`. Expected fields: `{"normalized": "one two"}`.
3. Input `{"document": "solo"}`. Expected fields: `{"words": 1}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
