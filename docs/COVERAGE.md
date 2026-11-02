# Topic coverage and evidence

| Stage | Lab | Mechanism | Architecture / interview tradeoff |
|---|---|---|---|
| Beginner | [B01](../01_Beginner/B01_Hello_Graph/README.md) | StateGraph compilation and invocation | Why is graph construction separate from graph execution? |
| Beginner | [B02](../01_Beginner/B02_Typed_State/README.md) | typed state versus runtime validation | TypedDict documents a contract but does not validate every value at runtime. Where should validation occur? |
| Beginner | [B03](../01_Beginner/B03_Partial_Updates/README.md) | partial node state updates | Why return only changed fields instead of rebuilding all state in every node? |
| Beginner | [B04](../01_Beginner/B04_Sequential_Nodes/README.md) | explicit sequential dependencies | What can go wrong if a consumer runs before the node producing its input? |
| Beginner | [B05](../01_Beginner/B05_Conditional_Routing/README.md) | conditional edges and routing invariants | How do explicit routes differ from an unrestricted model selecting side effects? |
| Beginner | [B06](../01_Beginner/B06_Reducers/README.md) | Annotated reducers and accumulation | When should repeated updates append, replace, deduplicate, or reject? |
| Beginner | [B07](../01_Beginner/B07_Message_State/README.md) | add_messages and message roles | Why does message identity matter when editing conversation state? |
| Beginner | [B08](../01_Beginner/B08_Tools_As_Nodes/README.md) | tool schemas and controlled graph execution | Does wrapping a function as a tool provide authorization or resource isolation by itself? |
| Beginner | [B09](../01_Beginner/B09_Bounded_Loops/README.md) | graph loops and termination | Why validate a business stopping condition as well as setting a recursion limit? |
| Beginner | [B10](../01_Beginner/B10_Update_Streaming/README.md) | updates stream deltas | How do node updates differ from snapshots of the entire state? |
| Beginner | [B11](../01_Beginner/B11_Value_Streaming/README.md) | values stream snapshots | What does collecting a stream into a list lose compared with rendering events as they arrive? |
| Beginner | [B12](../01_Beginner/B12_Graph_Visualization/README.md) | compiled graph inspection | Why is a graph diagram evidence of structure but not evidence of successful deployment? |
| Beginner | [B13](../01_Beginner/B13_Memory_Checkpoints/README.md) | checkpointer and thread configuration | What failure destroys an in-memory checkpoint even when a thread ID is stable? |
| Beginner | [B14](../01_Beginner/B14_Thread_Isolation/README.md) | thread-scoped checkpoint lookup | Why is a thread ID an address for state rather than proof of authorization? |
| Beginner | [B15](../01_Beginner/B15_SQLite_Checkpoints/README.md) | SQLite checkpoint durability | Which failures can one local SQLite file survive, and which need backups or replication? |
| Beginner | [B16](../01_Beginner/B16_Static_Breakpoints/README.md) | static interrupt_before checkpoints | How does resuming a static breakpoint differ from supplying a dynamic interrupt decision? |
| Beginner | [B17](../01_Beginner/B17_Dynamic_Interrupts/README.md) | interrupt payload and Command resume | Which parts of a node may execute again after resume, and where should side effects be placed? |
| Beginner | [B18](../01_Beginner/B18_Command_Routing/README.md) | Command update and goto | Why should destination names and return annotations agree? |
| Beginner | [B19](../01_Beginner/B19_Subgraphs/README.md) | compiled subgraph composition | When should child and parent share a state schema, and when is an adapter preferable? |
| Beginner | [B20](../01_Beginner/B20_Runtime_Context/README.md) | Runtime context versus mutable state | Why should authorization context come from a trusted caller rather than user-supplied state? |
| Intermediate | [I01](../02_Intermediate/I01_Fanout_Join/README.md) | parallel branches and explicit join | Why is a reducer necessary for concurrent findings updates? |
| Intermediate | [I02](../02_Intermediate/I02_Send_Map_Reduce/README.md) | dynamic Send fan-out and reduction | How would you preserve stable output ordering when task completion order is nondeterministic? |
| Intermediate | [I03](../02_Intermediate/I03_Checkpoint_Replay/README.md) | checkpoint history and replay configuration | Which operations may run again during replay, and why do external effects need idempotency? |
| Intermediate | [I04](../02_Intermediate/I04_State_Editing/README.md) | update_state with as_node | Why does the node attribution influence which steps run after a state edit? |
| Intermediate | [I05](../02_Intermediate/I05_Time_Travel_Forks/README.md) | branching from immutable checkpoint history | How would you distinguish exploratory forks from the production thread that may perform side effects? |
| Intermediate | [I06](../02_Intermediate/I06_Two_Stage_Review/README.md) | separate interrupt stages and composite approval | When should rejection short-circuit later reviewers rather than collecting all decisions? |
| Intermediate | [I07](../02_Intermediate/I07_Namespaced_Store/README.md) | InMemoryStore namespaces | What trusted information should determine a namespace in a multi-tenant application? |
| Intermediate | [I08](../02_Intermediate/I08_Validated_State/README.md) | Pydantic validation at the graph boundary | Why is a TypedDict annotation insufficient for hostile external input? |
| Intermediate | [I09](../02_Intermediate/I09_Async_Branches/README.md) | ainvoke and asynchronous node boundaries | Why does async execution not make CPU-bound work automatically faster? |
| Intermediate | [I10](../02_Intermediate/I10_Retry_Policy/README.md) | RetryPolicy and transient errors | Why can retries duplicate an external side effect even if the final graph state looks correct? |
| Intermediate | [I11](../02_Intermediate/I11_Idempotent_Effects/README.md) | idempotency keys and stored receipts | How should the system respond when one idempotency key is reused for different input? |
| Intermediate | [I12](../02_Intermediate/I12_Failure_Fallback/README.md) | fallback routing without hiding failure | When would returning stale fallback guidance be worse than failing the request? |
| Intermediate | [I13](../02_Intermediate/I13_Tool_Call_Graph/README.md) | ToolNode and tools_condition loop | Which part is deterministic protocol scaffolding here, and what would a live model add? |
| Intermediate | [I14](../02_Intermediate/I14_Tool_Validation/README.md) | tool allowlists and argument validation | Why should tool selection and tool authorization be separate checks? |
| Intermediate | [I15](../02_Intermediate/I15_Message_Replacement/README.md) | message replacement and RemoveMessage | Why can blind list concatenation duplicate edited assistant turns? |
| Intermediate | [I16](../02_Intermediate/I16_Handoffs/README.md) | explicit specialist handoffs | What context should be transferred to a specialist, and what should remain private? |
| Intermediate | [I17](../02_Intermediate/I17_Retrieval_Graph/README.md) | retrieval, provenance, and abstention | Why do source relevance, factual truth, and generated-answer correctness require different evaluation? |
| Intermediate | [I18](../02_Intermediate/I18_Plan_Execute/README.md) | bounded plan execution | Why must a model-produced plan be validated independently before tool execution? |
| Intermediate | [I19](../02_Intermediate/I19_Context_Compaction/README.md) | bounded context and role boundaries | When does truncation require requesting shorter input rather than claiming the context was summarized? |
| Intermediate | [I20](../02_Intermediate/I20_Graph_Evaluation/README.md) | behavioral evaluation for graph workflows | Which failures can remain invisible if you test only whether a graph compiles? |
| Advanced | [A01](../03_Advanced/A01_Durable_Jobs/README.md) | durable stepwise execution | How do stable job IDs and replay-safe units make restart recovery possible? |
| Advanced | [A02](../03_Advanced/A02_Payload_Migration/README.md) | versioned payload migration | Why must application-state migration be distinguished from serializer and dependency compatibility? |
| Advanced | [A03](../03_Advanced/A03_Durable_Preferences/README.md) | durable namespaced memory and SQL parameters | Why is a correctly scoped storage key not a substitute for verifying the requesting tenant? |
| Advanced | [A04](../03_Advanced/A04_Optimistic_Concurrency/README.md) | optimistic version checks | When should a client retry automatically, and when must it reconcile the conflicting edit? |
| Advanced | [A05](../03_Advanced/A05_Transactional_Outbox/README.md) | transactional outbox and idempotent dispatch | Why does local exactly-once recording not automatically guarantee exactly-once delivery to an external provider? |
| Advanced | [A06](../03_Advanced/A06_Authorized_Review/README.md) | authorization before interrupt resume | Why is an approve button insufficient without server-side identity and resource authorization? |
| Advanced | [A07](../03_Advanced/A07_Async_Timeouts/README.md) | async cancellation and timeout reporting | What happens if the underlying library ignores cancellation or performs a side effect before timeout? |
| Advanced | [A08](../03_Advanced/A08_Node_Caching/README.md) | CachePolicy and pure-node input keys | What authorization or freshness bug appears when a tenant or data version is omitted from a cache key? |
| Advanced | [A09](../03_Advanced/A09_Recursion_Budgets/README.md) | GraphRecursionError as a resource guard | Why does a graph step limit not replace a wall-clock timeout, token budget, or tool authorization? |
| Advanced | [A10](../03_Advanced/A10_Graph_Serving/README.md) | graph exports and functional HTTP validation | Why does a manifest or a listening port not establish a working managed deployment? |
| Advanced | [A11](../03_Advanced/A11_Signed_Identity/README.md) | authentication versus authorization | How can a valid identity still lack permission for a resource? |
| Advanced | [A12](../03_Advanced/A12_Tenant_Boundaries/README.md) | pre-execution tenant filtering | Why is filtering model output too late if unauthorized data was already sent to the model? |
| Advanced | [A13](../03_Advanced/A13_Trace_Propagation/README.md) | RunTree hierarchy and trace privacy | Why does a local trace ID not prove that a cloud run was received? |
| Advanced | [A14](../03_Advanced/A14_Cost_Budgets/README.md) | pre-step budget enforcement | How would you reconcile estimated cost with actual billed token usage? |
| Advanced | [A15](../03_Advanced/A15_Streaming_Failures/README.md) | partial stream evidence and explicit failure | How should a client distinguish partial updates from a completed response? |
| Advanced | [A16](../03_Advanced/A16_Functional_API/README.md) | functional entrypoint and task boundaries | When is a functional API clearer than an explicitly declared StateGraph? |
| Advanced | [A17](../03_Advanced/A17_Specialist_Subgraphs/README.md) | specialist subgraph contracts | What coupling appears when all specialist graphs share one large state schema? |
| Advanced | [A18](../03_Advanced/A18_Artifact_Integrity/README.md) | content hashes and artifact provenance | Why does a matching digest establish byte integrity but not source authenticity or semantic truth? |
| Advanced | [A19](../03_Advanced/A19_Release_Gates/README.md) | dataset-driven release gates | Why must a release gate account for dataset coverage as well as an aggregate pass rate? |
| Advanced | [A20](../03_Advanced/A20_Workflow_Observability/README.md) | node-level observability and privacy | Why should monitoring distinguish the primary failure, fallback behavior, and final user-visible outcome? |
| Capstone | [C01](../04_Capstones/C01_Support_Review/README.md) | durable support routing and review | What additional identity and payment-system controls are required before any real financial action? |
| Capstone | [C02](../04_Capstones/C02_Document_Review/README.md) | retrieval provenance and publication gating | Why does meeting a source-count threshold not prove that a claim is supported? |
| Capstone | [C03](../04_Capstones/C03_Research_Team/README.md) | parallel specialist evidence and critique | Why should the synthesizer preserve the critic’s uncertainty rather than smoothing it away? |
| Capstone | [C04](../04_Capstones/C04_Batch_Orchestrator/README.md) | dynamic batch work and idempotent results | How would you coordinate two workers racing to create the same job ID? |
| Capstone | [C05](../04_Capstones/C05_Engineering_Platform/README.md) | end-to-end evaluation and release observability | How would you expand this gate to cover quality, safety, latency, and deployment rollback separately? |

This is a practical curriculum map, not a claim that every possible library API or interview question is covered.
