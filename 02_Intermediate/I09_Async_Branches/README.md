# I09 · Async work without shared mutation

Run asynchronous graph branches and merge their independent results.

## Skills and purpose
This lab teaches **ainvoke and asynchronous node boundaries** through an observable execution path. Why does async execution not make CPU-bound work automatically faster?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"text": "abc"}`. Expected fields: `{"results": ["reverse:cba", "upper:ABC"]}`.
2. Input `{"text": "one"}`. Expected fields: `{"results": ["reverse:eno", "upper:ONE"]}`.
3. Input `{"text": "ab cd"}`. Expected fields: `{"results": ["reverse:dc ba", "upper:AB CD"]}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
