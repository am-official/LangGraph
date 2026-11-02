# Agents and tools
A graph can run deterministic nodes without being an autonomous agent. A model/tool loop adds decisions and protocol messages. AIMessage tool_calls describe requested names, arguments, and IDs; ToolMessage correlates the result by tool_call_id. ToolNode supplies framework execution, and tools_condition routes to tools or completion.

The installed ToolNode requires graph runtime facilities. I13 and I14 run it inside a compiled graph instead of calling it as an isolated function. A scripted assistant fixture exercises the protocol but does not demonstrate model reasoning quality.

A tool schema is not authorization. Validate names, arguments, tenant access, input size, resource use, and allowed side effects. Treat model requests and retrieved instructions as untrusted. Do not expose an unrestricted shell or eval merely because the caller is an agent.

Use a simple chain for fixed steps, an agent for a bounded decision/tool loop, and an explicit graph for durable branching, recovery, or review. Plan execution should validate each step against an allowlist before running it.

**Practice:** B08, I13–I18, A11–A12. Demonstrate an unapproved tool rejection and distinguish tool protocol correctness from task success.
