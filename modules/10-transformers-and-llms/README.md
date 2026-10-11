# Module 10 — Transformers & LLMs

## Purpose
Understand transformers and LLMs from the inside — build a tiny GPT you fully understand.

## Prerequisites
Module 09.

## Topics
Tokenization, vocabulary, embeddings, positional info · Q/K/V, scaled dot-product attention,
self-attention, multi-head, causal masks · feed-forward, residuals, normalization · encoder/
decoder/encoder-decoder · autoregressive generation · pretraining, fine-tuning, instruction
tuning, RLHF/DPO concepts · sampling (greedy, beam, temperature, top-k, top-p) · context windows,
KV cache, batching, quantization, LoRA, PEFT, inference, serving, evaluation, hallucination,
safety limits.

## Learning outcomes
- Implement self-attention and a transformer block from scratch.
- Train a tiny GPT; explain the KV cache and each sampling strategy.

## Exercises
Build a tokenizer; visualize attention weights; measure KV-cache effect; experiment with sampling.

## Projects
#23 char-level LM · #24 self-attention · #25 tiny transformer · #26 tiny GPT.

## Exit criteria
Self-attention + transformer block from scratch; trained tiny GPT; first paper logged.

## Connections
← [09](../09-deep-learning/) · → [11](../11-rag-and-ai-engineering/). Linear algebra → attention →
transformers ([`../../CONCEPT_MAP.md`](../../CONCEPT_MAP.md)). Phase detail:
[phase-10](../../curriculum/phases/phase-10-transformers-and-llms.md).
