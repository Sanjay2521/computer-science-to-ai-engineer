# First 12 Weeks

Detailed plan for the opening quarter (Phase 0 → early Phase 2, with DSA and math threads
starting). Not every week is equally dense — Weeks 6 and 12 are lighter (integration/review).
Buffer time is built in; if you fall behind, use it rather than creating a backlog.

> ~2 hrs/day. Each week ≈ 4 concept days · 1 integration day · 1 project day · 1 review day.

## Week 1 — What a computer is + binary + environment
- **Objective:** understand hardware/software, the execution chain, and binary; set up tools.
- **Prerequisites:** none.
- **Core concepts:** computer, hardware, software, program, CPU/RAM/storage/I/O; bits & binary;
  how a Python statement becomes work.
- **Reading/viewing:** CrashCourse CS (ep. 1–3) or Nand2Tetris intro; Python docs intro.
- **Coding:** run Python; tiny scripts; first binary↔decimal conversions in code.
- **DSA topic:** complexity *intuition* (what "faster" means) — no problems yet.
- **Math topic:** number bases (binary, decimal, hex).
- **Lab:** classify hardware vs software; trace a program's execution path.
- **Mini-project:** start #1 number-system converter (decimal↔binary).
- **Quiz:** Day 7 self-quiz.
- **Debugging challenge:** fix a broken Python one-liner (in Day 1).
- **Review items:** execution chain; CPU/RAM/storage/I/O roles; binary place values.
- **Completion evidence:** Day 1–7 done; converter converts dec↔bin; trackers updated.
- Full breakdown: [`week-01.md`](week-01.md).

## Week 2 — Binary arithmetic + Python basics
- **Objective:** two's complement & hex fluency; Python variables, types, control flow.
- **Core concepts:** unsigned/signed integers, two's complement, hex; Python types,
  references/mutability, if/for/while.
- **Coding:** extend converter to hex and two's complement.
- **DSA topic:** arrays & strings (indexing, iteration, complexity of access).
- **Math topic:** functions and their graphs.
- **Mini-project:** #1 converter adds hex + signed integers.
- **Quiz + debugging + review.** Evidence: converter handles all bases; Python basics demoed.

## Week 3 — Functions, modules, venv + boolean logic
- **Objective:** structure code; boolean algebra → logic gates.
- **Core concepts:** functions, scope, modules, packages, virtual environments; boolean
  algebra, AND/OR/NOT/NAND/XOR.
- **Coding:** refactor converter into functions/modules; set up a venv properly.
- **DSA topic:** two pointers (intro).
- **Math topic:** logarithms & exponents (and why log appears in complexity).
- **Mini-project:** start #2 logic-gate simulator (NOT, AND, OR from booleans).
- **Quiz + review.** Evidence: venv working; converter modularized; gates simulate truth tables.

## Week 4 — Logic gates → circuits + Git + CHECKPOINT
- **Objective:** combinational circuits; Git workflow; first assessment.
- **Core concepts:** gates → half/full adder; Git commits/branches/diffs.
- **Coding:** build adder from gates in the simulator; put the repo under Git with good commits.
- **DSA topic:** stacks & queues (concept + simple implementation).
- **Math topic:** sequences & summations.
- **Mini-project:** #2 simulator computes binary addition via a full adder.
- **Assessment:** **Checkpoint 1** — explain execution chain; binary arithmetic; trace a Python
  program; build a gate from booleans. (`EXAM` mode.)
- **Evidence:** checkpoint passed; adder works; repo has clean history.

## Week 5 — CPU concepts + Python data structures
- **Objective:** ALU, registers, control unit, fetch-decode-execute; Python lists/dicts/sets.
- **Core concepts:** registers, ALU, control unit, the instruction cycle; list/dict/set/tuple.
- **Coding:** model a register and a tiny ALU op in Python.
- **DSA topic:** hash tables / sets (how dict works).
- **Math topic:** vectors (intro).
- **Mini-project:** start #3 tiny instruction emulator (define a 3–4 instruction ISA).
- **Quiz + review.**

## Week 6 — Integration & review week (lighter)
- **Objective:** consolidate Weeks 1–5; catch up on buffer.
- **Activities:** `REVISE` due items; redo one earlier exercise from memory; extend the emulator;
  write a Feynman explanation of the execution chain.
- **No new heavy concepts.** Evidence: review queue current; one teach-back written.

## Week 7 — Memory model + Python OOP
- **Objective:** stack/heap, memory hierarchy; classes & objects.
- **Core concepts:** memory hierarchy, cache, stack vs heap; classes, methods, composition.
- **Coding:** model the emulator's memory; convert the emulator to OOP.
- **DSA topic:** recursion.
- **Math topic:** dot products.
- **Mini-project:** #3 emulator executes a small program.

## Week 8 — Intro to C + pointers
- **Objective:** see memory directly.
- **Core concepts:** compilation/linking, primitive types, arrays, pointers, addresses.
- **Coding:** first C programs; print addresses; pointer basics.
- **DSA topic:** binary search.
- **Math topic:** matrices (intro).
- **Mini-project:** start #4 C memory experiments.

## Week 9 — C memory + Python iterators/generators
- **Objective:** stack/heap in C; lazy iteration in Python.
- **Core concepts:** heap allocation, structs, segfaults, undefined behavior; iterators,
  generators, comprehensions.
- **Coding:** C structs + manual allocation; Python generators.
- **DSA topic:** sorting (implement one; analyze it).
- **Math topic:** matrix multiplication.
- **Mini-project:** #4 C memory experiments complete.

## Week 10 — Decorators/context managers + trees
- **Objective:** Python power features; tree structures.
- **Core concepts:** decorators, context managers, type hints, dataclasses; trees & BSTs.
- **Coding:** write a decorator and a context manager; implement a BST.
- **DSA topic:** trees / BST.
- **Math topic:** linear transformations (intro).
- **Mini-project:** start #7 data-structures library (stack, queue, BST).

## Week 11 — Testing, debugging, logging + CLI project
- **Objective:** professional Python practices.
- **Core concepts:** pytest, debugging strategy, logging, profiling basics.
- **Coding:** test suite for the data-structures library; a logged, tested CLI.
- **DSA topic:** heaps / priority queues.
- **Math topic:** derivatives (intro).
- **Mini-project:** #5 command-line utility.

## Week 12 — Integration, project, CHECKPOINT (lighter new content)
- **Objective:** consolidate the quarter; second checkpoint.
- **Activities:** finish the CLI; polish the data-structures library with tests; `REVISE`.
- **Assessment:** **Checkpoint 2** — Python fluency, C/pointers, DSA (implement a structure),
  complexity analysis, trace the emulator.
- **Evidence:** checkpoint passed; projects #4–5 done, #7 underway; all trackers current.

---
After Week 12 you'll be solidly in Phase 2→3. The agent generates Weeks 13+ as you demonstrate
readiness (`NEXT DAY` for lessons, and ask for the next week's plan when Week 12 is complete).
