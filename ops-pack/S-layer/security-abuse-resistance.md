# S-Layer — security and abuse resistance

## Purpose

This layer defines minimal defensive rules against agentic abuse:
prompt injection, tool injection, exfiltration, privilege escalation.

## Untrusted input rule

Any external content (web pages, emails, documents, user messages) is untrusted.

Untrusted input must not:
- grant authority
- override policy
- introduce new tool permissions

## Tool access constraints

- tools must be allowlisted
- domains/endpoints must be allowlisted when applicable
- secrets must never be directly readable by the model
- outputs must be validated before execution

## Exfiltration resistance

Authority must be denied or escalated if:
- requested output contains secrets or sensitive payloads
- tool output attempts to leak credentials
- the system cannot prove data minimization

## Non-goals

This layer does not prescribe:
- specific sandbox implementations
- secret management tooling
