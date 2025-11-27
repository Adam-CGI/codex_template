# AI Agent Instructions

This document provides guidance for AI coding agents (like GitHub Copilot, Cursor, etc.) when working with this repository.

## Project Overview

This is a Python project template.

- Primary code lives under `src/<package_name>/`.
- Tests are in the `tests/` directory.
- Notebooks (experiments, analysis) live under `notebooks/`.
- Example usage scripts live in `examples/`.
- Additional resources (data, docs) may live in `data/`, `docs/` as needed.

## Tooling & Workflow

### Dependency & Virtual-Environment Management

Managed via `uv`. Run the following to install or sync dependencies:

```bash
uv sync
```

### Installing or Adding Dependencies

Use `uv add <dependency>` (or `uv add -d <dev-dependency>` for dev tools).

### Run Package / CLI Entry Point

If defined:

```bash
uv run <console_script_name>
```

or explicitly:

```bash
uv run python -m <package_name>.main
```

### Run Tests

```bash
uv run pytest --cov=<package_name>
```

### Code Formatting

```bash
uv run black src tests examples
```

### Lint / Static Analysis

```bash
uv run ruff check .
```

### Pre-commit Hooks

Before committing, ensure hooks are installed, then run:

```bash
pre-commit install
pre-commit run --all-files
```

### Build / Packaging

If publishing, use your build backend (e.g. `hatchling`, or as configured in `pyproject.toml`):

```bash
uv build
```

## Coding Conventions & Style

### British English

Use British English spelling and grammar in comments, docstrings, README, and other documentation.

### Docstrings

Follow NumPy-style docstrings for functions, classes, and modules. Example template:

```python
def func(arg1: int, arg2: str) -> float:
    """
    Short summary of what the function does.

    Extended description (if needed).

    Parameters
    ----------
    arg1 : int
        Description of arg1.
    arg2 : str
        Description of arg2.

    Returns
    -------
    float
        Description of the return value.
    """
    ...
```

### Naming Conventions

- Use `snake_case` for variable, function, and module names.
- Use `PascalCase` for class names.

### Type Hints

Use type hints wherever feasible (especially for public APIs).

### Code Style Principles

- Prefer pure / functional-style logic for core functionality; keep side-effects (I/O, state mutations) isolated in minimal, well-documented modules.
- Avoid placeholders, commented-out stubs, or fallback "dummy" implementations — prefer working, testable code.

## Testing & Type Safety

- For every public or non-trivial function / module, provide corresponding test(s) in `tests/`.
- Test files should follow the naming pattern `test_*.py`.
- Tests should import from the installed package (after `uv sync`), not via relative file imports.
- If adding functionality, always add or update tests accordingly.
- If using type hints, optionally enforce static analysis (via `ruff`, `mypy`, or equivalent).

## Notebook & Example Code Guidelines

- Notebooks in `notebooks/` are allowed for experiments, data analysis, documentation, or prototyping.
- Before committing notebooks, clear outputs (e.g. via `nbstripout`) to avoid large diffs, accidental sensitive output, or version control bloat.
- Notebooks are generally not part of the core library code — treat them as separate artifacts (experiments / docs).
- Example scripts in `examples/` should be minimal, illustrative, and reflect real usage — not placeholders.

## Commit / Pull-Request Guidelines & Hygiene

- Always run pre-commit hooks (formatting, linting, trailing spaces, etc.) before committing.
- Do not commit commented-out code, debugging code, or unused placeholders. Remove dead code instead.
- Do not add heavy dependencies casually — new dependencies must be justified and documented.
- For new features, ensure: docstrings, tests, updated documentation (README / docs), and adherence to style/conventions.
- Keep commits and PRs small, focused, and with clear descriptions.

## Agent / Contributor Roles

To clarify responsibilities and maintain structure when using AI assistance:

- **@dev-agent**: implements logic in modules, adhering to coding conventions.
- **@test-agent**: writes or updates tests for any new/changed functionality.
- **@doc-agent**: ensures docstrings, module/class-level documentation, README/docs are present and up to date.
- **@cleanup-agent**: after feature changes or additions, reviews and removes any placeholder code, debugging artifacts, or unnecessary files.

## Do Not / Avoid

- Leaving placeholder functions or classes without implementation.
- Committing global mutable state or side-effects mixed into core logic.
- Mixing business logic with CLI / I/O code in the same module — separate concerns cleanly.
- Ignoring linting / formatting / type-hints / docstring conventions.
- Using magic, hacks or overly dynamic code unless absolutely necessary — prefer clarity and simplicity.

## Using MCP Servers & External Tooling

This template supports the use of MCP (Model Context Protocol) servers. If you configure MCP clients and servers, use the guidance below:

When using LLM-based agents (e.g. for code generation, documentation, test generation, refactoring), you can leverage MCP servers to give the agent accurate, up-to-date context — for example:

- Use **Context7 MCP** to fetch live, version-specific documentation and code examples for libraries you depend on. This helps avoid hallucinated APIs or outdated patterns.
- Include comments or instructions in prompts to "use context7" (or other configured MCP server) when requesting tasks related to external libraries or APIs.

### Important Guidelines for MCP Usage

- For defined, self-contained project logic (your own modules), agents do not need external MCP context — rely on the local codebase and existing structure.
- Treat MCP usage as opt-in: specify clearly when external docs or tool context are necessary. Do not over-use; indiscriminate use may lead to context overload or unnecessary complexity.
- Always use trusted MCP servers and verify their configuration and version. Unsupported or untrusted servers may return incorrect context or exacerbate hallucinations / tool misuse.

## When to Create Sub-package or Module-specific Agent Guides

If your project evolves into a larger system (multiple sub-packages, microservices, domain-specific modules), consider adding sub-directory agent guides — e.g. `AGENTS.override.md` or a second-level `AGENTS.md` in that sub-folder — to document module-specific conventions (e.g. import policies, module-level dependencies, logging, side-effect rules, docs, etc.).

## Revision & Maintenance Notes

- Keep this AGENTS guide up to date — if you change configurations (e.g. add new tooling, upgrade formatting rules, change docstring style) reflect that here.
- Review periodically (especially before major releases) to ensure conventions remain consistent, tooling works, and the template remains clean.
- When collaborating or letting AI agents contribute, treat this AGENTS guide as the "source of truth" for conventions.
