# Phase 9 — Deep Learning & PyTorch

**Timeline:** ~10–14 weeks · **Module:** [09-deep-learning](../../modules/09-deep-learning/)

## Goal
Build and train neural networks; understand backpropagation deeply enough to implement an
autograd engine.

## Prerequisites
Phase 8; calculus/linear-algebra threads.

## Topics & required depth
- **Core:** perceptrons, layers, tensors, forward propagation, loss functions, backpropagation,
  computational graphs, gradient descent, SGD, momentum, Adam, activation functions,
  initialization, normalization, regularization, dropout.
- **Architectures:** CNNs, RNNs, LSTMs, sequence modeling, attention (introduction — deepened in
  Phase 10).
- **PyTorch & engineering:** tensors/autograd, GPU fundamentals, training loops, datasets/
  dataloaders, checkpointing, evaluation, debugging training.

## Mathematics / DSA threads
Chain rule applied to backprop; matrix calculus intuition.

## Hands-on labs
Visualize a computational graph; overfit a tiny dataset deliberately (sanity check); debug a model
that won't learn (LR, init, normalization).

## From-scratch implementation
- NumPy neural network (project #20) — forward + manual backprop.
- Autograd engine (project #21) — micrograd-style reverse-mode autodiff.
- Reproduce the same network in PyTorch and match results.

## Mini-project
A from-scratch MLP trained on a small dataset with your own autograd.

## Major project
Project #22 — a PyTorch image or text model trained end-to-end.

## Recommended resources
Dive into Deep Learning (d2l.ai); Karpathy Zero-to-Hero + micrograd; PyTorch tutorials; fast.ai.
(See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Derive and implement backprop for a 2-layer net; explain each optimizer; debug a non-training
model and state the root cause.

## Exit criteria
- An autograd engine you built; a trained-from-scratch net; a matching PyTorch model.
- You can debug training failures systematically.

## Common mistakes
- Forgetting to zero gradients; wrong loss/activation pairing.
- Exploding/vanishing gradients from bad init/no normalization.
- Evaluating on training data; data not shuffled.

## Connection to next phase
Neural nets + attention intro → go deep on transformers and LLM internals (Phase 10).
