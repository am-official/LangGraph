# Interview rehearsal · Authenticate before authorizing
## Explain the mechanism
**Question:** How does this lab implement authentication versus authorization?

**Expected reasoning:** Start with the input contract, identify the state/record representation, walk through the critical operations in app.py, and connect each expected sample field to the operation that produces it. Use the three executable contracts as evidence.

## Defend the tradeoff
**Question:** How can a valid identity still lack permission for a resource?

**Expected reasoning:** State the guarantees provided by this implementation, identify the failure model it handles, and describe the operational cost or loss of flexibility. Then propose an alternative and explain which tests would need to change.

## Diagnose the failure
**Question:** A default run succeeds, but a user submits an empty field, invalid record, or wrong resume action. What should happen?

**Expected reasoning:** Identify the exact validation/state boundary. Reject before unsafe work, clear stale UI results, and retain enough non-sensitive evidence for diagnosis. A success badge from an earlier run is not evidence for the new request.

## Scale the design
**Question:** What must change before using this with concurrent users or a remote service?

**Expected reasoning:** Discuss trusted identity, tenant-scoped state, transaction isolation, checkpoint/storage durability, input/resource limits, idempotency, timeouts, privacy, observability, and service-specific authorization. Explain only concerns relevant to this workflow.

## Prove the claim
**Question:** Which behaviors are verified, and which are outside the test boundary?

**Expected reasoning:** Point to the acceptance and failure tests. Distinguish local framework execution, a fixture exercising an SDK boundary, a real service acknowledgement, and production deployment. Local deterministic workflow; model intelligence and managed deployment are separate concerns.

## Scoring rubric
Score each answer 0–2: 0 = unsupported claim; 1 = correct concept without code/evidence; 2 = correct mechanism with a failure case and a justified tradeoff. Target 8/10 or better on repeated explanations without memorizing this wording.

## Concrete prediction exercise
For input `{"role": "viewer", "operation": "read", "resource_tenant": "team-a"}`, explain why the expected fields are `{"authorized": true}`. Identify the exact operations responsible, then propose one counterexample that would reveal a missing validation or incorrect state transition.
