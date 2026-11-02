# I14 · Validate before invoking tools

Reject unapproved names and malformed arguments before a real ToolNode sees a request.

## Skills and purpose
This lab teaches **tool allowlists and argument validation** through an observable execution path. Why should tool selection and tool authorization be separate checks?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"tool_name": "count_words", "content": "a b"}`. Expected fields: `{"word_count": 2, "validated": true}`.
2. Input `{"tool_name": "count_words", "content": "a"}`. Expected fields: `{"tool_call_id": "validated-1"}`.
3. Input `{"tool_name": "count_words", "content": "a b c"}`. Expected fields: `{"word_count": 3}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
