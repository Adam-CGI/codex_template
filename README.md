# codex_template

An opinionated, Codex-inspired Python repo template that ships with linting, testing, and a tiny CLI so you can start building immediately.

## What's inside
- **uv** for reproducible environments and locked dependencies
- **hatchling** as the build backend for packaging
- **Pre-commit** with Black, Ruff (lint + format), and safety checks
- **Pytest** with coverage flags and a minimal example/CLI you can extend
- Single `src/` layout, console script (`codex-template`), and example usage

## Quick start

```bash
# Install all dependencies (including dev tools)
uv sync

# Run the CLI (installed as console script)
uv run codex-template --name "Codex User"

# Run the example script
uv run python examples/example_use.py

# Run tests with coverage
uv run pytest --cov=package_name -v
```

## Development workflow

```bash
# Format code
uv run black src tests examples

# Lint code
uv run ruff check .

# Auto-fix linting issues
uv run ruff check --fix .

# Format with Ruff
uv run ruff format .

# Install pre-commit hooks (first time only)
uv run pre-commit install

# Run pre-commit hooks manually
uv run pre-commit run --all-files
```

## Project layout
```
codex_template/
├── src/package_name/       # Library/CLI code (rename to your module name)
│   ├── __init__.py         # Package initialization
│   └── main.py             # CLI entry point
├── tests/                  # Pytest test suite
│   └── test_main.py        # Example tests
├── examples/               # Usage examples
│   └── example_use.py      # Simple example script
├── pyproject.toml          # Project metadata and dependencies
├── uv.lock                 # Locked dependency versions
├── .pre-commit-config.yaml # Pre-commit hook configuration
├── .gitignore              # Git ignore patterns
├── AGENTS.md               # AI agent instructions
├── LICENSE                 # MIT License
└── README.md               # This file
```

## Customizing for your project

1. **Rename the package**:
   ```bash
   mv src/package_name src/your_project_name
   ```

2. **Update `pyproject.toml`**:
   - Change `name` from `codex-template` to your project name
   - Update `description`, `authors`, and repository URLs
   - Update `[tool.hatch.build.targets.wheel]` packages path:
     ```toml
     [tool.hatch.build.targets.wheel]
     packages = ["src/your_project_name"]
     ```
   - Update `[project.scripts]` console script:
     ```toml
     [project.scripts]
     your-cli-name = "your_project_name.main:cli"
     ```

3. **Update imports**: Search and replace `package_name` with your module name in:
   - `tests/test_main.py`
   - `examples/example_use.py`
   - Any other files that import the package

4. **Update documentation**:
   - Edit `README.md` with your project description
   - Update `LICENSE` with your copyright holder
   - Customize `AGENTS.md` with project-specific instructions

5. **Re-sync dependencies**:
   ```bash
   uv sync
   ```

## Testing the template

After customization, verify everything works:

```bash
# Run tests
uv run pytest --cov=your_project_name -v

# Test the CLI
uv run your-cli-name --name "Test"

# Check formatting
uv run black --check src tests examples

# Check linting
uv run ruff check .

# Run the example
uv run python examples/example_use.py
```

## Adding dependencies

```bash
# Add a runtime dependency
uv add requests

# Add a dev dependency
uv add --group dev mypy

# Sync the environment
uv sync
```

## License

MIT License - see [LICENSE](LICENSE) for details.
