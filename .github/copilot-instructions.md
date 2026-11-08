# CHARMD GitHub Copilot Instructions

Follow the repository-wide `AGENTS.md` operating contract. Before working, inspect the relevant documents under `docs/`.

## For every task

- Confirm the requested scope and acceptance criteria before editing.
- Work only on a task branch; never write directly to `main`.
- Prefer small, reviewable changes and deterministic implementations.
- Add tests and report exact commands and results.
- Do not invent benchmark results, provider capabilities, licensing rights, security guarantees, or release-gate status.
- Update the decision register when evidence changes an architecture decision; distinguish Proposed, Accepted, and Validated.
- Open a pull request; do not merge or deploy without explicit authorization.

## CHARMD constraints

- Standalone product; no Pyong Recordz dependency.
- Mobile-web-first DAW; vocal and instrumental AI generation.
- Full professional mastering suite and substantial plugin ecosystem are required scope.
- Preserve the explicit non-goals in the product constitution.
- GitHub and Cloudflare are the target platform direction. Do not add Vercel or Supabase.
- No secrets, credentials, user audio, or private project data in source control.
- No production provisioning, deployments, billing changes, permission changes, or external consequential actions without approval.
- During G1, deliver feasibility evidence and decision records before broad implementation.
