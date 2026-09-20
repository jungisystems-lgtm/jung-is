# Repository instructions

These instructions apply to the entire Jung repository, including `frontend/` and `backend/`.

Before modifying a directory, read its local AGENTS.md and the applicable parent AGENTS.md files. Local instructions add context; they do not override the Engineering Constitution.

## Markdown language

- Write and edit all project-owned Markdown files in English. This includes README files, AGENTS.md files, architecture documents, ADRs, and any new documentation.
- Use English for headings, prose, tables, comments, and examples in Markdown. Keep established product names, code identifiers, commands, and file paths unchanged.
- When editing an existing Markdown file, translate any Spanish prose in the touched section so the document remains consistently in English.
- Do not translate application copy or source code solely to satisfy this documentation rule.

## Engineering context

Read `frontend/docs/engineering-constitution.md` before making architecture-level changes. Follow the more specific instructions in `frontend/AGENTS.md` when working on the frontend. Keep backend business capabilities in `jung-api` as that application is built.

## Change log

- Before finishing a task, append one entry per created, edited, moved, or deleted project-owned file to the repository-root agent-log.md.
- Each entry must contain an ISO 8601 timestamp with time zone, the agent name or task ID, a brief English summary, and the repository-relative file path.
- Use one bullet line per file in the log's Entries section, separated by blank lines; keep entries concise and in chronological order. Wrap the path in inline code so Markdown does not alter characters such as underscores.
- For a move or rename, record both the old and new paths in separate entries. Multiple files from one task may share a timestamp.
- Keep the log append-only. Correct an earlier entry with a new entry rather than rewriting history.
- Do not log generated files such as node_modules or .next, secret values, or customer personal data. Appending to agent-log.md does not need a separate entry every time; its creation or structural changes do.
- A file change is incomplete until its log entry has been added.
