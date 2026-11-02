# I19 · Keep a bounded context

Select recent messages within a character budget and keep a trusted policy outside history.

## Skills and purpose
This lab teaches **bounded context and role boundaries** through an observable execution path. When does truncation require requesting shorter input rather than claiming the context was summarized?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"messages": [{"role": "user", "content": "hello"}], "budget": 10}`. Expected fields: `{"used_characters": 5, "dropped": 0}`.
2. Input `{"messages": [{"role": "user", "content": "xxxxxxxxxxxxxxxxxxxx"}], "budget": 10}`. Expected fields: `{"messages": [], "dropped": 1}`.
3. Input `{"messages": [{"role": "assistant", "content": "orphan"}, {"role": "user", "content": "hi"}], "budget": 20}`. Expected fields: `{"messages": [{"role": "user", "content": "hi"}]}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
