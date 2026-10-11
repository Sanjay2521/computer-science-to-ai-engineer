# Module 11 — RAG & AI Engineering

## Purpose
Build grounded, reliable LLM applications — understand the full RAG pipeline without hiding it
behind a framework.

## Prerequisites
Module 10.

## Topics
RAG pipeline (ingest → parse → clean → chunk → metadata → embed → index → retrieve → rerank →
context → generate → cite → evaluate) · sparse (BM25)/dense/hybrid retrieval, vector indexes,
metadata filtering, chunking strategies, query transformation, grounded generation, retrieval &
answer evaluation, RAG failure modes, RAG security · AI engineering (model APIs, open-weight
models, structured outputs, function calling, prompt construction/versioning, routing, caching,
retries, validation, guardrails, evaluation, tracing, observability, latency, cost, fallbacks,
human approval, production architecture).

## Learning outcomes
- Build RAG exposing every stage; measure retrieval (recall@k) and answer quality.
- Add structured outputs, guardrails, and tracing.

## Exercises
BM25 by hand; dense retrieval with embeddings; hybrid comparison; a retrieval-quality harness.

## Projects
#27 embedding search engine · #28 RAG system with citations + evaluation.

## Exit criteria
Decomposable RAG system; measured retrieval/answer quality; guardrails + tracing.

## Connections
← [10](../10-transformers-and-llms/) · → [12](../12-agents-mcp-and-computer-use/). Embeddings →
similarity → retrieval ([`../../CONCEPT_MAP.md`](../../CONCEPT_MAP.md)). Phase detail:
[phase-11](../../curriculum/phases/phase-11-ai-engineering.md).
