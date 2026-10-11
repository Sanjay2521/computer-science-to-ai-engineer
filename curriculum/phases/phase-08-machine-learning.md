# Phase 8 — Classical Machine Learning

**Timeline:** ~10–14 weeks · **Module:** [08-machine-learning](../../modules/08-machine-learning/)

## Goal
Understand learning from data from first principles — implement core algorithms before reaching
for scikit-learn.

## Prerequisites
Phase 3 (math spine) and Phase 7 (data).

## Topics & required depth
- **Framing:** what learning from data means; supervised vs unsupervised; training/validation/
  testing; data leakage; features & labels.
- **Models:** linear regression, logistic regression, k-nearest neighbors, naive Bayes concepts,
  decision trees, random forests, gradient boosting, SVM concepts; clustering (k-means); PCA.
- **Practice:** feature engineering, preprocessing, missing data, class imbalance; loss functions,
  optimization, regularization, bias & variance, cross-validation, evaluation metrics,
  calibration, hyperparameter tuning, explainability, reproducibility, baselines, experiment
  design.

## Mathematics / DSA threads
Optimization & probability applied directly; information theory (entropy, cross-entropy) for
classification losses.

## Hands-on labs
Build a train/val/test split with no leakage; implement cross-validation; plot learning curves to
diagnose bias/variance.

## From-scratch implementation (before scikit-learn)
- Linear regression (project #16) — gradient descent + normal equation.
- Logistic regression (project #17) — sigmoid + cross-entropy.
- Decision tree (project #18) — recursive splits on impurity.
Then reproduce each with scikit-learn and explain what it hides.

## Mini-project
A baseline-vs-model comparison with honest metrics.

## Major project
Project #19 — end-to-end ML project with a leak-free evaluation harness.

## Recommended resources
ISLR; scikit-learn user guide (after from-scratch); Made With ML.
(See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Implement 3 algorithms from scratch; diagnose over/underfitting from curves; justify a metric for
a given problem; detect a leakage bug.

## Exit criteria
- Three algorithms implemented from scratch and verified against scikit-learn.
- A leak-free pipeline with honest evaluation and a sensible baseline.

## Common mistakes
- Data leakage (fitting scalers on the full dataset; target leakage).
- Optimizing accuracy on imbalanced data; ignoring baselines.
- Tuning on the test set.

## Connection to next phase
Classical ML → scale representation learning with neural networks (Phase 9: deep learning).
