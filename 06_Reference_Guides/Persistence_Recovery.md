# Persistence and recovery
A checkpointer stores execution snapshots. A thread ID selects a continuing state history; a checkpoint ID selects a particular snapshot. InMemorySaver lasts only for that process. SqliteSaver persists on the current filesystem but does not provide protection from disk or region loss.

Replay executes work after a chosen checkpoint. State edits can create alternate futures; as_node determines the attribution of the update and therefore the following work. Retain original checkpoint references when comparing forks. Historical snapshots should not be described as mutable records simply because the latest thread view changes.

Execution recovery and exactly-once external effects are separate properties. A process can perform a side effect and crash before recording completion, so the node may replay. Use idempotency keys, a receipt ledger, or a transactional outbox appropriate to the external service. Do not hold a database write transaction open while waiting on a remote model call.

Application payload migration requires explicit schema versions, tested transforms, and a rollback/backfill strategy. It does not guarantee that arbitrary checkpoint serializer or dependency upgrades remain compatible. Back up representative histories and rehearse restore before production upgrades.

**Practice:** B13–B15, I03–I05, I11, A01–A05. Reopen the database in a new process and test both successful continuation and conflicting input under one operation ID.
