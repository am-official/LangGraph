# Concurrency and effects
Graph parallelism can produce concurrent state updates. Reducers define merging; join edges define when downstream synthesis may proceed. Dynamic Send tasks should include stable indices if presentation order matters. Async I/O overlaps waiting but does not turn a CPU-bound calculation into faster parallel computation.

Storage concurrency is a separate layer. Optimistic version checks reject lost updates. Immediate SQLite transactions serialize the teaching examples' read-check-write critical sections; they are not a distributed lock. A unique job or operation key prevents conflicting reuse only if the operation's input identity is checked too.

Caching is appropriate for pure operations with a complete key. Include tenant, authorization-relevant scope, data version, model/prompt revision, and freshness requirements where relevant. Never omit them merely to improve hit rate. An in-memory TTL cache does not persist across restart.

Retries should target transient failures with bounded attempts and backoff. Permanent validation errors should not be retried unchanged. A timeout does not prove that a remote side effect did not occur; reconcile receipts and avoid repeating irreversible operations blindly.

**Practice:** I01–I02, I09–I12, A04–A08, C04. Explain reducer semantics, storage isolation, and external-effect idempotency as three different concerns.
