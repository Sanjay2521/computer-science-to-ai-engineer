# Phase 6 — Software Engineering & System Design

**Timeline:** ~8–12 weeks · **Module:** [06-software-and-backend-engineering](../../modules/06-software-and-backend-engineering/)

## Goal
Write maintainable systems and reason about design trade-offs; build a real backend service.

## Prerequisites
Phases 2 and 5.

## Topics & required depth
- **Engineering:** requirements, decomposition, clean code, naming, functions/modules,
  abstraction, coupling & cohesion, OOP principles, composition, SOLID as *guidance not dogma*,
  design patterns, refactoring.
- **Testing:** unit, integration, end-to-end, test doubles, property-based testing concepts.
- **Operability:** error handling, logging, configuration, documentation, code reviews, CI/CD,
  versioning, dependency management, security fundamentals, maintainability.
- **Backend:** APIs, service layers, authentication, authorization, background jobs, queues,
  caches, file storage, database integration.
- **System design:** scalability, horizontal/vertical scaling, load balancing, rate limiting,
  high availability, reliability, observability, fault tolerance, capacity estimation, trade-offs.

## Mathematics / DSA threads
Statistics (descriptive/inferential) in parallel; DSA via code-review-sized problems.

## Hands-on labs
Refactor a messy module; add a test pyramid; set up CI; add logging/metrics/tracing to a service;
do a capacity estimate.

## From-scratch implementation
A small service layer with auth and a background job/queue — standard library first where
reasonable, then one well-justified dependency.

## Mini-project
Add observability (logs, metrics, a health check) to an existing service.

## Major project
Project #10 — a REST API backed by a database, with tests, CI, and observability.

## Recommended resources
Designing Data-Intensive Applications (early chapters); The Twelve-Factor App; framework docs.
(See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Design a small service end-to-end on paper and defend the trade-offs; ship a tested, documented,
observable API.

## Exit criteria
- Build and operate a tested REST API with CI.
- Reason explicitly about coupling, testing strategy, and scaling trade-offs.

## Common mistakes
- Applying SOLID/patterns dogmatically; premature abstraction.
- Tests that assert implementation details; no integration tests.
- No observability until production breaks.

## Connection to next phase
Single-node mastery → scale out and move data at scale (Phase 7: distributed systems, cloud, data
engineering).
