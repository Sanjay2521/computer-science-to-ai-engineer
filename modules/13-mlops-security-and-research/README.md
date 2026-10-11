# Module 13 — MLOps, Security & Research

## Purpose
Run AI systems reliably, securely, and responsibly; understand RL and multimodal AI; read and
reproduce research.

## Prerequisites
Modules 11–12.

## Topics
MLOps/LLMOps (experiment/dataset/model versioning, registries, packaging, serving, batch/online
inference, CI/CD, monitoring, drift, LLM/prompt evaluation, tracing, latency/throughput/batching,
GPU utilization, caching, cost, rollbacks, A/B, incident response) · security & responsible AI
(authn/authz, least privilege, secrets, encryption, dependency/supply-chain risk, input validation,
privacy/PII, prompt injection, tool abuse, exfiltration, excessive agency, RAG poisoning,
sandboxing, audit logs, bias/fairness) · reinforcement learning (MDP, value/policy, Bellman,
exploration/exploitation, bandits, Q-learning, policy gradients, deep RL, alignment link) ·
multimodal (image embeddings, ViT, contrastive learning, VLMs, speech/audio, diffusion, multimodal
agents) · research skills (reading papers, reproducing baselines, experiment design, ablations,
benchmark literacy, technical writing, documenting failures).

## Learning outcomes
- Deploy and monitor a service; threat-model an agent.
- Reproduce a paper baseline, run an ablation, write a technical report.

## Exercises
Add experiment tracking + versioning to an earlier project; set up monitoring + drift detection;
Q-learning on a gridworld; reproduce a paper figure.

## Projects
#35 production AI service · #36 end-to-end AI platform capstone · one reproduced paper (logged in
[`../../state/paper-reading-log.md`](../../state/paper-reading-log.md)).

## Exit criteria (research-capable)
Monitored production service; agent threat model; reproduced paper baseline + ablation + report;
capstone integrating the full stack.

## Connections
← [12](../12-agents-mcp-and-computer-use/). Completes the arc: explain, implement, test, debug, and
connect the full stack from transistors to production AI. Phase detail:
[phase-13](../../curriculum/phases/phase-13-production-and-research.md).
