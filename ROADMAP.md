# ROADMAP — Computer Science → AI/ML Engineer (≈2–3 years)

This is the full dependency-ordered progression. Durations assume ~12–14 hrs/week and are
**ranges, not promises** — you advance on demonstrated evidence (see
[`MILESTONES.md`](MILESTONES.md)), not on the calendar.

## How phases relate

Each phase assumes the one before it. Mathematics and DSA run as **parallel threads**
alongside the systems/AI track rather than as isolated blocks, because later phases depend on
them continuously. The ordering below is the *spine*; the parallel threads are called out per
phase.

```
P0 method ─ P1 systems ─ P2 languages/tools ─ P3 DSA+math ─ P4 OS/net/db
   └─ P5 software eng ─ P6 distributed/cloud/data ─ P7 classical ML
      └─ P8 deep learning ─ P9 transformers/LLMs ─ P10 RAG/AI eng
         └─ P11 agents/MCP/computer-use ─ P12 MLOps/security/research
```

Detailed per-phase files live in [`curriculum/phases/`](curriculum/phases/).

---

## Phase 0 — Learning method & environment  (~1–2 weeks)
- **Goal:** install a durable learning system and a working toolchain.
- **Prerequisites:** none.
- **Core topics:** active recall, spaced repetition, deliberate practice, Feynman technique,
  interleaving; PowerShell basics, VS Code, Python + venv, Git init.
- **Deliverables:** this repo in active use; first entries in all trackers; Day 1–7 complete.
- **Exit criteria:** you run a 2-hr session unaided, record evidence, and manage your review
  queue.
- **Common mistakes:** passive re-reading; skipping the trackers.
- **Next:** method in place → start building the mental stack in P1.
- Detail: [`phase-00-learning-method.md`](curriculum/phases/phase-00-learning-method.md)

## Phase 1 — Computer systems foundations  (~6–10 weeks)
- **Goal:** understand what a computer *is*, bottom-up.
- **Prerequisites:** P0.
- **Core topics:** bits/bytes, binary, hex, two's complement, floating point, char encodings;
  boolean algebra, logic gates, combinational & sequential circuits, adders, flip-flops,
  registers; ALU, control unit, CPU, memory hierarchy, cache; ISA, machine code, assembly,
  fetch-decode-execute, interrupts, I/O, buses; stack/heap, virtual memory, system calls.
- **Math thread:** number bases, boolean algebra. **DSA thread:** none yet (warm-up only).
- **Labs/from-scratch:** number-system converter; logic-gate simulator; small instruction
  emulator (Nand2Tetris-style).
- **Major project:** tiny CPU / instruction-set emulator.
- **Resources:** Nand2Tetris, CS:APP (selectively), Crafting the stack conceptually.
- **Exit criteria:** trace a value from binary through gates to a CPU register; explain
  fetch-decode-execute; implement an adder and a mini-emulator.
- **Next:** hardware model in place → learn the languages that drive it (P2).
- Detail: [`phase-01-computer-systems.md`](curriculum/phases/phase-01-computer-systems.md)

## Phase 2 — Programming, C, Git, shell, testing  (~8–12 weeks)
- **Goal:** fluency in Python + enough C to see the metal; professional tooling.
- **Prerequisites:** P1.
- **Core topics:** Python deeply (types, references/mutability, functions/scope, recursion,
  modules/packages, venv, exceptions, OOP, iterators/generators, comprehensions, decorators,
  context managers, type hints, dataclasses, testing, debugging, logging, profiling, threads/
  processes/async, packaging); C (compilation, linking, pointers, structs, stack/heap,
  memory errors, segfaults, debugging); PowerShell & CLI; Git (commits, branches, merges,
  rebase concepts, PRs, diffs); debuggers.
- **Math thread:** functions, logs/exponents. **DSA thread:** complexity, arrays, strings.
- **Labs/from-scratch:** CLI utility; C memory experiments; test suites with pytest.
- **Major project:** mini shell (reads commands, runs processes, pipes).
- **Exit criteria:** write idiomatic tested Python; explain a segfault; drive Git confidently.
- **Next:** can code → formalize problem-solving in P3.
- Detail: [`phase-02-programming.md`](curriculum/phases/phase-02-programming.md)

## Phase 3 — Data structures, algorithms & math foundations  (~12–16 weeks)
- **Goal:** solve problems with the right structure; build the math spine for ML.
- **Prerequisites:** P2.
- **Core topics (DSA):** Big-O/Θ/Ω; arrays, linked lists, stacks, queues, deques, hash tables,
  sets; recursion, binary search, sorting; trees, BSTs, balanced-tree concepts, heaps/priority
  queues, tries; graphs, BFS/DFS, union-find, topological sort, shortest paths, MST; patterns:
  two pointers, sliding window, prefix sums, monotonic stack, greedy, backtracking, D&C, DP,
  bit manipulation.
- **Core topics (math):** linear algebra (vectors, matrices, dot products, matmul, linear
  transforms, basis, eigen-intuition); probability (conditional, Bayes, random variables,
  distributions, expectation/variance/covariance); statistics (descriptive, inferential,
  hypothesis-testing intuition); calculus (limits, derivatives, partials, gradients, chain
  rule, optimization, gradient descent, convexity); information theory (entropy, cross-entropy,
  KL).
- **Labs/from-scratch:** data-structures library; algorithm visualizer; math-in-code notebooks.
- **Major project:** data-structures library + algorithm visualizer.
- **Exit criteria:** pick/justify a structure, analyze complexity, implement gradient descent
  by hand; every math idea connected to computing/ML.
- **Next:** problem-solving + math ready → learn the systems programs run on (P4).
- Detail: [`phase-03-dsa.md`](curriculum/phases/phase-03-dsa.md) ·
  [`phase-04-mathematics.md`](curriculum/phases/phase-04-mathematics.md)

## Phase 4 — Operating systems, networking, databases  (~10–14 weeks)
- **Goal:** understand the environment software runs inside and talks across.
- **Prerequisites:** P2 (P3 in parallel).
- **Core topics:** OS (kernel/user space, processes/threads, scheduling, context switches,
  concurrency, locks/semaphores, deadlocks, race conditions, virtual memory/paging, files,
  permissions, syscalls, signals, IPC, containers vs VMs); networking (layers, TCP/IP,
  DNS, ports, sockets, TCP/UDP, HTTP/HTTPS/TLS, REST, WebSockets, proxies, load balancers,
  auth/authz, tokens/OAuth, retries/timeouts/idempotency/rate limits); databases (SQL, joins,
  aggregation, window functions, normalization, keys, indexes, B-trees, query planning,
  transactions/ACID, isolation levels, replication, partitioning, NoSQL, caching, vector DBs).
- **Labs/from-scratch:** HTTP client & server; concurrent task processor; key-value store.
- **Major project:** HTTP server + small relational application, or a key-value store.
- **Exit criteria:** explain a context switch, a TCP handshake, and an index; build a server.
- **Next:** know the platform → engineer real software on it (P5).
- Detail: [`phase-05-core-software-systems.md`](curriculum/phases/phase-05-core-software-systems.md)

## Phase 5 — Software engineering & system design  (~8–12 weeks)
- **Goal:** write maintainable systems and reason about design trade-offs.
- **Prerequisites:** P2, P4.
- **Core topics:** requirements/decomposition, clean code, coupling/cohesion, OOP + SOLID as
  guidance, design patterns, refactoring; testing (unit/integration/e2e, doubles, property-
  based concepts); error handling, logging, config, docs, code review, CI/CD, versioning,
  dependency management, security fundamentals; backend (APIs, services, auth, background jobs,
  queues, caches, storage); system design (scaling, load balancing, rate limiting, HA,
  observability, fault tolerance, capacity estimation, trade-offs).
- **Major project:** a REST API backed by a database, with tests, CI, and observability.
- **Exit criteria:** design a small service end-to-end and defend the trade-offs.
- **Next:** single-node mastery → scale out in P6.
- Detail: [`phase-06-software-engineering.md`](curriculum/phases/phase-06-software-engineering.md)

## Phase 6 — Distributed systems, cloud & data engineering  (~8–12 weeks)
- **Goal:** reason about systems that fail partially and span machines; move data at scale.
- **Prerequisites:** P4, P5.
- **Core topics:** distributed failure modes, latency, partial failure, consistency/
  availability, CAP, replication/partitioning, consensus intuition, message queues, pub/sub,
  event-driven systems, delivery semantics, idempotency, retries/backoff, distributed locks,
  sagas, eventual consistency, clocks/ordering, observability; cloud/DevOps (Linux, VMs,
  Docker, images/registries, volumes, Kubernetes basics, CI/CD, secrets, IaC concepts, managed
  services, serverless, monitoring, cost); data engineering (NumPy, Pandas, SQL, cleaning/
  validation, ETL/ELT, batch/streaming, pipelines, orchestration, warehouses/lakes/lakehouses,
  columnar formats, partitioning, Spark basics, quality, lineage, feature pipelines).
- **Major project:** queue-based distributed-system experiment + an ETL pipeline.
- **Exit criteria:** explain CAP with a concrete scenario; build a resilient pipeline.
- **Next:** data + infrastructure ready → start learning *from* data (P7).
- Detail: [`phase-07-data-and-distributed-systems.md`](curriculum/phases/phase-07-data-and-distributed-systems.md)

## Phase 7 — Classical machine learning  (~10–14 weeks)
- **Goal:** understand learning from data from first principles.
- **Prerequisites:** P3 (math), P6 (data).
- **Core topics:** what learning means; supervised/unsupervised; train/val/test, data leakage;
  regression (linear, logistic), KNN, naive Bayes, decision trees, random forests, gradient
  boosting, SVM concepts; clustering (k-means), PCA; feature engineering, preprocessing,
  missing data, class imbalance; loss functions, optimization, regularization, bias/variance,
  cross-validation, metrics, calibration, hyperparameter tuning, explainability, baselines,
  experiment design.
- **From-scratch:** linear regression, logistic regression, decision tree — in NumPy, before
  scikit-learn.
- **Major project:** end-to-end ML project with a proper evaluation harness.
- **Exit criteria:** implement 3 algorithms from scratch; diagnose over/underfitting.
- **Next:** classical ML → scale representations with neural nets (P8).
- Detail: [`phase-08-machine-learning.md`](curriculum/phases/phase-08-machine-learning.md)

## Phase 8 — Deep learning & PyTorch  (~10–14 weeks)
- **Goal:** build and train neural networks; understand backprop deeply.
- **Prerequisites:** P7, calculus/linear-algebra thread.
- **Core topics:** perceptrons, layers, tensors, forward prop, losses, backprop, computational
  graphs, SGD/momentum/Adam, activations, initialization, normalization, regularization,
  dropout; CNNs, RNNs, LSTMs, sequence modeling, attention intro; PyTorch, GPU basics, training
  loops, checkpointing, evaluation, debugging training.
- **From-scratch:** NumPy neural network; a small autograd engine (micrograd-style); matching
  PyTorch version.
- **Major project:** a PyTorch image or text model trained end-to-end.
- **Exit criteria:** derive and implement backprop; debug a non-training model.
- **Next:** neural nets + attention intro → go deep on transformers (P9).
- Detail: [`phase-09-deep-learning.md`](curriculum/phases/phase-09-deep-learning.md)

## Phase 9 — NLP, attention, transformers & LLM internals  (~12–16 weeks)
- **Goal:** understand transformers and LLMs from the inside.
- **Prerequisites:** P8.
- **Core topics:** tokenization, vocab, embeddings, positional info; Q/K/V, scaled dot-product
  attention, self-attention, multi-head, causal masks; feed-forward, residuals, normalization;
  encoder/decoder/enc-dec; autoregressive generation; pretraining, fine-tuning, instruction
  tuning, RLHF/DPO concepts; sampling (greedy, beam, temperature, top-k, top-p); context
  windows, KV cache, batching, quantization, LoRA/PEFT, inference, serving, evaluation,
  hallucination, safety limits.
- **From-scratch (progressive):** char-level model → attention → transformer block → tiny GPT
  → train & generate (nanoGPT-style).
- **Major project:** a tiny GPT trained on a small corpus, with a generation experiment.
- **Exit criteria:** implement self-attention and a transformer block from scratch; explain
  the KV cache.
- **Next:** understand LLMs → use them in real systems (P10).
- Detail: [`phase-10-transformers-and-llms.md`](curriculum/phases/phase-10-transformers-and-llms.md)

## Phase 10 — RAG & production AI engineering  (~8–12 weeks)
- **Goal:** build grounded, reliable LLM applications.
- **Prerequisites:** P9.
- **Core topics:** full RAG pipeline (ingest → parse → clean → chunk → metadata → embed →
  index → retrieve → rerank → context → generate → cite → evaluate); sparse (BM25)/dense/
  hybrid retrieval, vector indexes, metadata filtering, chunking strategies, query
  transformation, grounded generation, retrieval & answer evaluation, RAG failure modes & 
  security; AI engineering (model APIs, open-weight models, structured outputs, function
  calling, prompt construction/versioning, routing, caching, retries, validation, guardrails,
  evaluation, tracing, observability, latency/cost, fallbacks, human approval, production
  architecture).
- **From-scratch:** simple retrieval + embedding search before any RAG framework.
- **Major project:** a RAG system with an evaluation harness and citations.
- **Exit criteria:** build RAG without hiding the pipeline; measure retrieval quality.
- **Next:** grounded apps → give them tools and autonomy (P11).
- Detail: [`phase-11-ai-engineering.md`](curriculum/phases/phase-11-ai-engineering.md)

## Phase 11 — Tool calling, MCP, agents, browser & computer use  (~12–16 weeks)
- **Goal:** build tool-using agents safely, including browser/computer-use and coding agents.
- **Prerequisites:** P10.
- **Core topics:** the agent loop (goal → state → plan → tool select → execute → observe →
  update → next → respond); workflows vs agents; tool calling, state, memory, planning,
  reflection, retries, error recovery, human-in-the-loop, permissions, multi-agent, agent
  evaluation, excessive-agency risk; MCP (client/server, tool discovery, schemas, resources,
  auth/authz, validation, errors, security boundaries, observability); browser/computer use
  (HTML/DOM/CSS selectors, accessibility trees, Playwright, screenshots, CV/OCR concepts,
  mouse/keyboard automation, OS APIs, sandboxes/containers/VMs, credentials, sessions, prompt
  injection — direct & indirect, audit logs, recovery); coding agents (indexing, search,
  context selection, planning, patch generation, terminal/test feedback, diffs, rollback).
- **From-scratch:** minimal agent loop → MCP server/client → browser automation agent →
  sandboxed computer-use agent → simplified coding agent.
- **Major project:** a simplified coding agent that reads a repo, edits, runs tests, retries,
  and produces a diff + report.
- **Safety:** all browser/computer-use/coding-agent work starts in local sandboxes with
  disposable data and explicit approval gates. See [`AGENT_RULES.md`](AGENT_RULES.md) §Safety.
- **Exit criteria:** build an agent loop from scratch; explain & mitigate prompt injection.
- **Next:** working agents → operate them in production and study the field (P12).
- Detail: [`phase-12-agents-and-computer-use.md`](curriculum/phases/phase-12-agents-and-computer-use.md)

## Phase 12 — MLOps, LLMOps, security, multimodal, RL & research  (~ongoing)
- **Goal:** run AI systems reliably, securely, responsibly; read and reproduce research.
- **Prerequisites:** P10–P11.
- **Core topics:** MLOps/LLMOps (experiment/dataset/model versioning, registries, packaging,
  serving, batch/online inference, CI/CD, monitoring, drift, LLM/prompt evaluation, tracing,
  latency/throughput/batching, GPU utilization, caching, cost, rollbacks, A/B, incident
  response); security & responsible AI (authn/authz, least privilege, secrets, encryption,
  dependency/supply-chain risk, input validation, privacy/PII, prompt injection, tool abuse,
  exfiltration, excessive agency, RAG poisoning, sandboxing, audit logs, bias/fairness);
  reinforcement learning (MDP, value/policy, Bellman, exploration/exploitation, bandits,
  Q-learning, policy gradients, deep RL, alignment link); multimodal (image embeddings, ViT,
  contrastive learning, VLMs, speech/audio, diffusion, multimodal agents); research skills
  (reading papers, reproducing baselines, experiment design, ablations, benchmark literacy,
  technical writing).
- **Major project:** a production AI service, then an end-to-end AI platform capstone; plus a
  reproduced research paper.
- **Exit criteria:** reproduce a paper baseline; deploy and monitor a service; threat-model an
  agent.
- Detail: [`phase-13-production-and-research.md`](curriculum/phases/phase-13-production-and-research.md)

---

See [`CONCEPT_MAP.md`](CONCEPT_MAP.md) for how specific concepts depend on each other, and
[`PROJECTS.md`](PROJECTS.md) for the 36-step project ladder that threads through these phases.
