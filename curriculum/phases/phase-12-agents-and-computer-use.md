# Phase 12 — Tool Calling, MCP, Agents, Browser & Computer Use

**Timeline:** ~12–16 weeks · **Module:** [12-agents-mcp-and-computer-use](../../modules/12-agents-mcp-and-computer-use/)

## Goal
Build tool-using agents **safely**, from a minimal loop up to browser, computer-use, and coding
agents. This is a major goal of the whole program.

## Prerequisites
Phase 11.

## Topics & required depth
- **The agent loop:** user request → goal interpretation → state → planning → tool selection →
  tool execution → observation → state update → next action → final response.
- **Agent design:** workflows vs agents, deterministic orchestration, tool calling, state, memory,
  planning, reflection, retries, error recovery, human-in-the-loop, permissions, multi-agent
  concepts, agent evaluation, agent reliability, excessive-agency risks.
- **MCP:** model/agent → MCP client → MCP server → tools/resources/prompts → external system; why
  a protocol layer helps; client/server responsibilities; tool discovery; schemas; resource
  access; authn/authz; permissions; validation; error handling; security boundaries; observability.
- **Browser & computer use:** HTML, DOM, CSS selectors, accessibility trees; browser automation
  (Playwright; Selenium concepts); screenshots; computer vision & OCR concepts; mouse/keyboard
  automation; OS APIs; sandboxes, containers, VMs; credentials, sessions, permissions; human
  approval; prompt injection (direct and **indirect**); destructive actions; audit logs; recovery.
- **Coding agents:** repository indexing, search, context retrieval, dependency tracing, planning,
  editing, patch generation, terminal execution, test feedback, compiler feedback, git diffs,
  sandboxing, permissions, context limits, evaluation, rollback.

## Safety (non-negotiable)
All browser/computer-use/coding-agent work starts in **local test folders, sample/controlled
pages, sandboxes, with disposable data and non-privileged accounts**. Require **explicit
approval** before deletion, external communication, account changes, purchases/payments,
production systems, credentials, personal data, privileged commands, or irreversible changes.
Teach and apply least privilege, allowlists, validation, audit logs, human approval, rollback.
See [`../../AGENT_RULES.md`](../../AGENT_RULES.md) §Safety.

## Hands-on labs
Define tools with JSON schemas; build the loop step-by-step; craft and then *defend against* a
prompt-injection attempt in a sandbox; drive a sample local webpage with Playwright.

## From-scratch implementation (progressive)
1. Minimal agent loop / framework (project #31)
2. MCP server and client (project #30)
3. Tool-calling assistant (project #29)
4. Browser automation agent (project #32)
5. Sandboxed computer-use agent (project #33)
6. Simplified coding agent (project #34)

## Major project
Project #34 — a simplified coding agent: read a small repo → locate files → propose a change →
modify code → run tests → inspect failures → retry safely → produce a final diff + explanation.

## Recommended resources
MCP docs (modelcontextprotocol.io); Playwright docs; Microsoft AI-Agents-for-Beginners;
OWASP LLM Top 10. (See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Build an agent loop from scratch; build an MCP server/client; explain and mitigate direct & indirect
prompt injection; demonstrate approval gates and rollback.

## Exit criteria
- A from-scratch agent loop, an MCP server/client, a browser agent, a sandboxed computer-use agent,
  and a simplified coding agent — all with safety controls.
- You can threat-model an agent and defend it.

## Common mistakes
- Giving an agent broad permissions "to make it work."
- Trusting tool output / page content as instructions (indirect injection).
- No audit log, no rollback, no human approval on destructive actions.

## Connection to next phase
Working agents → operate them in production, secure them, and study the field (Phase 13).
