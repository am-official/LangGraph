# C03 · A research and critique team

Run separate evidence and critique branches, join their findings, and preserve uncertainty in the final brief.

## Skills and purpose
This lab teaches **parallel specialist evidence and critique** through an observable execution path. Why should the synthesizer preserve the critic’s uncertainty rather than smoothing it away?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"question": "tools", "documents": ["Agents use tools."]}`. Expected fields: `{"specialists": 2}`.
2. Input `{"question": "!!!", "documents": ["Agents use tools."]}`. Expected fields: `{"specialists": 2}`.
3. Input `{"question": "state", "documents": ["Graphs preserve state."]}`. Expected fields: `{"specialists": 2}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
