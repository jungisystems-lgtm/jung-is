# Style instructions

This directory owns global styles and shared visual primitives.

- Keep layout, typography, color, and responsive rules understandable. Maintain accessible contrast and visible focus states.
- Keep brand choices configurable where practical so components remain reusable.
- Use component-local styles for truly local behavior rather than expanding global selectors unnecessarily.
- Do not add a styling framework or design-system dependency without a concrete need and review.
- Verify meaningful visual changes at relevant viewport sizes.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
