# Human review and interruption
Static breakpoints stop before or after a declared node and resume without supplying a dynamic value. Dynamic interrupt emits a review payload and returns the later value supplied by Command(resume=...). Both need the same checkpointer/thread configuration to continue the intended execution.

A node containing an interrupt can restart on resume. Put irreversible effects after approval, and make any earlier work replay-safe. An approval is a decision, not proof of the reviewer's identity or authority. Verify the actor, tenant, resource, and allowed action on the server before resuming protected work.

Two-stage approvals need an explicit policy: collect both decisions, short-circuit rejection, or escalate disagreement. Also decide how to handle stale requests whose underlying data changed while review was pending. Bind approval to the actual request/revision rather than accepting a new unreviewed payload at resume time.

**Practice:** B16–B17, I06, A06, C01. Submit, inspect the pause, reopen the saver, reject the request, and verify that duplicate resume and unauthorized approval are refused.
