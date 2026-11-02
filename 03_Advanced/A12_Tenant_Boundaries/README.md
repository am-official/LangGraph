# A12 · Filter before exposing data

Select authorized tenant records before retrieval and ensure foreign records never reach a graph node.

## Skills and purpose
This lab teaches **pre-execution tenant filtering** through an observable execution path. Why is filtering model output too late if unauthorized data was already sent to the model?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"tenant": "team-a", "records": [{"tenant": "team-a", "text": "allowed"}, {"tenant": "team-b", "text": "secret"}]}`. Expected fields: `{"documents": ["allowed"], "answer": "allowed"}`.
2. Input `{"tenant": "team-b", "records": [{"tenant": "team-a", "text": "secret"}]}`. Expected fields: `{"documents": []}`.
3. Input `{"tenant": "team-b", "records": [{"tenant": "team-b", "text": "own"}]}`. Expected fields: `{"answer": "own"}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
