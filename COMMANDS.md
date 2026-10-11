# COMMANDS

Commands you can give your coding agent while studying. Type them in plain language; the agent
follows the behavior defined here and in [`AGENT_RULES.md`](AGENT_RULES.md).

## Teaching modes

| Command | What the agent does |
|---------|---------------------|
| `TEACH <topic>` | Teach interactively. Questions, examples, hints, checks for understanding. **Does not** reveal the final solution upfront. |
| `HINT` | Give only the smallest useful hint. No full solution. |
| `REVIEW` | Review my work: correct parts, bugs, weak reasoning, missing tests, complexity & maintainability concerns. Does not rewrite everything unless necessary. |
| `DEBUG` | Guide me through debugging. Ask for my hypothesis, help inspect evidence, explain the root cause **after** the investigation. |
| `SOLUTION` | Give a complete solution with explanation, tests, complexity, and alternatives. **Only when I explicitly ask.** |
| `BUILD` | Act as an engineering agent: implement the feature, run tests, inspect failures, give a diff-oriented summary. **Not** applied automatically to learning exercises. |
| `QUIZ` | Test understanding without showing answers first. Conceptual + tracing + debugging + application questions. |
| `EXAM` | Create a timed checkpoint. Does not change progress until the assessment is reviewed. |
| `REVISE` | Pull due items from [`state/review-queue.md`](state/review-queue.md) and run active recall. |

## Progression & bookkeeping

| Command | What the agent does |
|---------|---------------------|
| `NEXT DAY` | Read current progress and generate **only** the next appropriate lesson. Never skips prerequisites. |
| `SYNC PROGRESS` | Update trackers from demonstrated evidence. Never marks unverified topics mastered. |
| `WHERE AM I` | Summarize current phase / week / lesson / project and the next recommended action. |
| `LOG MISTAKE` | Record a mistake in [`state/mistakes-log.md`](state/mistakes-log.md) with the correct mental model. |
| `LOG PROBLEM` | Record a DSA problem in [`state/dsa-tracker.md`](state/dsa-tracker.md). |

## Working style reminder
Default is **guide, don't solve**: I write the code; the agent hints and points me to docs; it
does **not** validate my work until I ask. `SOLUTION` and `BUILD` are the explicit opt-outs.

## Example session
```
WHERE AM I
TEACH two's complement
<I attempt the exercise>
HINT
<I attempt again>
REVIEW            ← only after I say I'm ready
QUIZ
SYNC PROGRESS
```
