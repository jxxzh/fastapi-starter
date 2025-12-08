<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# AGENTS instructions

## Project Knowledge

### Development Environment
- Use `uv` as the package manager.
  - dev server: `uv run dev`
  - prod server: `uv run start`
- Use `ruff` as the linter and formatter.
  - lint: `uv run ruff check`
  - format: `uv run ruff format`

### Core Stack
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.14+
- Pydantic V2: Data validation and settings management using Python type hints

### Project Architecture

### Code Style
- **Functional Programming**: Prefer functional programming over object-oriented programming
- **Declarative Programming**: Prefer declarative programming over imperative programming
- **Type Hints**: All function signatures must include complete type hints
- **Code Reusability**: Avoid code duplication through iteration and modularization

## Tips

- Always use context7 when I need code generation, setup or configuration steps, or library/API documentation. This means you should automatically use the Context7 MCP tools to resolve library id and get library docs without me having to explicitly ask.