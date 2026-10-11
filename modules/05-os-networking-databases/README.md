# Module 05 — Operating Systems, Networking, Databases

## Purpose
Understand the environment software runs inside, talks across, and persists to.

## Prerequisites
Module 02 (Module 03 in parallel).

## Topics
OS (kernel/user space, processes/threads, scheduling, context switches, concurrency, locks/
semaphores, deadlocks, races, virtual memory/paging, files, permissions, syscalls, signals, IPC,
containers vs VMs) · networking (layers, TCP/IP, DNS, ports, sockets, TCP/UDP, HTTP/HTTPS/TLS,
REST, WebSockets, proxies, load balancers, auth/authz, tokens/OAuth, retries/timeouts/idempotency/
rate limits) · databases (SQL, joins, aggregation, window functions, normalization, keys, indexes,
B-trees, query planning, transactions/ACID, isolation levels, replication, partitioning, NoSQL,
caching, vector DBs).

## Learning outcomes
- Explain a context switch, a TCP handshake, and a database index.
- Build a client/server over sockets; write non-trivial SQL; reason about isolation.

## Exercises
Socket client/server; observe a handshake; `EXPLAIN` a query; demonstrate a deadlock and a race.

## Projects
#9 HTTP client/server · #11 small relational application · #12 key-value store.

## Exit criteria
Working server; non-trivial SQL; concurrency hazards explained.

## Connections
← [02](../02-programming/) · → [06](../06-software-and-backend-engineering/). Networking→HTTP→APIs→
tool calling→MCP→agents; OS→processes→permissions→sandboxes→computer-use agents
([`../../CONCEPT_MAP.md`](../../CONCEPT_MAP.md)). Phase detail:
[phase-05](../../curriculum/phases/phase-05-core-software-systems.md).
