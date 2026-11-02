# Practice tasks
1. Run all three sample contracts and explain each returned field. Success: exact expected-field matches.
2. Demonstrate thread-scoped checkpoint lookup by changing one input. Record your prediction and observed result. Success: explain why they match or differ.
3. Add a malformed, empty, and boundary input to the tests. Success: the application rejects invalid data before the protected operation.
4. Evaluate this tradeoff: Why is a thread ID an address for state rather than proof of authorization? Write a short alternative design and state the invariant it must preserve.
5. Implement an extension with one additional acceptance test and one failure test. Success: existing behavior remains intact and the new property has independent evidence.

## Debugging exercise
Remove or alter one important validation/reducer/routing step in a temporary copy. Identify a test that should fail. Restore the implementation and explain why that test protects useful behavior rather than mirroring a line of code.
