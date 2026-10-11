# CURRICULUM — Central Index

This is the map of the whole program. [`ROADMAP.md`](ROADMAP.md) gives the phase-by-phase
progression; this file explains the *philosophy, dependencies, and systems* that hold it
together.

## Curriculum philosophy

1. **Understand beneath the abstraction.** For every important concept, ask the nine questions
   (see below) before using a library.
2. **Depth over coverage.** It is better to deeply understand backprop than to skim ten models.
3. **Build it, then use it.** Implement a simplified version from scratch, test it, compare it
   to the production library, then use the library and articulate what it hides.
4. **Evidence over exposure.** Reading a lesson is not learning. Code, quizzes, bug fixes, and
   teach-backs are.
5. **Sustainable, not front-loaded.** Lessons are generated as you progress, not pre-written.

### The nine questions (apply to every major concept)
1. What problem does it solve?
2. What is beneath the abstraction?
3. How does it work internally?
4. Why was it designed this way?
5. What assumptions does it make?
6. What can fail?
7. How do I debug it?
8. Can I implement a simplified version?
9. How does it connect to the next layer?

## Dependency order

The spine is linear (P0→P12) but two threads run **in parallel** from P2 onward:

- **DSA thread** — starts in P2 (complexity, arrays), deepens through P3, stays warm
  afterward via the review queue and periodic problems.
- **Mathematics thread** — starts in P2 (functions/logs), core block in P3, then applied
  continuously in P7–P9.

```
Binary → boolean logic → gates → adders/registers → CPU → machine instr → assembly → OS → languages
Memory → arrays → data structures → algorithms → databases → model tensors
Linear algebra → vectors → embeddings → attention → transformers → LLMs
Networking → HTTP → APIs → tool calling → MCP → agents
OS → processes → permissions → sandboxes → computer-use agents
Statistics → loss functions → evaluation → ML → model monitoring
```
Full graph: [`CONCEPT_MAP.md`](CONCEPT_MAP.md).

## Phase links

| Phase | File | Module |
|-------|------|--------|
| 0 Method | [phase-00](curriculum/phases/phase-00-learning-method.md) | [00](modules/00-learning-how-to-learn/) |
| 1 Systems | [phase-01](curriculum/phases/phase-01-computer-systems.md) | [01](modules/01-computer-systems/) |
| 2 Programming | [phase-02](curriculum/phases/phase-02-programming.md) | [02](modules/02-programming/) |
| 3 DSA | [phase-03](curriculum/phases/phase-03-dsa.md) | [03](modules/03-data-structures-and-algorithms/) |
| 4 Mathematics | [phase-04](curriculum/phases/phase-04-mathematics.md) | [04](modules/04-mathematics/) |
| 5 Core systems | [phase-05](curriculum/phases/phase-05-core-software-systems.md) | [05](modules/05-os-networking-databases/) |
| 6 Software eng | [phase-06](curriculum/phases/phase-06-software-engineering.md) | [06](modules/06-software-and-backend-engineering/) |
| 7 Dist/data | [phase-07](curriculum/phases/phase-07-data-and-distributed-systems.md) | [07](modules/07-distributed-cloud-and-data-engineering/) |
| 8 ML | [phase-08](curriculum/phases/phase-08-machine-learning.md) | [08](modules/08-machine-learning/) |
| 9 DL | [phase-09](curriculum/phases/phase-09-deep-learning.md) | [09](modules/09-deep-learning/) |
| 10 Transformers/LLMs | [phase-10](curriculum/phases/phase-10-transformers-and-llms.md) | [10](modules/10-transformers-and-llms/) |
| 11 AI engineering | [phase-11](curriculum/phases/phase-11-ai-engineering.md) | [11](modules/11-rag-and-ai-engineering/) |
| 12 Agents/MCP | [phase-12](curriculum/phases/phase-12-agents-and-computer-use.md) | [12](modules/12-agents-mcp-and-computer-use/) |
| 13 Production/research | [phase-13](curriculum/phases/phase-13-production-and-research.md) | [13](modules/13-mlops-security-and-research/) |

> Note: the 14 phase files map onto the 13 subject modules — DSA (P3) and Mathematics (P4 file)
> are the two parallel threads that share the early timeline. The ROADMAP numbers phases by
> *timeline*; the phase files number by *subject*. Both are cross-linked.

## Project progression

A 36-step ladder runs through the phases, from a number-system converter to an end-to-end AI
platform capstone. Each project validates one or more layers. See [`PROJECTS.md`](PROJECTS.md).

## Assessment model

- **Four mastery levels:** (1) explain in own words, (2) implement a simplified version,
  (3) debug/modify, (4) apply to an unfamiliar problem.
- **Checkpoint assessments ≈ every 4 weeks** mixing explain / trace / implement / debug /
  complexity / design / transfer questions. No topic is "mastered" on multiple-choice alone.
- **Status labels** (in [`state/progress.md`](state/progress.md)): Not started · Introduced ·
  Practicing · Demonstrated · Needs review · Mastered for current level.
- Rules in full: [`LEARNING_RULES.md`](LEARNING_RULES.md).

## Review strategy

Spaced repetition in [`state/review-queue.md`](state/review-queue.md): same day, D3, D7, D14,
D30, D60, D90, adjusted by performance. Only foundational concepts, recurring mistakes,
formulas, patterns, and mental models enter the queue — not every fact.

## Where things live

- Curriculum detail → [`curriculum/`](curriculum/)
- Subject overviews & exit criteria → [`modules/`](modules/)
- Daily lessons (generated one at a time) → [`lessons/`](lessons/)
- Your living state → [`state/`](state/)
- Your code → [`exercises/`](exercises/), [`labs/`](labs/), [`projects/`](projects/)
