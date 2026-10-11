# Week 1 — What a computer is, binary, and your environment

**Objective:** by Friday you can explain what happens when a program runs (from source code to
hardware and back), read and write binary, and you have a working Python + Git environment with
your trackers in use. ~2 hrs/day.

> Only Day 1 has a full lesson file right now ([`../lessons/day-001.md`](../lessons/day-001.md)).
> Days 2–7 are planned below; generate each as a full lesson with `NEXT DAY` when you reach it.

## Daily plan

### Day 1 (Mon) — What is a computer? Hardware, software, and the execution chain
- **Lesson:** [`../lessons/day-001.md`](../lessons/day-001.md) (complete, ~2 hrs).
- **You'll produce:** hardware/software classification, a run Python program, a CLI session, a
  fixed bug, a quiz attempt, and a teach-back.
- **Record** evidence in [`../state/progress.md`](../state/progress.md).

### Day 2 (Tue) — Bits & binary
- Why binary? bits, bytes, place value; binary→decimal and decimal→binary by hand.
- Coding: write `decimal_to_binary` and `binary_to_decimal` yourself (you write it — hints only).
- Start project #1 (converter). Math: number bases.
- Evidence: both functions work on 5 test cases you choose.

### Day 3 (Wed) — Hexadecimal + bytes + review
- Hex as compact binary; nibbles; why hex is everywhere (addresses, colors).
- **First spaced-repetition review:** Day 1 concepts (`REVISE`).
- Coding: extend converter to hex. Evidence: converter handles dec/bin/hex.

### Day 4 (Thu) — Inside the box: CPU, RAM, storage, I/O (deeper)
- The roles revisited with the fetch-decode-execute preview; the memory hierarchy at a glance.
- Lab: label a diagram of a computer; map each part to what it does during a program run.
- Evidence: written explanation of what each component does when you run your converter.

### Day 5 (Fri) — Command line + Git initialization
- PowerShell essentials (paths, listing, running Python); initialize Git; first commits.
- You'll put the repo under version control and commit your Week-1 work.
- Evidence: `git log` shows ≥3 meaningful commits (e.g. `chore: initialize learning repository`).

### Day 6 (Sat) — Project day
- Finish the first version of project #1 (decimal↔binary, with hex if ready).
- Write its entry in [`../state/project-log.md`](../state/project-log.md) with tests and a
  retrospective.
- Evidence: converter + tests + retrospective.

### Day 7 (Sun) — Review & self-quiz
- `REVISE` all Week-1 items; take the Week-1 self-quiz; write a Feynman explanation of the
  execution chain.
- Update [`../state/review-queue.md`](../state/review-queue.md) and
  [`../state/progress.md`](../state/progress.md).
- Evidence: quiz attempted + graded; review queue scheduled; teach-back written.

## Week-1 completion evidence (all required)
- [ ] Days 1–7 worked through.
- [ ] Project #1 converts decimal↔binary (hex optional this week), with tests.
- [ ] Repo under Git with ≥3 meaningful commits.
- [ ] Review queue seeded with Week-1 foundational concepts.
- [ ] Progress tracker updated with sessions and evidence.
- [ ] One written teach-back of the execution chain.

## What Week 1 deliberately does NOT do
No AI APIs, no frameworks, no advanced Python. Foundations first.
