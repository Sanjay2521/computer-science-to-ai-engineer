# Phase 4 (thread) — Mathematics for AI & Computing

**Timeline:** runs in parallel with Phases 3–9 · **Module:** [04-mathematics](../../modules/04-mathematics/)

> This is a **parallel thread**, not a stop-the-world block. It starts in Phase 2 (functions,
> logs), has its core block alongside DSA (Phase 3), and is then *applied continuously* in ML/DL
> (Phases 7–9). Teach intuition first, then formal notation, then code.

## Goal
Build the mathematical spine for machine learning: linear algebra, probability/statistics,
calculus/optimization, and information theory — each connected to code and to AI.

## Prerequisites
Phase 2 (functions, logs/exponents). Comfort reading/writing Python.

## Topics & required depth
- **Foundations:** algebra, functions, graphs, exponents, logarithms, sequences, summations.
- **Linear algebra:** vectors, matrices, dot products, matrix multiplication, linear
  transformations, basis & dimension, eigenvalue intuition.
- **Probability:** probability, conditional probability, Bayes' theorem, random variables, common
  distributions, expectation, variance, covariance, sampling.
- **Statistics:** descriptive & inferential statistics, hypothesis-testing intuition.
- **Calculus & optimization:** limits, derivatives, partial derivatives, gradients, chain rule,
  optimization, gradient descent, convexity intuition.
- **Information theory:** entropy, cross-entropy, KL divergence.

Depth: enough to *implement* each idea in NumPy and to recognize it inside ML/DL later.

## Hands-on labs / from-scratch
- Vector & matrix operations in NumPy, then verify by hand.
- Gradient descent from scratch on a simple function.
- Entropy/cross-entropy computed by hand and in code.

## Mini-project
A notebook series: "math you can run" — each concept with an intuition note, the formula, and a
code cell. Log connections in [`../../state/mathematics-tracker.md`](../../state/mathematics-tracker.md).

## Major project
Gradient descent from scratch that later becomes the optimizer in your from-scratch ML (Phase 7)
and neural net (Phase 8).

## Recommended resources
3Blue1Brown (Essence of Linear Algebra/Calculus); Mathematics for Machine Learning (mml-book);
Khan Academy. (See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Implement a dot product, matmul, and gradient descent by hand; explain Bayes with a concrete
example; derive cross-entropy from entropy.

## Exit criteria
- Each major idea: intuition + formula + working code, with a logged connection to computing/ML.
- Gradient descent implemented and understood.

## Common mistakes
- Learning notation without intuition (or vice versa).
- Confusing probability with likelihood; mixing up rows/columns in matmul.
- Treating gradient descent as magic rather than "step downhill."

## Connection to the AI track
Linear algebra → embeddings → attention → transformers. Calculus → backprop. Probability/stats →
losses & evaluation. Information theory → classification/LLM objectives. See
[`../../CONCEPT_MAP.md`](../../CONCEPT_MAP.md).
