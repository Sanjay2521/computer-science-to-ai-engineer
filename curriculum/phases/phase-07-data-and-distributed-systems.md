# Phase 7 — Distributed Systems, Cloud & Data Engineering

**Timeline:** ~8–12 weeks · **Module:** [07-distributed-cloud-and-data-engineering](../../modules/07-distributed-cloud-and-data-engineering/)

## Goal
Reason about systems that fail partially and span machines; move and transform data reliably at
scale.

## Prerequisites
Phases 5 and 6.

## Topics & required depth
- **Distributed systems:** failure modes, latency, partial failure, consistency, availability,
  CAP theorem, replication, partitioning, consensus intuition, message queues, pub/sub,
  event-driven systems, delivery semantics (at-most/at-least/exactly-once), idempotency,
  retries & backoff, distributed locks, sagas, eventual consistency, clocks & ordering,
  observability.
- **Cloud & DevOps:** Linux fundamentals, VMs, containers, Docker, images/registries, container
  networking, volumes, Kubernetes fundamentals, CI/CD, secrets, configuration, IaC concepts,
  cloud compute/storage/networking, managed databases, serverless concepts, monitoring, cost
  awareness. *Not* certification memorization.
- **Data engineering:** NumPy, Pandas, SQL, data cleaning, validation, ETL/ELT, batch processing,
  streaming concepts, data pipelines, orchestration, warehouses, lakes, lakehouses, columnar
  formats, partitioning, Spark fundamentals, data quality, lineage, feature pipelines,
  reproducibility.

## Mathematics / DSA threads
NumPy/Pandas reinforce linear algebra and statistics in practice.

## Hands-on labs
Containerize a service with Docker; build a queue-based producer/consumer with retries and
idempotency; clean & validate a messy dataset; schedule a simple pipeline.

## From-scratch implementation
A reliable producer/consumer over a queue (at-least-once + idempotent handler) before adopting a
framework.

## Mini-project
Project #14 — queue-based distributed-system experiment.

## Major project
Project #15 — ETL pipeline with validation, partitioning, and reproducibility.

## Recommended resources
Designing Data-Intensive Applications; Docker/Kubernetes docs; Pandas/NumPy docs.
(See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Explain CAP with a concrete scenario; design retry/idempotency for a flaky dependency; build a
validated pipeline and defend its reliability choices.

## Exit criteria
- Build a resilient queue-based component and a validated data pipeline.
- Containerize a service; reason about consistency/availability trade-offs.

## Common mistakes
- Assuming the network is reliable; retries without idempotency (duplicates).
- Confusing "exactly-once delivery" myths with "effectively-once processing."
- Pipelines with no validation or lineage.

## Connection to next phase
Data + infrastructure ready → start learning *from* data (Phase 8: classical ML).
