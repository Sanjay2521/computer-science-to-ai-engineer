# Progress

> Authoritative current position. The agent reads this at the start of every session and updates
> it with **evidence**. Status labels: Not started · Introduced · Practicing · Demonstrated ·
> Needs review · Mastered for current level. Avoid fake precision.

## Current position
- **Phase:** 0 — Learning method & environment
- **Module:** [00 — Learning how to learn](../modules/00-learning-how-to-learn/)
- **Week:** 1 (see [week-01](../curriculum/week-01.md))
- **Lesson:** Day 2 — bits & binary — ✅ **Demonstrated** (2026-10-19) · Day 3 (hexadecimal) next
- **Start date:** 2026-10-11
- **Current project:** #1 Number-system converter — decimal↔binary done; hex next (Day 3)
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
👉 Work through [`../lessons/day-003.md`](../lessons/day-003.md) (hexadecimal + extend the
converter). Small carry-over: finish the Exercise C note from Day 2 (bin()/int(s,2)) and delete the
two leftover `...` lines in converter.py.

---
### Session log
| Date | Session # | Focus | Evidence produced | Minutes |
|------|-----------|-------|-------------------|---------|
| 2026-10-11 | 1 | Day 1 — computer basics & execution chain | day01_hello.py (int vs str), day01_bug.py (fixed NameError), quiz Q1–Q5, teach-back in own words | ~120 |
| 2026-10-19 | 2 | Day 2 — bits & binary; started Project #1 | converter.py (both functions pass), day02_bug.py (logic-bug fix), quiz, teach-back; corrections: 2⁸=256, bin() `0b` prefix | ~120 |
