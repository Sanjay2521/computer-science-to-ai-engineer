# Phase 5 — Operating Systems, Networking, Databases

**Timeline:** ~10–14 weeks · **Module:** [05-os-networking-databases](../../modules/05-os-networking-databases/)

> (ROADMAP calls this timeline-phase 4; the subject module/phase file is numbered 5. Both are
> cross-linked.)

## Goal
Understand the environment software runs inside (OS), talks across (networking), and persists to
(databases).

## Prerequisites
Phase 2 (Phase 3 in parallel).

## Topics & required depth
- **Operating systems:** kernel vs user space, processes, threads, scheduling, context switching,
  concurrency, synchronization (locks, semaphores), deadlocks, race conditions, virtual memory,
  paging, files, file systems, permissions, system calls, signals, IPC, containers vs VMs.
- **Networking:** network layers, TCP/IP, IP addresses, subnets (conceptually), routing, DNS,
  ports, sockets, TCP, UDP, HTTP, HTTPS, TLS, requests/responses, REST, WebSockets, proxies,
  reverse proxies, load balancers, authentication, authorization, sessions, tokens, OAuth
  concepts, API design, retries, timeouts, idempotency, rate limits.
- **Databases:** relational model, tables/schemas, SQL, joins, aggregation, subqueries, window
  functions, normalization, keys, constraints, indexes, B-trees (conceptually), query planning,
  transactions, ACID, locks, isolation levels, concurrency anomalies, replication, partitioning,
  NoSQL categories, document/key-value stores, caching, vector databases, reliability.

## Mathematics / DSA threads
Probability starts here (conditional, Bayes); DSA stays warm via mixed problems and tries.

## Hands-on labs
Socket programming; observe a TCP handshake; write non-trivial SQL with joins/window functions;
`EXPLAIN` a query plan; demonstrate a deadlock and a race condition.

## From-scratch implementation
- HTTP client and server (parse requests, form responses).
- Key-value store with a simple on-disk index.

## Mini-project
Project #12 — key-value store.

## Major project
Project #9 — HTTP client/server, and/or project #11 — small relational application.

## Recommended resources
OSTEP; Beej's Guide; Computer Networking (Top-Down); Use The Index, Luke.
(See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Explain a context switch, a TCP handshake, and a database index; build a working server; write
SQL answering a real question; reason about an isolation anomaly.

## Exit criteria
- Build a client/server over sockets and speak HTTP.
- Write non-trivial SQL; explain indexes and transactions.
- Explain concurrency hazards and how to avoid them.

## Common mistakes
- Blocking on I/O without understanding why; ignoring timeouts/retries.
- Treating HTTP as magic rather than text over TCP.
- SELECT * and missing indexes; not understanding isolation levels.

## Connection to next phase
Know the platform → engineer maintainable software and design systems on it (Phase 6).
