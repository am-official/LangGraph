# LangGraph interview preparation
## A five-round practice session
1. **Mechanism, 10 minutes:** choose a beginner lab. Sketch its data flow, run a sample, and explain each output field without reading notes.
2. **Debugging, 15 minutes:** choose an intermediate failure test. Predict what breaks if a validation, reducer, or reference boundary is removed. Demonstrate the failing behavior in a temporary copy.
3. **Architecture, 20 minutes:** choose an advanced tradeoff below. Discuss identity, durability, concurrency, cost, and monitoring only where relevant to that design. State an invariant and how to test it.
4. **Coding, 30 minutes:** implement one EXERCISES.md extension with an acceptance and failure test. Explain complexity and the operational limit.
5. **Evidence review, 10 minutes:** separate local results, mocked/fixture contracts, live acknowledgements, and production behavior. Avoid unsupported claims.

Score each dimension 0–2 using the portal. Revisit a lab when you cannot explain a result or its failure model. For code review, prioritize a meaningful invariant over test counts alone.

## Topic-by-topic questions
### B01 · Your first graph
**Mechanism:** StateGraph compilation and invocation.

**Discussion:** Why is graph construction separate from graph execution?

[Answer guidance and follow-ups](../01_Beginner/B01_Hello_Graph/INTERVIEW.md)

### B02 · A state contract
**Mechanism:** typed state versus runtime validation.

**Discussion:** TypedDict documents a contract but does not validate every value at runtime. Where should validation occur?

[Answer guidance and follow-ups](../01_Beginner/B02_Typed_State/INTERVIEW.md)

### B03 · Update only what changes
**Mechanism:** partial node state updates.

**Discussion:** Why return only changed fields instead of rebuilding all state in every node?

[Answer guidance and follow-ups](../01_Beginner/B03_Partial_Updates/INTERVIEW.md)

### B04 · A pipeline with clear stages
**Mechanism:** explicit sequential dependencies.

**Discussion:** What can go wrong if a consumer runs before the node producing its input?

[Answer guidance and follow-ups](../01_Beginner/B04_Sequential_Nodes/INTERVIEW.md)

### B05 · Route by policy
**Mechanism:** conditional edges and routing invariants.

**Discussion:** How do explicit routes differ from an unrestricted model selecting side effects?

[Answer guidance and follow-ups](../01_Beginner/B05_Conditional_Routing/INTERVIEW.md)

### B06 · Merge updates deliberately
**Mechanism:** Annotated reducers and accumulation.

**Discussion:** When should repeated updates append, replace, deduplicate, or reject?

[Answer guidance and follow-ups](../01_Beginner/B06_Reducers/INTERVIEW.md)

### B07 · Messages with identity
**Mechanism:** add_messages and message roles.

**Discussion:** Why does message identity matter when editing conversation state?

[Answer guidance and follow-ups](../01_Beginner/B07_Message_State/INTERVIEW.md)

### B08 · A bounded tool node
**Mechanism:** tool schemas and controlled graph execution.

**Discussion:** Does wrapping a function as a tool provide authorization or resource isolation by itself?

[Answer guidance and follow-ups](../01_Beginner/B08_Tools_As_Nodes/INTERVIEW.md)

### B09 · Repeat with a stopping rule
**Mechanism:** graph loops and termination.

**Discussion:** Why validate a business stopping condition as well as setting a recursion limit?

[Answer guidance and follow-ups](../01_Beginner/B09_Bounded_Loops/INTERVIEW.md)

### B10 · Read node updates
**Mechanism:** updates stream deltas.

**Discussion:** How do node updates differ from snapshots of the entire state?

[Answer guidance and follow-ups](../01_Beginner/B10_Update_Streaming/INTERVIEW.md)

### B11 · Read evolving state
**Mechanism:** values stream snapshots.

**Discussion:** What does collecting a stream into a list lose compared with rendering events as they arrive?

[Answer guidance and follow-ups](../01_Beginner/B11_Value_Streaming/INTERVIEW.md)

### B12 · Architecture you can inspect
**Mechanism:** compiled graph inspection.

**Discussion:** Why is a graph diagram evidence of structure but not evidence of successful deployment?

[Answer guidance and follow-ups](../01_Beginner/B12_Graph_Visualization/INTERVIEW.md)

### B13 · The last state is available
**Mechanism:** checkpointer and thread configuration.

**Discussion:** What failure destroys an in-memory checkpoint even when a thread ID is stable?

[Answer guidance and follow-ups](../01_Beginner/B13_Memory_Checkpoints/INTERVIEW.md)

### B14 · Two threads, separate histories
**Mechanism:** thread-scoped checkpoint lookup.

**Discussion:** Why is a thread ID an address for state rather than proof of authorization?

[Answer guidance and follow-ups](../01_Beginner/B14_Thread_Isolation/INTERVIEW.md)

### B15 · Checkpoints on disk
**Mechanism:** SQLite checkpoint durability.

**Discussion:** Which failures can one local SQLite file survive, and which need backups or replication?

[Answer guidance and follow-ups](../01_Beginner/B15_SQLite_Checkpoints/INTERVIEW.md)

### B16 · Stop before the node
**Mechanism:** static interrupt_before checkpoints.

**Discussion:** How does resuming a static breakpoint differ from supplying a dynamic interrupt decision?

[Answer guidance and follow-ups](../01_Beginner/B16_Static_Breakpoints/INTERVIEW.md)

### B17 · Ask before proceeding
**Mechanism:** interrupt payload and Command resume.

**Discussion:** Which parts of a node may execute again after resume, and where should side effects be placed?

[Answer guidance and follow-ups](../01_Beginner/B17_Dynamic_Interrupts/INTERVIEW.md)

### B18 · Update and route together
**Mechanism:** Command update and goto.

**Discussion:** Why should destination names and return annotations agree?

[Answer guidance and follow-ups](../01_Beginner/B18_Command_Routing/INTERVIEW.md)

### B19 · A graph inside a graph
**Mechanism:** compiled subgraph composition.

**Discussion:** When should child and parent share a state schema, and when is an adapter preferable?

[Answer guidance and follow-ups](../01_Beginner/B19_Subgraphs/INTERVIEW.md)

### B20 · Configuration outside state
**Mechanism:** Runtime context versus mutable state.

**Discussion:** Why should authorization context come from a trusted caller rather than user-supplied state?

[Answer guidance and follow-ups](../01_Beginner/B20_Runtime_Context/INTERVIEW.md)

### I01 · Two branches, one result
**Mechanism:** parallel branches and explicit join.

**Discussion:** Why is a reducer necessary for concurrent findings updates?

[Answer guidance and follow-ups](../02_Intermediate/I01_Fanout_Join/INTERVIEW.md)

### I02 · Map a changing workload
**Mechanism:** dynamic Send fan-out and reduction.

**Discussion:** How would you preserve stable output ordering when task completion order is nondeterministic?

[Answer guidance and follow-ups](../02_Intermediate/I02_Send_Map_Reduce/INTERVIEW.md)

### I03 · Replay from a known point
**Mechanism:** checkpoint history and replay configuration.

**Discussion:** Which operations may run again during replay, and why do external effects need idempotency?

[Answer guidance and follow-ups](../02_Intermediate/I03_Checkpoint_Replay/INTERVIEW.md)

### I04 · Edit a saved state
**Mechanism:** update_state with as_node.

**Discussion:** Why does the node attribution influence which steps run after a state edit?

[Answer guidance and follow-ups](../02_Intermediate/I04_State_Editing/INTERVIEW.md)

### I05 · Compare two futures
**Mechanism:** branching from immutable checkpoint history.

**Discussion:** How would you distinguish exploratory forks from the production thread that may perform side effects?

[Answer guidance and follow-ups](../02_Intermediate/I05_Time_Travel_Forks/INTERVIEW.md)

### I06 · Two decisions, one policy
**Mechanism:** separate interrupt stages and composite approval.

**Discussion:** When should rejection short-circuit later reviewers rather than collecting all decisions?

[Answer guidance and follow-ups](../02_Intermediate/I06_Two_Stage_Review/INTERVIEW.md)

### I07 · Memory beyond one thread
**Mechanism:** InMemoryStore namespaces.

**Discussion:** What trusted information should determine a namespace in a multi-tenant application?

[Answer guidance and follow-ups](../02_Intermediate/I07_Namespaced_Store/INTERVIEW.md)

### I08 · Validate before orchestration
**Mechanism:** Pydantic validation at the graph boundary.

**Discussion:** Why is a TypedDict annotation insufficient for hostile external input?

[Answer guidance and follow-ups](../02_Intermediate/I08_Validated_State/INTERVIEW.md)

### I09 · Async work without shared mutation
**Mechanism:** ainvoke and asynchronous node boundaries.

**Discussion:** Why does async execution not make CPU-bound work automatically faster?

[Answer guidance and follow-ups](../02_Intermediate/I09_Async_Branches/INTERVIEW.md)

### I10 · Retry the right failure
**Mechanism:** RetryPolicy and transient errors.

**Discussion:** Why can retries duplicate an external side effect even if the final graph state looks correct?

[Answer guidance and follow-ups](../02_Intermediate/I10_Retry_Policy/INTERVIEW.md)

### I11 · One operation, one receipt
**Mechanism:** idempotency keys and stored receipts.

**Discussion:** How should the system respond when one idempotency key is reused for different input?

[Answer guidance and follow-ups](../02_Intermediate/I11_Idempotent_Effects/INTERVIEW.md)

### I12 · An explicit fallback path
**Mechanism:** fallback routing without hiding failure.

**Discussion:** When would returning stale fallback guidance be worse than failing the request?

[Answer guidance and follow-ups](../02_Intermediate/I12_Failure_Fallback/INTERVIEW.md)

### I13 · A visible tool-call protocol
**Mechanism:** ToolNode and tools_condition loop.

**Discussion:** Which part is deterministic protocol scaffolding here, and what would a live model add?

[Answer guidance and follow-ups](../02_Intermediate/I13_Tool_Call_Graph/INTERVIEW.md)

### I14 · Validate before invoking tools
**Mechanism:** tool allowlists and argument validation.

**Discussion:** Why should tool selection and tool authorization be separate checks?

[Answer guidance and follow-ups](../02_Intermediate/I14_Tool_Validation/INTERVIEW.md)

### I15 · Edit without duplicating turns
**Mechanism:** message replacement and RemoveMessage.

**Discussion:** Why can blind list concatenation duplicate edited assistant turns?

[Answer guidance and follow-ups](../02_Intermediate/I15_Message_Replacement/INTERVIEW.md)

### I16 · A scoped specialist handoff
**Mechanism:** explicit specialist handoffs.

**Discussion:** What context should be transferred to a specialist, and what should remain private?

[Answer guidance and follow-ups](../02_Intermediate/I16_Handoffs/INTERVIEW.md)

### I17 · Ground the response
**Mechanism:** retrieval, provenance, and abstention.

**Discussion:** Why do source relevance, factual truth, and generated-answer correctness require different evaluation?

[Answer guidance and follow-ups](../02_Intermediate/I17_Retrieval_Graph/INTERVIEW.md)

### I18 · Execute an explicit plan
**Mechanism:** bounded plan execution.

**Discussion:** Why must a model-produced plan be validated independently before tool execution?

[Answer guidance and follow-ups](../02_Intermediate/I18_Plan_Execute/INTERVIEW.md)

### I19 · Keep a bounded context
**Mechanism:** bounded context and role boundaries.

**Discussion:** When does truncation require requesting shorter input rather than claiming the context was summarized?

[Answer guidance and follow-ups](../02_Intermediate/I19_Context_Compaction/INTERVIEW.md)

### I20 · Test behavior, not topology alone
**Mechanism:** behavioral evaluation for graph workflows.

**Discussion:** Which failures can remain invisible if you test only whether a graph compiles?

[Answer guidance and follow-ups](../02_Intermediate/I20_Graph_Evaluation/INTERVIEW.md)

### A01 · A job that resumes
**Mechanism:** durable stepwise execution.

**Discussion:** How do stable job IDs and replay-safe units make restart recovery possible?

[Answer guidance and follow-ups](../03_Advanced/A01_Durable_Jobs/INTERVIEW.md)

### A02 · Evolve persisted application state
**Mechanism:** versioned payload migration.

**Discussion:** Why must application-state migration be distinguished from serializer and dependency compatibility?

[Answer guidance and follow-ups](../03_Advanced/A02_Payload_Migration/INTERVIEW.md)

### A03 · A durable memory namespace
**Mechanism:** durable namespaced memory and SQL parameters.

**Discussion:** Why is a correctly scoped storage key not a substitute for verifying the requesting tenant?

[Answer guidance and follow-ups](../03_Advanced/A03_Durable_Preferences/INTERVIEW.md)

### A04 · Reject a lost update
**Mechanism:** optimistic version checks.

**Discussion:** When should a client retry automatically, and when must it reconcile the conflicting edit?

[Answer guidance and follow-ups](../03_Advanced/A04_Optimistic_Concurrency/INTERVIEW.md)

### A05 · Record intent before dispatch
**Mechanism:** transactional outbox and idempotent dispatch.

**Discussion:** Why does local exactly-once recording not automatically guarantee exactly-once delivery to an external provider?

[Answer guidance and follow-ups](../03_Advanced/A05_Transactional_Outbox/INTERVIEW.md)

### A06 · Approval needs permission
**Mechanism:** authorization before interrupt resume.

**Discussion:** Why is an approve button insufficient without server-side identity and resource authorization?

[Answer guidance and follow-ups](../03_Advanced/A06_Authorized_Review/INTERVIEW.md)

### A07 · A timeout is an outcome
**Mechanism:** async cancellation and timeout reporting.

**Discussion:** What happens if the underlying library ignores cancellation or performs a side effect before timeout?

[Answer guidance and follow-ups](../03_Advanced/A07_Async_Timeouts/INTERVIEW.md)

### A08 · Cache the right state
**Mechanism:** CachePolicy and pure-node input keys.

**Discussion:** What authorization or freshness bug appears when a tenant or data version is omitted from a cache key?

[Answer guidance and follow-ups](../03_Advanced/A08_Node_Caching/INTERVIEW.md)

### A09 · Stop an overlong graph
**Mechanism:** GraphRecursionError as a resource guard.

**Discussion:** Why does a graph step limit not replace a wall-clock timeout, token budget, or tool authorization?

[Answer guidance and follow-ups](../03_Advanced/A09_Recursion_Budgets/INTERVIEW.md)

### A10 · An exportable graph
**Mechanism:** graph exports and functional HTTP validation.

**Discussion:** Why does a manifest or a listening port not establish a working managed deployment?

[Answer guidance and follow-ups](../03_Advanced/A10_Graph_Serving/INTERVIEW.md)

### A11 · Authenticate before authorizing
**Mechanism:** authentication versus authorization.

**Discussion:** How can a valid identity still lack permission for a resource?

[Answer guidance and follow-ups](../03_Advanced/A11_Signed_Identity/INTERVIEW.md)

### A12 · Filter before exposing data
**Mechanism:** pre-execution tenant filtering.

**Discussion:** Why is filtering model output too late if unauthorized data was already sent to the model?

[Answer guidance and follow-ups](../03_Advanced/A12_Tenant_Boundaries/INTERVIEW.md)

### A13 · Follow execution across spans
**Mechanism:** RunTree hierarchy and trace privacy.

**Discussion:** Why does a local trace ID not prove that a cloud run was received?

[Answer guidance and follow-ups](../03_Advanced/A13_Trace_Propagation/INTERVIEW.md)

### A14 · Stop before spending the budget
**Mechanism:** pre-step budget enforcement.

**Discussion:** How would you reconcile estimated cost with actual billed token usage?

[Answer guidance and follow-ups](../03_Advanced/A14_Cost_Budgets/INTERVIEW.md)

### A15 · Preserve partial evidence on failure
**Mechanism:** partial stream evidence and explicit failure.

**Discussion:** How should a client distinguish partial updates from a completed response?

[Answer guidance and follow-ups](../03_Advanced/A15_Streaming_Failures/INTERVIEW.md)

### A16 · A functional workflow
**Mechanism:** functional entrypoint and task boundaries.

**Discussion:** When is a functional API clearer than an explicitly declared StateGraph?

[Answer guidance and follow-ups](../03_Advanced/A16_Functional_API/INTERVIEW.md)

### A17 · Reusable specialist graphs
**Mechanism:** specialist subgraph contracts.

**Discussion:** What coupling appears when all specialist graphs share one large state schema?

[Answer guidance and follow-ups](../03_Advanced/A17_Specialist_Subgraphs/INTERVIEW.md)

### A18 · Verify what you saved
**Mechanism:** content hashes and artifact provenance.

**Discussion:** Why does a matching digest establish byte integrity but not source authenticity or semantic truth?

[Answer guidance and follow-ups](../03_Advanced/A18_Artifact_Integrity/INTERVIEW.md)

### A19 · Evaluate before release
**Mechanism:** dataset-driven release gates.

**Discussion:** Why must a release gate account for dataset coverage as well as an aggregate pass rate?

[Answer guidance and follow-ups](../03_Advanced/A19_Release_Gates/INTERVIEW.md)

### A20 · Measure every stage
**Mechanism:** node-level observability and privacy.

**Discussion:** Why should monitoring distinguish the primary failure, fallback behavior, and final user-visible outcome?

[Answer guidance and follow-ups](../03_Advanced/A20_Workflow_Observability/INTERVIEW.md)

### C01 · Support with a review boundary
**Mechanism:** durable support routing and review.

**Discussion:** What additional identity and payment-system controls are required before any real financial action?

[Answer guidance and follow-ups](../04_Capstones/C01_Support_Review/INTERVIEW.md)

### C02 · Evidence before publishing
**Mechanism:** retrieval provenance and publication gating.

**Discussion:** Why does meeting a source-count threshold not prove that a claim is supported?

[Answer guidance and follow-ups](../04_Capstones/C02_Document_Review/INTERVIEW.md)

### C03 · A research and critique team
**Mechanism:** parallel specialist evidence and critique.

**Discussion:** Why should the synthesizer preserve the critic’s uncertainty rather than smoothing it away?

[Answer guidance and follow-ups](../04_Capstones/C03_Research_Team/INTERVIEW.md)

### C04 · A recoverable batch pipeline
**Mechanism:** dynamic batch work and idempotent results.

**Discussion:** How would you coordinate two workers racing to create the same job ID?

[Answer guidance and follow-ups](../04_Capstones/C04_Batch_Orchestrator/INTERVIEW.md)

### C05 · An observable release workflow
**Mechanism:** end-to-end evaluation and release observability.

**Discussion:** How would you expand this gate to cover quality, safety, latency, and deployment rollback separately?

[Answer guidance and follow-ups](../04_Capstones/C05_Engineering_Platform/INTERVIEW.md)
