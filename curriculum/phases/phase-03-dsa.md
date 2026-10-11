# Phase 3 — Data Structures & Algorithms

**Timeline:** ~12–16 weeks (overlaps the math block, Phase 4 file) ·
**Module:** [03-data-structures-and-algorithms](../../modules/03-data-structures-and-algorithms/)

## Goal
Solve problems by choosing the right structure and algorithm, and reason about cost. Learn
*patterns and invariants*, not memorized answers.

## Prerequisites
Phase 2.

## Topics & required depth
- **Complexity:** Big-O, Big-Θ, Big-Ω; amortized analysis intuition.
- **Linear structures:** arrays, strings, linked lists, stacks, queues, deques, hash tables, sets.
- **Recursion & search:** recursion, binary search, sorting algorithms.
- **Trees & heaps:** trees, BSTs, balanced-tree concepts, heaps/priority queues, tries.
- **Graphs:** representations, BFS, DFS, union-find, topological sort, shortest paths, MST.
- **Patterns:** two pointers, sliding window, prefix sums, monotonic stack, greedy, backtracking,
  divide & conquer, dynamic programming, bit manipulation.

Depth: implement each core structure yourself; solve medium problems independently across every
pattern; always state time & space complexity.

## Mathematics thread
Runs in parallel — see [`phase-04-mathematics.md`](phase-04-mathematics.md) (linear algebra &
calculus start here).

## Hands-on labs
Implement each structure from scratch with tests; build an algorithm visualizer; time your
implementations and compare to theoretical complexity.

## From-scratch implementation
A data-structures library (lists, stacks, queues, hash map, BST, heap, graph) — before relying on
`collections`/`heapq`, then compare.

## Mini-project
Project #8 — algorithm visualizer (sorting/search/graph traversal).

## Major project
Project #7 — data-structures library with a full test suite.

## Logging requirement
Every problem goes in [`../../state/dsa-tracker.md`](../../state/dsa-tracker.md): problem, topic,
difficulty, initial idea, final approach, time/space, mistake, hint level, solved independently?,
retry date.

## Recommended resources
MIT 6.006; a pattern-based problem set. (See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Pick & justify a structure for a scenario; analyze complexity; implement a structure and a graph
algorithm from scratch; solve an unseen medium problem.

## Exit criteria
- Core structures implemented from scratch with tests.
- Independent solves logged across all major patterns.
- Fluent complexity analysis.

## Common mistakes
- Memorizing solutions instead of recognizing patterns.
- Ignoring space complexity.
- Off-by-one in binary search; forgetting the visited set in graph traversal.

## Connection to next phase
Problem-solving + the math spine → understand the systems programs run on (Phase 4: OS,
networking, databases).
