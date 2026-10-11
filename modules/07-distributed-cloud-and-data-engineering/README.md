# Module 07 — Distributed Systems, Cloud & Data Engineering

## Purpose
Reason about systems that fail partially and span machines; move and transform data reliably.

## Prerequisites
Modules 05 and 06.

## Topics
Distributed systems (failure modes, latency, partial failure, consistency/availability, CAP,
replication/partitioning, consensus intuition, message queues, pub/sub, event-driven, delivery
semantics, idempotency, retries/backoff, distributed locks, sagas, eventual consistency, clocks/
ordering, observability) · cloud/DevOps (Linux, VMs, Docker, images/registries, volumes,
Kubernetes basics, CI/CD, secrets, IaC concepts, managed services, serverless, monitoring, cost) ·
data engineering (NumPy, Pandas, SQL, cleaning/validation, ETL/ELT, batch/streaming, pipelines,
orchestration, warehouses/lakes/lakehouses, columnar formats, partitioning, Spark basics, quality,
lineage, feature pipelines, reproducibility).

## Learning outcomes
- Explain CAP with a concrete scenario; design retry + idempotency for a flaky dependency.
- Build a resilient queue component and a validated data pipeline; containerize a service.

## Exercises
Dockerize a service; producer/consumer with at-least-once + idempotent handling; clean/validate a
messy dataset.

## Projects
#14 queue-based distributed experiment · #15 ETL pipeline.

## Exit criteria
Resilient queue component + validated pipeline; containerized service.

## Connections
← [06](../06-software-and-backend-engineering/) · → [08](../08-machine-learning/) (NumPy/Pandas
feed ML). Phase detail: [phase-07](../../curriculum/phases/phase-07-data-and-distributed-systems.md).
