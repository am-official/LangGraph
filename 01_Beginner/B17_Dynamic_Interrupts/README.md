# B17 · Ask before proceeding

Pause with a review payload and resume with an explicit decision, retaining the original request.

## Skills and purpose
This lab teaches **interrupt payload and Command resume** through an observable execution path. Which parts of a node may execute again after resume, and where should side effects be placed?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"thread": "a", "action": "submit", "request": "Draft A"}`. Expected fields: `{"pending": true, "approved": false}`.
2. Input `{"thread": "b", "action": "submit", "request": "Draft B"}`. Expected fields: `{"request": "Draft B"}`.
3. Input `{"thread": "c", "action": "submit", "request": "Draft C"}`. Expected fields: `{"external_effects": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
