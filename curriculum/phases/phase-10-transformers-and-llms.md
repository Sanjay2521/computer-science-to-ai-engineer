# Phase 10 — NLP, Attention, Transformers & LLM Internals

**Timeline:** ~12–16 weeks · **Module:** [10-transformers-and-llms](../../modules/10-transformers-and-llms/)

## Goal
Understand transformers and LLMs from the inside — build a tiny GPT you fully understand.

## Prerequisites
Phase 9.

## Topics & required depth
- **NLP foundations:** text preprocessing, tokenization, vocabulary, language modeling, word
  embeddings, sequence models, evaluation.
- **Attention:** embeddings, positional information, query/key/value, scaled dot-product
  attention, self-attention, multi-head attention, causal masks.
- **Transformer:** feed-forward layers, residual connections, normalization; encoder, decoder,
  encoder-decoder; autoregressive generation.
- **Training & tuning:** pretraining, fine-tuning, instruction tuning, preference optimization /
  RLHF / DPO concepts.
- **Inference:** sampling, greedy decoding, beam-search concepts, temperature, top-k, top-p,
  context windows, KV cache, batching, quantization, LoRA, PEFT, serving, evaluation,
  hallucination, safety limitations.

## Mathematics / DSA threads
Linear algebra realized: attention *is* matmul + softmax. Information theory: the LM loss is
cross-entropy.

## Hands-on labs
Implement a tokenizer; visualize attention weights; measure how the KV cache changes inference
cost; experiment with sampling parameters.

## From-scratch implementation (progressive)
1. Character-level model (project #23)
2. Self-attention (project #24)
3. Transformer block (project #25)
4. Tiny GPT (project #26)
5. Train & generate experiment (nanoGPT-style)

## Mini-project
Self-attention from scratch with a visualization of the attention matrix.

## Major project
Project #26 — a tiny GPT trained on a small corpus, with a generation experiment.

## Recommended resources
Karpathy nanoGPT + "Let's build GPT"; "Attention Is All You Need" (after implementing attention);
The Illustrated Transformer; LLMs from Scratch (Raschka); Hugging Face course.
(See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Implement self-attention and a transformer block from scratch; explain the KV cache and each
sampling strategy; train and sample from a tiny GPT.

## Exit criteria
- Self-attention + transformer block from scratch; a trained tiny GPT.
- You can explain tokenization, generation, and inference optimizations.
- First paper logged in [`../../state/paper-reading-log.md`](../../state/paper-reading-log.md).

## Common mistakes
- Forgetting the causal mask (future leakage); wrong softmax axis.
- Confusing parameters vs activations; misunderstanding positional encodings.
- Treating temperature/top-p as interchangeable.

## Connection to next phase
Understand LLMs → use them in real, grounded, reliable systems (Phase 11: RAG & AI engineering).
