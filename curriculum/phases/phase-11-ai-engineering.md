# Phase 11 — RAG & Production AI Engineering

**Timeline:** ~8–12 weeks · **Module:** [11-rag-and-ai-engineering](../../modules/11-rag-and-ai-engineering/)

## Goal
Build grounded, reliable LLM applications — understand the full RAG pipeline without hiding it
behind a framework.

## Prerequisites
Phase 10.

## Topics & required depth
- **RAG pipeline:** documents → ingestion → parsing → cleaning → chunking → metadata → embeddings
  → indexing → retrieval → reranking → context construction → generation → citations → evaluation.
- **Retrieval:** sparse retrieval (BM25), dense retrieval, embeddings, semantic search, vector
  indexes, metadata filtering, hybrid search, reranking, chunking strategies, query transformation,
  context limits, grounded generation, retrieval evaluation, answer evaluation, RAG failure modes,
  RAG security (poisoning, injection via documents).
- **AI engineering:** model APIs, open-weight models, structured outputs, function calling, prompt
  construction, prompt versioning, tool definitions, model routing, caching, retries, validation,
  guardrails, evaluation, tracing, observability, latency, cost, reliability, fallbacks, human
  approval, production architecture.

## Mathematics / DSA threads
Vector similarity (dot product/cosine); nearest-neighbor search structures.

## Hands-on labs
Build BM25 by hand; build dense retrieval with embeddings; compare both and a hybrid; measure
retrieval quality (recall@k) and answer quality; add structured-output validation and tracing.

## From-scratch implementation
- Embedding search engine (project #27) — embeddings + cosine similarity + a simple index.
- A minimal RAG loop before adopting any RAG framework.

## Mini-project
A retrieval-quality harness (recall@k, MRR) over a small corpus.

## Major project
Project #28 — a RAG system with citations and an evaluation harness.

## Recommended resources
Full Stack Deep Learning; your model provider's official docs; OWASP LLM Top 10 (for RAG security).
(See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Build RAG exposing every stage; measure and improve retrieval; show a grounded answer with
citations; identify and mitigate a RAG failure mode.

## Exit criteria
- A working RAG system you can decompose stage-by-stage.
- Retrieval and answer quality measured, not assumed.
- Structured outputs + guardrails + tracing in place.

## Common mistakes
- Chunking blindly; ignoring metadata; no retrieval evaluation.
- Trusting the model's answer without grounding/citations.
- No guardrails on structured output; no cost/latency tracing.

## Connection to next phase
Grounded apps → give them tools and autonomy, safely (Phase 12: agents, MCP, computer use).
