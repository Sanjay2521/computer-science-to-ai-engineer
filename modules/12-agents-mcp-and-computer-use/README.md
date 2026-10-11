# Module 12 — Agents, MCP & Computer Use

## Purpose
Build tool-using agents **safely**, from a minimal loop up to browser, computer-use, and coding
agents. A major goal of the program.

## Prerequisites
Module 11.

## Topics
The agent loop (goal → state → plan → tool select → execute → observe → update → next → respond) ·
workflows vs agents, tool calling, state, memory, planning, reflection, retries, error recovery,
human-in-the-loop, permissions, multi-agent, agent evaluation, excessive-agency risk · MCP
(client/server, tool discovery, schemas, resources, auth/authz, validation, errors, security
boundaries, observability) · browser/computer use (HTML/DOM/CSS selectors, accessibility trees,
Playwright, screenshots, CV/OCR concepts, mouse/keyboard automation, OS APIs, sandboxes/containers/
VMs, credentials, sessions, prompt injection — direct & indirect, audit logs, recovery) · coding
agents (indexing, search, context selection, planning, patch generation, terminal/test feedback,
diffs, rollback).

## Safety (non-negotiable)
Start in local sandboxes with disposable data and non-privileged accounts; require explicit
approval for destructive/external/irreversible actions. See
[`../../AGENT_RULES.md`](../../AGENT_RULES.md) §Safety.

## Learning outcomes
- Build an agent loop from scratch and an MCP server/client.
- Build browser, sandboxed computer-use, and simplified coding agents; mitigate prompt injection.

## Exercises
Define tools with JSON schemas; craft and defend against a prompt-injection attempt in a sandbox;
drive a sample local page with Playwright.

## Projects
#29 tool-calling assistant · #30 MCP server/client · #31 minimal agent framework · #32 browser
agent · #33 sandboxed computer-use agent · #34 simplified coding agent.

## Exit criteria
From-scratch agent loop, MCP server/client, browser + computer-use + coding agents, all with
safety controls; can threat-model an agent.

## Connections
← [11](../11-rag-and-ai-engineering/) · → [13](../13-mlops-security-and-research/). Networking →
APIs → tool calling → MCP → agents; OS → sandboxes → computer use
([`../../CONCEPT_MAP.md`](../../CONCEPT_MAP.md)). Phase detail:
[phase-12](../../curriculum/phases/phase-12-agents-and-computer-use.md).
