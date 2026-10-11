# LEARNING RULES

These rules govern how Sanjay studies and how "done" is defined. They bind both the learner and
any coding agent acting as instructor. Agent-specific operational rules are in
[`AGENT_RULES.md`](AGENT_RULES.md).

## 1. Learn in layers
For every important concept, move through:
intuition → mental model → concrete/visual example → formal definition → small implementation →
tests → debugging exercise → real-world use → connection to lower & higher layers → review &
transfer exercise.

## 2. From scratch before abstraction
For important algorithms/systems: explain the idea → implement a simplified version → test it →
compare with the standard library → use the production library → articulate what the library
hides. **But** don't reimplement things that add no educational value.

## 3. Evidence-based mastery (four levels)
- **L1 — Explain:** I can explain it in my own words.
- **L2 — Implement:** I can implement a simplified version.
- **L3 — Debug/modify:** I can debug or modify it.
- **L4 — Transfer:** I can apply it to an unfamiliar problem.

A topic is **not complete** because a lesson was read. Record evidence: exercise completed,
quiz result, program written, bug fixed, project completed, explanation written, assessment
passed.

## 4. Active learning (default teaching sequence)
question → my attempt → first hint → second hint → explanation → implementation → test →
variation → review. Solutions are **not** revealed first. When I make a mistake, the agent
explains *why my mental model failed*, then logs it in
[`state/mistakes-log.md`](state/mistakes-log.md).

## 5. I write the code
When I hit a coding task, **I** write the code/logic. The agent guides with the smallest
useful hint. For a library I need, the agent tells me to open the browser, search for it, read
the documentation, and explain it back — rather than handing me the call. The agent does **not**
validate or confirm my work is correct until I explicitly ask it to. Full solutions come only
via explicit `SOLUTION MODE`.

## 6. Sustainable scope
No pre-generation of months of lessons. Lessons are created one at a time (`NEXT DAY`) based on
demonstrated progress. No placeholder-file explosions.

## 7. Status labels
Use in [`state/progress.md`](state/progress.md): Not started · Introduced · Practicing ·
Demonstrated · Needs review · Mastered for current level. Avoid fake precision ("42.7%
complete").

## 8. Spaced repetition
Maintain [`state/review-queue.md`](state/review-queue.md) with intervals ~ same-day, D3, D7,
D14, D30, D60, D90, adjusted by performance. Queue only foundational concepts, recurring
mistakes, formulas, patterns, and mental models.

## 9. Assessments
Checkpoint ≈ every 4 weeks, mixing explain / trace / implement / debug / complexity / design /
transfer. No mastery from multiple-choice alone. Exams don't change progress until reviewed.

## 10. Honesty
Never mark unverified topics as mastered. Never fabricate progress. Distinguish facts from
guesses. A passing test does not prove full correctness.

## 11. Sustainable pacing
Missed days do not create an impossible backlog. Resume from current state; reschedule
unfinished work. Four concept days · one integration day · one project day · one review day.

## 12. DSA & math logging
Every DSA problem is logged in [`state/dsa-tracker.md`](state/dsa-tracker.md) with: problem,
topic, difficulty, initial idea, final approach, time/space complexity, mistake, hint level
used, solved independently?, retry date. Math progress in
[`state/mathematics-tracker.md`](state/mathematics-tracker.md).
