# Year 1 Curriculum

The first year builds **foundations** before rushing into AI frameworks. It covers Phases 0–9
at an introductory-to-intermediate depth, with DSA and mathematics running as parallel threads
throughout. Later years deepen ML/DL/LLMs and reach agents, MCP, computer use, MLOps, and
research.

> Durations are targets at ~12–14 hrs/week, not promises. Advance on evidence
> ([`../MILESTONES.md`](../MILESTONES.md)).

## Year 1 shape

| Months | Main objective | Maps to phases |
|--------|----------------|----------------|
| 1–2 | Computer fundamentals, Python, C, command line, Git | 0, 1 (start), 2 |
| 3–4 | DSA, mathematics, debugging, operating systems | 3, 4 (OS) |
| 5–6 | Networking, databases, backend engineering, testing | 4, 5 |
| 7–8 | Data engineering and classical machine learning | 6, 7 |
| 9–10 | Deep learning and PyTorch | 8 |
| 11–12 | NLP, attention, transformers, intro LLM engineering | 9 |

---

## Month 1 — Computer fundamentals + Python start
- **Objective:** understand what a computer is and start writing real Python.
- **Topics:** bits/binary/hex, two's complement, hardware vs software, the execution chain;
  Python syntax, types, variables/references, control flow, functions, modules, venv.
- **Weekly focus:** W1 computers & binary · W2 Python basics · W3 functions/modules/venv ·
  W4 files/exceptions + review + checkpoint.
- **DSA focus:** complexity intuition; arrays & strings.
- **Math focus:** number bases; functions; logs/exponents.
- **Labs:** number-system converter (project #1); small Python scripts.
- **Project:** #1 Number-system converter.
- **Assessment:** W4 checkpoint (explain execution chain; trace a Python program).
- **Exit criteria:** convert between bases by hand; write & run a small Python program;
  explain source→output.

## Month 2 — Python depth + C + Git/CLI
- **Objective:** Python OOP & idioms; see the metal with C; professional tooling.
- **Topics:** OOP, iterators/generators, comprehensions, decorators, context managers, type
  hints, dataclasses, testing (pytest), debugging, logging; C: compilation, pointers, structs,
  stack/heap, segfaults; PowerShell, Git branches/merges/diffs.
- **DSA focus:** linked lists, stacks, queues; two pointers.
- **Math focus:** sequences & summations.
- **Labs:** C memory experiments (project #4); CLI utility (project #5).
- **Project:** #5 Command-line utility; begin #6 mini shell.
- **Assessment:** explain a segfault; write a tested Python module.
- **Exit criteria:** idiomatic tested Python; drive Git; explain pointers/segfault.

## Month 3 — DSA core + OS start
- **Objective:** core data structures & algorithms; how the OS runs programs.
- **Topics:** hash tables/sets, recursion, binary search, sorting, trees/BST, heaps; OS:
  processes/threads, scheduling, memory/paging, syscalls.
- **DSA focus:** sliding window, prefix sums, binary search, sorting, trees.
- **Math focus:** linear algebra start — vectors, dot products.
- **Labs:** data-structures library (project #7).
- **Project:** #7 Data-structures library.
- **Assessment:** analyze complexity; implement a BST; explain a context switch.
- **Exit criteria:** choose/justify a structure; implement core structures from scratch.

## Month 4 — Algorithms + math spine
- **Objective:** graph algorithms, DP; the math that ML needs.
- **Topics:** graphs (BFS/DFS, shortest paths, topo sort, union-find), greedy, backtracking,
  divide & conquer, dynamic programming; linear algebra (matrices, matmul, transforms);
  calculus (derivatives, gradients, chain rule), gradient descent.
- **DSA focus:** graphs, DP.
- **Math focus:** matrices/matmul; derivatives/gradients; gradient descent.
- **Labs:** algorithm visualizer (project #8); gradient descent from scratch (notebook).
- **Project:** #8 Algorithm visualizer.
- **Assessment:** implement BFS/DFS + one DP; implement gradient descent by hand.
- **Exit criteria:** solve medium graph/DP problems; connect calculus to optimization.

## Month 5 — Networking + databases
- **Objective:** how programs talk and persist.
- **Topics:** TCP/IP, DNS, sockets, HTTP/HTTPS/TLS, REST; SQL, joins, indexes/B-trees,
  transactions/ACID, isolation.
- **DSA focus:** review via problems; tries.
- **Math focus:** probability start — conditional probability, Bayes.
- **Labs:** HTTP client & server (project #9); key-value store (project #12).
- **Project:** #9 HTTP client/server.
- **Assessment:** explain a TCP handshake and a DB index; build a tiny server.
- **Exit criteria:** build client/server; write non-trivial SQL; explain transactions.

## Month 6 — Backend engineering + testing
- **Objective:** build a maintainable service with real engineering practices.
- **Topics:** API design, services, auth/authz, background jobs, queues, caches; clean code,
  refactoring, test doubles, integration tests, CI, logging, config.
- **DSA focus:** mixed review problems.
- **Math focus:** random variables, distributions, expectation/variance.
- **Labs:** REST API (project #10); small relational app (project #11).
- **Project:** #10 REST API with DB + tests + CI.
- **Assessment:** design a small service; defend trade-offs.
- **Exit criteria:** ship a tested, documented API.

## Month 7 — Data engineering
- **Objective:** move and clean data reliably.
- **Topics:** NumPy, Pandas, SQL at scale, cleaning/validation, ETL/ELT, pipelines, batch vs
  streaming, columnar formats; intro to containers (Docker).
- **DSA focus:** light; keep review queue warm.
- **Math focus:** descriptive & inferential statistics.
- **Labs:** ETL pipeline (project #15).
- **Project:** #15 ETL pipeline.
- **Assessment:** build a validated pipeline; reason about data quality.
- **Exit criteria:** clean/transform a dataset end-to-end with checks.

## Month 8 — Classical machine learning
- **Objective:** learn from data, from first principles.
- **Topics:** supervised/unsupervised, train/val/test, leakage; linear & logistic regression,
  KNN, decision trees; loss, regularization, bias/variance, cross-validation, metrics.
- **DSA/Math:** optimization review; covariance; information theory (entropy, cross-entropy).
- **Labs:** linear & logistic regression from scratch (projects #16–17); decision tree (#18).
- **Project:** #19 ML evaluation project.
- **Assessment:** implement 3 algorithms from scratch; diagnose over/underfitting.
- **Exit criteria:** build a leak-free ML pipeline with honest evaluation.

## Month 9 — Deep learning foundations
- **Objective:** neural networks and backprop, deeply.
- **Topics:** perceptrons, layers, tensors, forward prop, losses, backprop, computational
  graphs, SGD/momentum/Adam, activations, initialization, regularization.
- **Math focus:** chain rule applied to backprop.
- **Labs:** NumPy neural network (project #20); autograd engine (project #21).
- **Project:** #21 Small autograd engine (micrograd-style).
- **Assessment:** derive and implement backprop.
- **Exit criteria:** train a net you built from scratch; explain every gradient.

## Month 10 — PyTorch
- **Objective:** real deep learning with a framework — understanding what it hides.
- **Topics:** PyTorch tensors/autograd, training loops, datasets/dataloaders, GPU basics,
  checkpointing, evaluation, debugging training; CNNs, RNNs/LSTMs intro.
- **Labs:** PyTorch model (project #22).
- **Project:** #22 PyTorch image or text model.
- **Assessment:** debug a non-training model; reproduce your NumPy net in PyTorch.
- **Exit criteria:** train & evaluate a PyTorch model; map it to the from-scratch version.

## Month 11 — NLP + attention
- **Objective:** sequence modeling and the attention mechanism.
- **Topics:** tokenization, embeddings, language modeling, sequence models; attention (Q/K/V,
  scaled dot-product, self-attention, multi-head, causal masks).
- **Labs:** char-level language model (project #23); self-attention (project #24).
- **Project:** #24 Self-attention implementation.
- **Assessment:** implement self-attention from scratch; explain multi-head.
- **Exit criteria:** attention implemented and explained.

## Month 12 — Transformers + intro LLM engineering
- **Objective:** assemble a transformer; first taste of LLM engineering.
- **Topics:** transformer block (residuals, norm, FFN), encoder/decoder, autoregressive
  generation, sampling (temperature, top-k/p), KV cache; model APIs, structured outputs.
- **Labs:** tiny transformer (project #25); tiny GPT (project #26).
- **Project:** #26 Tiny GPT-style model trained on a small corpus.
- **Assessment:** build & train a tiny transformer; explain generation & sampling.
- **Exit criteria (Year 1):** a working tiny GPT you understand end-to-end → ready for Year 2
  (RAG, AI engineering, agents, MCP, computer use, MLOps, research).

---
Year 2+ continues with Phases 10–12. Those lessons are generated as you reach them.
