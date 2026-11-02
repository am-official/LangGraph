# I12 · An explicit fallback path

Route a failed primary operation to a declared fallback while preserving the failure reason.

## Skills and purpose
This lab teaches **fallback routing without hiding failure** through an observable execution path. When would returning stale fallback guidance be worse than failing the request?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"primary_available": false, "request": "hello"}`. Expected fields: `{"path": "fallback", "error": "Primary unavailable"}`.
2. Input `{"primary_available": true, "request": "hello"}`. Expected fields: `{"path": "primary", "answer": "Primary: hello"}`.
3. Input `{"primary_available": false, "request": "tools"}`. Expected fields: `{"path": "fallback"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
