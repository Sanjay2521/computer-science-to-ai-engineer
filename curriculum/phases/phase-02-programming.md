# Phase 2 — Programming, C, Git, Shell, Testing

**Timeline:** ~8–12 weeks · **Module:** [02-programming](../../modules/02-programming/)

## Goal
Fluency in Python, enough C to see memory directly, and professional tooling (Git, shell,
debuggers, tests).

## Prerequisites
Phase 1.

## Topics & required depth
- **Python (deep):** syntax/expressions, data types, variables & references, mutability, control
  flow, functions, scope, recursion, modules/packages, virtual environments, files, exceptions,
  classes/OOP, composition, iterators, generators, comprehensions, decorators, context managers,
  type hints, dataclasses, testing, debugging, logging, profiling, threads/processes, async,
  memory behavior, packaging & dependency management, standard library.
- **C (enough to understand the metal):** compilation, linking, source/headers, primitive types,
  arrays, strings, pointers, addresses, stack memory, heap allocation, structs, function calls,
  memory errors, undefined behavior, segfaults, basic debugging. *Not* a multi-year C specialty.
- **Tooling:** PowerShell & CLI (paths, env vars, processes, pipes/redirection); Git (commits,
  branches, merge conflicts, PRs, diffs, rebase concepts); debuggers; editors; package managers.

## Mathematics thread
Functions; logarithms & exponents; sequences & summations.

## DSA thread
Complexity analysis; arrays & strings; linked lists, stacks, queues; two pointers.

## Hands-on labs
C pointer/address experiments; pytest suites; a logged, profiled Python script; Git branching
exercises with deliberate merge conflicts.

## From-scratch implementation
A small container type (e.g. your own stack) before using library abstractions.

## Mini-project
Project #5 — command-line utility (argument parsing, files, tests, packaging).

## Major project
Project #6 — mini shell (read commands, spawn processes, handle pipes).

## Recommended resources
Official Python docs; CS50 (C); Pro Git; The Missing Semester. (See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Write an idiomatic, tested Python module; explain and reproduce a segfault; drive a Git workflow
including a merge conflict.

## Exit criteria
- Idiomatic, typed, tested Python; comfortable with generators/decorators/context managers.
- Explain pointers and a segfault in C.
- Confident Git and shell usage.

## Common mistakes
- Confusing variables with the objects they reference (mutability bugs).
- Mutable default arguments; late-binding closures.
- In C: off-by-one and use-after-free causing segfaults.
- Committing a venv or secrets (see [`../../.gitignore`](../../.gitignore)).

## Connection to next phase
You can code → formalize problem-solving and build the math spine in Phase 3.
