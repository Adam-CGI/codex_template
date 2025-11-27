# Contributing to codex_template

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## Development Setup

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup**:
   ```bash
   git clone <your-fork-url>
   cd codex_template
   uv sync
   ```

3. **Install pre-commit hooks**:
   ```bash
   uv run pre-commit install
   ```

## Making Changes

### Before You Start
- Check existing issues and PRs to avoid duplicate work
- For major changes, open an issue first to discuss your approach

### Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Run tests**:
   ```bash
   uv run pytest --cov=package_name -v
   ```

4. **Check formatting and linting**:
   ```bash
   uv run black src tests examples
   uv run ruff check .
   ```

5. **Run pre-commit hooks**:
   ```bash
   uv run pre-commit run --all-files
   ```

### Code Style Guidelines

- **Line length**: 100 characters (configured for both Black and Ruff)
- **Python version**: 3.11+
- **Type hints**: Use type hints for function signatures
- **Docstrings**: Add docstrings for public functions and classes
- **Testing**: Write tests for new functionality

### Commit Messages

Use clear, descriptive commit messages:
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 72 characters
- Add detailed explanation in the body if needed

Example:
```
Add user authentication feature

- Implement JWT-based authentication
- Add login/logout endpoints
- Update tests for auth flow
```

## Testing

### Running Tests

```bash
# Run all tests with coverage
uv run pytest --cov=package_name -v

# Run specific test file
uv run pytest tests/test_main.py

# Run specific test
uv run pytest tests/test_main.py::test_build_greeting_trims_whitespace
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names that explain what is being tested
- Aim for high test coverage (90%+)

## Pull Request Process

1. **Update documentation** if you've changed functionality
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass** and code is properly formatted
4. **Update the README** if you've added user-facing changes
5. **Create a pull request** with a clear description of changes

### PR Checklist

- [ ] Tests pass (`uv run pytest`)
- [ ] Code is formatted (`uv run black src tests examples`)
- [ ] Linting passes (`uv run ruff check .`)
- [ ] Pre-commit hooks pass (`uv run pre-commit run --all-files`)
- [ ] Documentation updated (if applicable)
- [ ] CHANGELOG updated (if applicable)

## Questions?

If you have questions or need help, feel free to:
- Open an issue for discussion
- Ask in the pull request comments
- Check existing documentation and issues

Thank you for contributing! 🎉
