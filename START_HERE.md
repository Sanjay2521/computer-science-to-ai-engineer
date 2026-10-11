# START HERE

Welcome, Sanjay. This is your starting sequence. Do it once, in order. It takes ~15 minutes
before you reach Day 1 proper.

## The seven steps

1. **Read your learner profile** → [`state/learner-profile.md`](state/learner-profile.md)
   Confirm it still describes you. Edit anything that has changed.

2. **Read the learning rules** → [`LEARNING_RULES.md`](LEARNING_RULES.md)
   These govern how you study and how "done" is defined. The most important one: *evidence,
   not reading, equals mastery.*

3. **Skim Week 1** → [`curriculum/week-01.md`](curriculum/week-01.md)
   See where the week is going. Don't study ahead — just orient.

4. **Open Day 1** → [`lessons/day-001.md`](lessons/day-001.md)
   This is a complete ~2-hour lesson. Work through it top to bottom.

5. **Do the exercises** inside Day 1. Write your own code in
   [`exercises/`](exercises/). Don't look up solutions first — attempt, then hint.

6. **Record your results** → update [`state/progress.md`](state/progress.md) with what you
   completed and the evidence (code written, quiz score, teach-back done).

7. **Update the review queue** → add Day 1's core concepts to
   [`state/review-queue.md`](state/review-queue.md) with their first review dates.

## Daily rhythm (foundation phase, ~2 hrs)

| Time | Activity |
|------|----------|
| 10 min | Active recall warm-up (yesterday + a due review item) |
| 30 min | New concept |
| 55 min | Coding / lab |
| 20 min | DSA or mathematics (alternating days) |
| 5 min  | Reflection + update `state/progress.md` |

## Weekly rhythm

4 concept-and-practice days · 1 integration day · 1 project day · 1 review & recovery day.

Missed a day? Don't build a backlog. Resume from the current state; the agent reschedules
unfinished work.

## Driving this with your agent

Tell your coding agent things like:
- `NEXT DAY` — generate the next appropriate lesson (only when Day 1 is done).
- `TEACH <topic>` — teach me interactively.
- `HINT` — smallest useful nudge, no solution.
- `REVIEW` — review the code I wrote.
- `QUIZ` — test me without showing answers first.
- `REVISE` — run due items from my review queue.

Full list: [`COMMANDS.md`](COMMANDS.md).

---

**Your first action:** open [`lessons/day-001.md`](lessons/day-001.md) and do the 10-minute
warm-up at the top.
