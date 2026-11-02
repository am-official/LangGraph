# A18 · Verify what you saved

Write an artifact through a graph node, record its SHA-256 digest, and verify the bytes after reopening.

## Skills and purpose
This lab teaches **content hashes and artifact provenance** through an observable execution path. Why does a matching digest establish byte integrity but not source authenticity or semantic truth?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"content": "one"}`. Expected fields: `{"verified": true}`.
2. Input `{"content": "two"}`. Expected fields: `{"verified": true}`.
3. Input `{"content": "你好"}`. Expected fields: `{"verified": true}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
