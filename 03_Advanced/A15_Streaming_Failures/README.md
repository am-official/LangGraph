# A15 · Preserve partial evidence on failure

Capture successful stream updates before a later node fails, without returning a fabricated final answer.

## Skills and purpose
This lab teaches **partial stream evidence and explicit failure** through an observable execution path. How should a client distinguish partial updates from a completed response?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"fail": true, "value": "one"}`. Expected fields: `{"status": "failed", "events": [{"prepare": {"prepared": "ONE"}}]}`.
2. Input `{"fail": false, "value": "two"}`. Expected fields: `{"status": "success", "error": null}`.
3. Input `{"fail": true, "value": "three"}`. Expected fields: `{"has_partial_evidence": true}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
