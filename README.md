# LangGraph Engineering Labs

**65 independent labs:** 20 beginner, 20 intermediate, 20 advanced, and five capstones. Each lab has a polished Streamlit interface, detailed setup and implementation notes, sample contracts, automated tests, debugging exercises, and interview discussion.

Explore state, routing, persistence, and recovery through 65 runnable graph labs.

## Start the learning portal
Use Python 3.12. Run these commands from the repository root.

Windows PowerShell:
```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.lock.txt
.venv\Scripts\python.exe -m streamlit run portal.py
```
macOS/Linux:
```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.lock.txt
.venv/bin/python -m streamlit run portal.py
```

The portal searches by project code and topic, shows launch commands, and includes outcome-prediction and interview self-assessment exercises. No API key is needed for its default local workflows.

## Run one lab independently
```sh
cd 01_Beginner/B01_Hello_Graph
python -m venv .venv
# Windows: .venv\Scripts\python.exe -m pip install -r requirements.txt
# Windows: .venv\Scripts\python.exe -m streamlit run app.py
# macOS/Linux:
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```
Copy the project’s `.env.example` to `.env` only when configuring optional service access. Each lab contains all its own code and data; copying one folder outside this repository is supported. Keep credentials out of source control. Optional service modes are explicitly selected and never silently substituted for failed account requests.

## What every lab contains
| File | Purpose |
|---|---|
| app.py | Complete backend and graphical interface |
| requirements.txt | Pinned direct dependencies |
| sample_data/examples.json | Three executable input/output contracts |
| tests/test_app.py | Acceptance, invalid-input, and form tests; additional failure contracts where relevant |
| INSTRUCTIONS.md | Windows/macOS/Linux setup, execution, examples, and testing |
| EXPLANATION.md | Architecture, input fields, imports, complete core, and operational boundaries |
| EXERCISES.md | Extensions and deliberate debugging tasks |
| INTERVIEW.md | Mechanism, tradeoff, failure, scaling, and evidence questions with answer guidance |
| TROUBLESHOOTING.md | Concrete recovery actions |

## Build understanding in stages
- **Beginner:** learn one mechanism, run three contracts, explain every result field.
- **Intermediate:** compose mechanisms, inspect failure paths, and compare design alternatives.
- **Advanced:** reason about correctness under restarts, concurrent users, changing datasets, resource limits, privacy, and operational load.
- **Capstone:** integrate the pipeline and defend its acceptance criteria.

See [topic coverage](docs/COVERAGE.md), [interview practice](05_Interview_Preparation/README.md), [study plan](06_Reference_Guides/Study_Plan.md), and [API compatibility](06_Reference_Guides/API_Compatibility.md).

## Verified local results
**365 passing automated tests**, a clean hashed installation, 6 standalone lab tests, and representative desktop/mobile browser checks. See [validation evidence](docs/VALIDATION.md) for scope and limitations.

## Verify
```sh
python scripts/validate_repository.py
python -m pytest -q --junitxml=docs/test-results.xml
python -m pip check
```

Validation results are recorded in [docs/VALIDATION.md](docs/VALIDATION.md). Local execution, SDK contract fixtures, live account responses, and managed deployments are treated as separate kinds of evidence. In constrained cloud command sandboxes, asynchronous SDK evaluation may need an execution context that supports its runtime facilities. The installed SDK also emits beta/dependency deprecation warnings; see the compatibility guide.

The graph labs execute the installed LangGraph runtime. Deterministic nodes isolate orchestration behavior without requiring a model account. Production identity, distributed storage, arbitrary-code isolation, and managed deployments require their own integration checks.

## Project index
- [B01 · Your first graph](01_Beginner/B01_Hello_Graph/README.md) — StateGraph compilation and invocation
- [B02 · A state contract](01_Beginner/B02_Typed_State/README.md) — typed state versus runtime validation
- [B03 · Update only what changes](01_Beginner/B03_Partial_Updates/README.md) — partial node state updates
- [B04 · A pipeline with clear stages](01_Beginner/B04_Sequential_Nodes/README.md) — explicit sequential dependencies
- [B05 · Route by policy](01_Beginner/B05_Conditional_Routing/README.md) — conditional edges and routing invariants
- [B06 · Merge updates deliberately](01_Beginner/B06_Reducers/README.md) — Annotated reducers and accumulation
- [B07 · Messages with identity](01_Beginner/B07_Message_State/README.md) — add_messages and message roles
- [B08 · A bounded tool node](01_Beginner/B08_Tools_As_Nodes/README.md) — tool schemas and controlled graph execution
- [B09 · Repeat with a stopping rule](01_Beginner/B09_Bounded_Loops/README.md) — graph loops and termination
- [B10 · Read node updates](01_Beginner/B10_Update_Streaming/README.md) — updates stream deltas
- [B11 · Read evolving state](01_Beginner/B11_Value_Streaming/README.md) — values stream snapshots
- [B12 · Architecture you can inspect](01_Beginner/B12_Graph_Visualization/README.md) — compiled graph inspection
- [B13 · The last state is available](01_Beginner/B13_Memory_Checkpoints/README.md) — checkpointer and thread configuration
- [B14 · Two threads, separate histories](01_Beginner/B14_Thread_Isolation/README.md) — thread-scoped checkpoint lookup
- [B15 · Checkpoints on disk](01_Beginner/B15_SQLite_Checkpoints/README.md) — SQLite checkpoint durability
- [B16 · Stop before the node](01_Beginner/B16_Static_Breakpoints/README.md) — static interrupt_before checkpoints
- [B17 · Ask before proceeding](01_Beginner/B17_Dynamic_Interrupts/README.md) — interrupt payload and Command resume
- [B18 · Update and route together](01_Beginner/B18_Command_Routing/README.md) — Command update and goto
- [B19 · A graph inside a graph](01_Beginner/B19_Subgraphs/README.md) — compiled subgraph composition
- [B20 · Configuration outside state](01_Beginner/B20_Runtime_Context/README.md) — Runtime context versus mutable state
- [I01 · Two branches, one result](02_Intermediate/I01_Fanout_Join/README.md) — parallel branches and explicit join
- [I02 · Map a changing workload](02_Intermediate/I02_Send_Map_Reduce/README.md) — dynamic Send fan-out and reduction
- [I03 · Replay from a known point](02_Intermediate/I03_Checkpoint_Replay/README.md) — checkpoint history and replay configuration
- [I04 · Edit a saved state](02_Intermediate/I04_State_Editing/README.md) — update_state with as_node
- [I05 · Compare two futures](02_Intermediate/I05_Time_Travel_Forks/README.md) — branching from immutable checkpoint history
- [I06 · Two decisions, one policy](02_Intermediate/I06_Two_Stage_Review/README.md) — separate interrupt stages and composite approval
- [I07 · Memory beyond one thread](02_Intermediate/I07_Namespaced_Store/README.md) — InMemoryStore namespaces
- [I08 · Validate before orchestration](02_Intermediate/I08_Validated_State/README.md) — Pydantic validation at the graph boundary
- [I09 · Async work without shared mutation](02_Intermediate/I09_Async_Branches/README.md) — ainvoke and asynchronous node boundaries
- [I10 · Retry the right failure](02_Intermediate/I10_Retry_Policy/README.md) — RetryPolicy and transient errors
- [I11 · One operation, one receipt](02_Intermediate/I11_Idempotent_Effects/README.md) — idempotency keys and stored receipts
- [I12 · An explicit fallback path](02_Intermediate/I12_Failure_Fallback/README.md) — fallback routing without hiding failure
- [I13 · A visible tool-call protocol](02_Intermediate/I13_Tool_Call_Graph/README.md) — ToolNode and tools_condition loop
- [I14 · Validate before invoking tools](02_Intermediate/I14_Tool_Validation/README.md) — tool allowlists and argument validation
- [I15 · Edit without duplicating turns](02_Intermediate/I15_Message_Replacement/README.md) — message replacement and RemoveMessage
- [I16 · A scoped specialist handoff](02_Intermediate/I16_Handoffs/README.md) — explicit specialist handoffs
- [I17 · Ground the response](02_Intermediate/I17_Retrieval_Graph/README.md) — retrieval, provenance, and abstention
- [I18 · Execute an explicit plan](02_Intermediate/I18_Plan_Execute/README.md) — bounded plan execution
- [I19 · Keep a bounded context](02_Intermediate/I19_Context_Compaction/README.md) — bounded context and role boundaries
- [I20 · Test behavior, not topology alone](02_Intermediate/I20_Graph_Evaluation/README.md) — behavioral evaluation for graph workflows
- [A01 · A job that resumes](03_Advanced/A01_Durable_Jobs/README.md) — durable stepwise execution
- [A02 · Evolve persisted application state](03_Advanced/A02_Payload_Migration/README.md) — versioned payload migration
- [A03 · A durable memory namespace](03_Advanced/A03_Durable_Preferences/README.md) — durable namespaced memory and SQL parameters
- [A04 · Reject a lost update](03_Advanced/A04_Optimistic_Concurrency/README.md) — optimistic version checks
- [A05 · Record intent before dispatch](03_Advanced/A05_Transactional_Outbox/README.md) — transactional outbox and idempotent dispatch
- [A06 · Approval needs permission](03_Advanced/A06_Authorized_Review/README.md) — authorization before interrupt resume
- [A07 · A timeout is an outcome](03_Advanced/A07_Async_Timeouts/README.md) — async cancellation and timeout reporting
- [A08 · Cache the right state](03_Advanced/A08_Node_Caching/README.md) — CachePolicy and pure-node input keys
- [A09 · Stop an overlong graph](03_Advanced/A09_Recursion_Budgets/README.md) — GraphRecursionError as a resource guard
- [A10 · An exportable graph](03_Advanced/A10_Graph_Serving/README.md) — graph exports and functional HTTP validation
- [A11 · Authenticate before authorizing](03_Advanced/A11_Signed_Identity/README.md) — authentication versus authorization
- [A12 · Filter before exposing data](03_Advanced/A12_Tenant_Boundaries/README.md) — pre-execution tenant filtering
- [A13 · Follow execution across spans](03_Advanced/A13_Trace_Propagation/README.md) — RunTree hierarchy and trace privacy
- [A14 · Stop before spending the budget](03_Advanced/A14_Cost_Budgets/README.md) — pre-step budget enforcement
- [A15 · Preserve partial evidence on failure](03_Advanced/A15_Streaming_Failures/README.md) — partial stream evidence and explicit failure
- [A16 · A functional workflow](03_Advanced/A16_Functional_API/README.md) — functional entrypoint and task boundaries
- [A17 · Reusable specialist graphs](03_Advanced/A17_Specialist_Subgraphs/README.md) — specialist subgraph contracts
- [A18 · Verify what you saved](03_Advanced/A18_Artifact_Integrity/README.md) — content hashes and artifact provenance
- [A19 · Evaluate before release](03_Advanced/A19_Release_Gates/README.md) — dataset-driven release gates
- [A20 · Measure every stage](03_Advanced/A20_Workflow_Observability/README.md) — node-level observability and privacy
- [C01 · Support with a review boundary](04_Capstones/C01_Support_Review/README.md) — durable support routing and review
- [C02 · Evidence before publishing](04_Capstones/C02_Document_Review/README.md) — retrieval provenance and publication gating
- [C03 · A research and critique team](04_Capstones/C03_Research_Team/README.md) — parallel specialist evidence and critique
- [C04 · A recoverable batch pipeline](04_Capstones/C04_Batch_Orchestrator/README.md) — dynamic batch work and idempotent results
- [C05 · An observable release workflow](04_Capstones/C05_Engineering_Platform/README.md) — end-to-end evaluation and release observability
