# Git guide for Jung

The repository root contains frontend/ and backend/. Both applications share one Git history on the main branch.

- GitHub remote: [jungisystems-lgtm/jung-is](https://github.com/jungisystems-lgtm/jung-is)
- Remote name: origin
- Default working branch: main

## Clone on another machine

```powershell
git clone https://github.com/jungisystems-lgtm/jung-is.git
cd jung-is
```

Follow [frontend/README.md](frontend/README.md) and [backend/README.md](backend/README.md) to install each application's dependencies and local environment.

## Make a change

Work from the repository root. Read the applicable AGENTS.md files and add an entry to [agent-log.md](agent-log.md) for every project file changed.

```powershell
git status
git pull --ff-only origin main
git add README.md
git commit -m "Describe the change"
git push origin main
```

Replace README.md in the staging command with the actual paths you changed. Review git status and the staged diff before committing. Keep changes small and explain the reason in the commit message.

## What stays local

Do not commit environment files, secrets, local databases, virtual environments, node_modules, or build output. The application-specific .gitignore files cover these paths. Commit the example environment files instead.

## First publication

To publish a local main branch to an empty remote for the first time, use:

```powershell
git push -u origin main
```

Do not force-push to replace remote history. If Git reports that the remote has commits the local branch lacks, inspect and integrate them before pushing.
