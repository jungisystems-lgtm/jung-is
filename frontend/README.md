# Jung web app

Jung's website and a reusable foundation for future sites. It uses Next.js, React, and TypeScript. Business capabilities belong in `jung-api`; this application owns presentation, page composition, and HTTP integration with that API.

## Requirements

- Node.js 20.9 or later
- npm

## Quick start

Run these commands from `frontend/`:

```powershell
Copy-Item .env.example .env.local
npm ci
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). The initial page works without `jung-api`. Set `JUNG_API_URL` in `.env.local` when a feature needs the API.

## Checks

```powershell
npm run lint
npm run format:check
npm run typecheck
npm run test
npm run build
```

`npm run check` runs all of these checks. `npm run format` applies the configured formatting. Keep `package-lock.json` in Git and use `npm ci` for clean installations and CI.

## Structure

| Path             | Responsibility                            |
| ---------------- | ----------------------------------------- |
| `src/app`        | Next.js routes, layouts, and metadata     |
| `src/components` | Reusable interface components             |
| `src/features`   | Interface features when real needs emerge |
| `src/config`     | Site copy, branding, and navigation       |
| `src/api`        | Typed HTTP access to `jung-api`           |
| `src/lib`        | Small shared utilities when needed        |
| `src/styles`     | Global styles                             |
| `tests`          | Behavior tests                            |
| `docs`           | Principles, architecture, and decisions   |

The initial copy and branding are provisional and live in `src/config/site.ts`. They do not represent future customer configuration. When `jung-api` exposes site content and configuration, this layer should consume that contract without duplicating business rules.

## Working documents

- [Engineering Constitution](docs/engineering-constitution.md): agreed engineering principles (draft v0.1).
- [Architecture](docs/architecture.md): current boundaries and system state.
- [ADRs](docs/adr/): specific decisions and their reasoning.
- [AGENTS.md](AGENTS.md): development agent instructions.

## Git

Initialize Git from the repository root, one level above `frontend/`, so frontend and backend share one history.
