# I07 · Memory beyond one thread

Store preferences under separate namespaces with the LangGraph store interface.

## Skills and purpose
This lab teaches **InMemoryStore namespaces** through an observable execution path. What trusted information should determine a namespace in a multi-tenant application?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"tenant": "a", "user": "ada", "preference": "brief"}`. Expected fields: `{"value": "brief", "foreign_namespace_missing": true, "items": 1}`.
2. Input `{"tenant": "b", "user": "lin", "preference": "detailed"}`. Expected fields: `{"value": "detailed"}`.
3. Input `{"tenant": "c", "user": "sam", "preference": "examples"}`. Expected fields: `{"items": 1}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
