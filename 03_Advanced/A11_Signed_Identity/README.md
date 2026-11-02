# A11 · Authenticate before authorizing

Verify a signed token and enforce tenant/role policy before executing a graph node.

## Skills and purpose
This lab teaches **authentication versus authorization** through an observable execution path. How can a valid identity still lack permission for a resource?

Start with [INSTRUCTIONS](INSTRUCTIONS.md), inspect [EXPLANATION](EXPLANATION.md), then complete [EXERCISES](EXERCISES.md) and [INTERVIEW](INTERVIEW.md). Source, dependencies, data, and tests are contained in this folder; it does not import another lab.

## Acceptance examples
1. Input `{"role": "viewer", "operation": "read", "resource_tenant": "team-a"}`. Expected fields: `{"authorized": true}`.
2. Input `{"role": "viewer", "operation": "write", "resource_tenant": "team-a"}`. Expected fields: `{"authorized": false}`.
3. Input `{"role": "editor", "operation": "write", "resource_tenant": "team-b"}`. Expected fields: `{"authorized": false}`.

## Scope
Local deterministic workflow; model intelligence and managed deployment are separate concerns. The default path runs without any service account.

See [TROUBLESHOOTING](TROUBLESHOOTING.md) for input, persistence, and environment failures. Never commit secrets or real customer data.
