# PROJECTS — The Project Ladder

A progressive ladder of 36 projects. Each validates one or more layers of the stack. Small
projects validate a single layer; larger ones integrate several. You don't need to build all of
them huge — use the small ones as checkpoints.

Status tracked in [`state/project-log.md`](state/project-log.md).

## How to use each project
Before starting, fill in (in the project log): **goal · prerequisites · concepts practiced ·
constraints · architecture · milestones · tests · debugging tasks · extensions · completion
evidence · retrospective questions.** A project is "done" only with completion evidence and a
written retrospective.

## The ladder

| # | Project | Phase | Layer validated |
|---|---------|-------|-----------------|
| 1 | Number-system converter | 1 | binary/hex/two's complement |
| 2 | Logic-gate simulator | 1 | boolean logic, circuits |
| 3 | Small CPU / instruction-set emulator | 1 | ISA, fetch-decode-execute |
| 4 | C memory experiments | 2 | pointers, stack/heap, segfaults |
| 5 | Command-line utility | 2 | Python, CLI, packaging |
| 6 | Mini shell | 2 | processes, pipes, OS basics |
| 7 | Data-structures library | 3 | lists/stacks/queues/trees/graphs |
| 8 | Algorithm visualizer | 3 | sorting/search/graph algorithms |
| 9 | HTTP client and server | 4 | sockets, TCP, HTTP |
| 10 | REST API | 5 | API design, services |
| 11 | Small relational application | 4–5 | SQL, schema, transactions |
| 12 | Key-value store | 4 | storage, indexing, persistence |
| 13 | Concurrent task processor | 4 | threads/processes, synchronization |
| 14 | Queue-based distributed-system experiment | 6 | queues, delivery semantics, retries |
| 15 | ETL pipeline | 6 | data engineering, validation |
| 16 | Linear regression from scratch | 7 | gradient descent, loss |
| 17 | Logistic regression from scratch | 7 | classification, sigmoid, cross-entropy |
| 18 | Decision tree from scratch | 7 | recursion, impurity, splits |
| 19 | ML evaluation project | 7 | metrics, cross-validation, leakage |
| 20 | NumPy neural network | 8 | forward/backprop by hand |
| 21 | Small autograd engine | 8 | computational graph (micrograd-style) |
| 22 | PyTorch image or text model | 8 | training loops, GPU, checkpoints |
| 23 | Character-level language model | 9 | sequence modeling |
| 24 | Self-attention implementation | 9 | Q/K/V, scaled dot-product |
| 25 | Tiny transformer | 9 | blocks, residuals, norm, masks |
| 26 | Tiny GPT-style model | 9 | autoregressive generation (nanoGPT-style) |
| 27 | Embedding search engine | 10 | embeddings, similarity, vector index |
| 28 | RAG system | 10 | full retrieve→rerank→generate→cite pipeline |
| 29 | Tool-calling assistant | 11 | function calling, structured output |
| 30 | MCP server and client | 11 | protocol, schemas, resources, auth |
| 31 | Minimal agent framework | 11 | the agent loop from scratch |
| 32 | Browser automation agent | 11 | DOM/accessibility tree, Playwright |
| 33 | Sandboxed computer-use agent | 11 | OS actions, sandbox, approval gates |
| 34 | Simplified coding agent | 11 | repo index → patch → test → retry → diff |
| 35 | Production AI service | 12 | serving, monitoring, guardrails, cost |
| 36 | End-to-end AI platform capstone | 12 | integrates the whole stack |

## Dependencies
Projects generally require the project(s) in their phase and earlier. For example: #28 (RAG)
needs #27 (embedding search); #34 (coding agent) needs #31 (agent loop) and #29 (tool calling);
#36 (capstone) integrates retrieval (#28), agents (#31–34), and production ops (#35).

## Safety note
Projects #32–34 (browser / computer-use / coding agents) must begin in **local sandboxes with
disposable data and explicit approval gates**. See [`AGENT_RULES.md`](AGENT_RULES.md) §Safety.
