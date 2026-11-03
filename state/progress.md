# Progress

> Authoritative current position. The agent reads this at the start of every session and updates
> it with **evidence**. Status labels: Not started · Introduced · Practicing · Demonstrated ·
> Needs review · Mastered for current level. Avoid fake precision.

## Current position
- **Phase:** 0 — Learning method & environment
- **Module:** [00 — Learning how to learn](../modules/00-learning-how-to-learn/)
- **Week:** 1 (see [week-01](../curriculum/week-01.md))
- **Lesson:** Python Basics ladder — P1–P5 ✅ (2026-11-03) · **P6 (for loops & range)** next.
  (Day 3/hex paused until P1–P9 done.)
- **Start date:** 2026-10-11
- **Current project:** #1 Number-system converter — **paused** at hex; resumes after Python basics P9
- **Current DSA pattern:** none yet
- **Current math topic:** number bases (binary → hex)

## Totals
- Completed study sessions: 2
- Approximate focused hours: ~4

## Concepts by mastery level
*(Populated as you demonstrate evidence. L1 explain · L2 implement · L3 debug · L4 transfer.)*
- **L1 (explain):** hardware vs software · the execution chain (source → interpreter → OS → CPU →
  hardware → output) · roles of CPU/RAM/storage/I/O · RAM is volatile (variables live in RAM) ·
  int vs str and how `+` differs by type · `NameError` vs `SyntaxError`
- **L2 (implement):** `binary_to_decimal` and `decimal_to_binary` written from scratch, all tests
  pass (converter.py) · place-value & repeated-division methods
- **L3 (debug/modify):** fixed the `prnt`→`print` NameError (day01_bug.py) · fixed the place-value
  logic bug in day02_bug.py (distinguished a logic error from a crash)
- **L4 (transfer):** —

## Topics needing review
- Execution chain — keep the OS and hardware layers in the picture (tended to skip them).
- "Interpreter → executable code" phrasing — Python translates to low-level ops, not a standalone .exe.
- **2ᴺ vs max value** — 2⁸ = 256 patterns, max value 255 (off-by-one). See mistakes-log 2026-10-19.
- `bin()` returns a string with a `0b` prefix; `int(s, 2)` parses binary — finish Exercise C note.

## Recent assessment results
- — (first checkpoint ~end of Week 4)

## Blocking prerequisites
- None.

## Next recommended action
👉 Do **P6** in `exercises/python-basics/p06_for_loops.py`: study the worked example (range,
for-loops, accumulator, looping over a string), run it, then solve the 4 problems. Say `REVIEW`
when done. (P1–P5 ✅.)

---
### Session log
| Date | Session # | Focus | Evidence produced | Minutes |
|------|-----------|-------|-------------------|---------|
| 2026-10-11 | 1 | Day 1 — computer basics & execution chain | day01_hello.py (int vs str), day01_bug.py (fixed NameError), quiz Q1–Q5, teach-back in own words | ~120 |
| 2026-10-19 | 2 | Day 2 — bits & binary; started Project #1 | converter.py (both functions pass), day02_bug.py (logic-bug fix), quiz, teach-back; corrections: 2⁸=256, bin() `0b` prefix | ~120 |
