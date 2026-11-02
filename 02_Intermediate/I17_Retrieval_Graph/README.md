# I17 · Ground the response

Retrieve lexical evidence in one node, then compose a cited extractive response or abstain.

## Skills and purpose
This lab teaches **retrieval, provenance, and abstention** through an observable execution path. Why do source relevance, factual truth, and generated-answer correctness require different evaluation?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"question": "tools", "documents": ["Agents use tools."]}`. Expected fields: `{"sources": ["doc-1"], "answer": "[doc-1] Agents use tools."}`.
2. Input `{"question": "!!!", "documents": ["Agents use tools."]}`. Expected fields: `{"sources": [], "answer": "No matching evidence. I do not know."}`.
3. Input `{"question": "state", "documents": ["Tools execute.", "Graphs preserve state."]}`. Expected fields: `{"sources": ["doc-2"]}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
