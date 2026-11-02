# State and execution
A StateGraph declares computation; compile produces an executable graph. A node receives the current state and returns updates, not a replacement for every field. START and END bound the computation. Sequential edges encode dependency; conditional edges encode policy. Command can combine updates with routing, while Send creates dynamic work items.

Reducers determine how multiple updates merge. List concatenation preserves all contributions, including duplicates; it is not automatically idempotent. An overwrite is useful for one current value but unsafe when parallel writers target the same field. add_messages merges by message identity and supports replacement/removal instead of blind list append.

TypedDict describes state shape to tooling. Validate untrusted values before graph execution using explicit checks or a Pydantic boundary. Runtime context should carry trusted caller configuration that a node should not mutate. Do not derive authorization from arbitrary user-supplied state.

**Practice:** B02–B06, B18–B20, I01–I02, I08. Explain one invariant for each and demonstrate a failure if a required edge, reducer, or validation is removed.
