# Phase 13 — MLOps, LLMOps, Security, Multimodal, RL & Research

**Timeline:** ongoing · **Module:** [13-mlops-security-and-research](../../modules/13-mlops-security-and-research/)

## Goal
Run AI systems reliably, securely, and responsibly; understand RL and multimodal AI; read and
reproduce research.

## Prerequisites
Phases 11–12.

## Topics & required depth
- **MLOps / LLMOps:** experiment tracking, dataset versioning, model versioning, reproducible
  training, model registries, packaging, model serving, batch & online inference, CI/CD,
  monitoring, data drift, concept drift, model quality, LLM evaluation, prompt evaluation,
  tracing, latency, throughput, batching, GPU utilization, caching, cost optimization, rollbacks,
  A/B testing concepts, incident response.
- **Security & responsible AI:** authentication, authorization, least privilege, secret
  management, encryption concepts, dependency & supply-chain risk, input validation, data privacy,
  PII handling, prompt injection (direct & indirect), tool abuse, data exfiltration, excessive
  agency, RAG poisoning, model misuse, sandboxing, audit logging, human approval, evaluation
  limitations, bias & fairness, responsible deployment.
- **Reinforcement learning:** agent, environment, state, action, reward, policy, return, value
  functions, Bellman intuition, exploration vs exploitation, multi-armed bandits, Q-learning,
  policy gradients, deep RL concepts, relationship to alignment and agent learning.
- **Multimodal AI:** image representation, image embeddings, vision transformers, contrastive
  learning concepts, vision-language models, speech/audio fundamentals, multimodal transformers,
  diffusion-model fundamentals, multimodal agents.
- **Research skills:** reading papers, identifying research questions, understanding assumptions,
  reproducing baselines, designing experiments, tracking variables, comparing models fairly,
  ablations, interpreting benchmarks, avoiding misleading conclusions, writing technical reports,
  documenting failed experiments.

## Hands-on labs
Add experiment tracking + model versioning to an earlier project; set up monitoring + drift
detection; threat-model an agent; implement a bandit and Q-learning on a toy environment;
reproduce a figure from a paper.

## From-scratch implementation
A small RL agent (Q-learning) on a gridworld before any deep-RL library.

## Major projects
- Project #35 — a production AI service (serving, monitoring, guardrails, cost).
- Project #36 — end-to-end AI platform capstone integrating retrieval, agents, and ops.
- A reproduced research paper baseline, logged in
  [`../../state/paper-reading-log.md`](../../state/paper-reading-log.md).

## Recommended resources
Made With ML / Full Stack Deep Learning (MLOps); OWASP LLM Top 10; OpenAI Spinning Up (RL);
arXiv + Papers With Code. (See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Deploy and monitor a service; threat-model an agent and propose mitigations; reproduce a paper
baseline and run an ablation; write a technical report of an experiment (including what failed).

## Exit criteria (research-capable, M10)
- A monitored production AI service; a security threat model for an agent.
- One reproduced paper baseline with an ablation and a written report.
- The capstone integrating the full stack.

## Common mistakes
- Treating a passing eval as proof of correctness; cherry-picking benchmarks.
- No drift monitoring; no rollback plan; secrets in config.
- Reproducing a paper without controlling variables.

## Connection onward
This phase is where learning becomes practice: you now *explain, implement, test, debug, and
connect* the full stack from transistors to production AI agents — the central objective of the
whole program. Keep a steady cadence of papers, projects, and reviews.
