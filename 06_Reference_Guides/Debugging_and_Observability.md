# Debugging and observability
Compilation verifies graph structure, not business correctness. Start with a sample contract, inspect node updates, and compare final state to an independently stated invariant. Values streaming gives snapshots; updates streaming gives node deltas. Partial updates before failure are useful evidence but not a completed answer.

A recursion limit guards graph steps; a wall-clock timeout bounds waiting; cost budgets bound declared spending; tool permissions bound actions. These controls address different failure modes and should not be collapsed into one retry loop.

Keep input, final output, errors, and timing provenance clear. Child spans can overlap, so summing their durations can overstate root wall-clock latency. Capture identifiers and non-sensitive summaries instead of dumping secrets or entire customer records. A local trace object is not proof of cloud delivery.

**Practice:** B10–B12, I20, A09, A13–A15, A20. Trigger a late-stage failure, retain earlier evidence, and explain exactly which final claim is no longer justified.
