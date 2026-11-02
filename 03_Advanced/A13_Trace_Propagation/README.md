# A13 · Follow execution across spans

Attach a local RunTree hierarchy to a graph and optionally create/read back a redacted LangSmith run.

## Skills and purpose
This lab teaches **RunTree hierarchy and trace privacy** through an observable execution path. Why does a local trace ID not prove that a cloud run was received?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"text": " one   two "}`. Expected fields: `{"answer": "ONE TWO", "spans": 2, "cloud_exported": false}`.
2. Input `{"text": "state"}`. Expected fields: `{"answer": "STATE"}`.
3. Input `{"text": "tools"}`. Expected fields: `{"spans": 2}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. An optional account mode is implemented in run_cloud; cloud access is not required by the local tests.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
