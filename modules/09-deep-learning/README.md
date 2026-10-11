# Module 09 — Deep Learning

## Purpose
Build and train neural networks; understand backpropagation deeply enough to write an autograd
engine.

## Prerequisites
Module 08; calculus/linear-algebra threads.

## Topics
Perceptrons, layers, tensors, forward prop, losses, backprop, computational graphs · gradient
descent, SGD, momentum, Adam · activations, initialization, normalization, regularization, dropout
· CNNs, RNNs, LSTMs, sequence modeling, attention (intro) · PyTorch, GPU basics, training loops,
datasets/dataloaders, checkpointing, evaluation, debugging training.

## Learning outcomes
- Derive and implement backprop; build a micrograd-style autograd engine.
- Train a PyTorch model and debug one that won't learn.

## Exercises
Overfit a tiny dataset on purpose (sanity check); visualize a computational graph; debug LR/init/
normalization failures.

## Projects
#20 NumPy neural network · #21 autograd engine · #22 PyTorch model.

## Exit criteria
Autograd engine + from-scratch net + matching PyTorch model; systematic training debugging.

## Connections
← [08](../08-machine-learning/) · → [10](../10-transformers-and-llms/). Calculus (chain rule) →
backprop ([`../../CONCEPT_MAP.md`](../../CONCEPT_MAP.md)). Phase detail:
[phase-09](../../curriculum/phases/phase-09-deep-learning.md).
