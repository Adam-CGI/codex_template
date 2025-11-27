from __future__ import annotations

import argparse
from collections.abc import Sequence

DEFAULT_NAME = "codex-template"


def build_greeting(name: str = DEFAULT_NAME) -> str:
    """
    Compose a friendly greeting that trims whitespace and falls back to a default.

    Parameters
    ----------
    name : str, default="codex-template"
        The name to include in the greeting.

    Returns
    -------
    str
        A greeting incorporating the provided name.
    """

    cleaned = name.strip() or DEFAULT_NAME
    return f"Hello from {cleaned}!"


def main(name: str | None = None) -> str:
    """
    Print a greeting to stdout and return it for further use.

    Parameters
    ----------
    name : str or None, optional
        Optional name to include; defaults to the template name when omitted.

    Returns
    -------
    str
        The greeting that was printed.
    """

    greeting = build_greeting(name or DEFAULT_NAME)
    print(greeting)
    return greeting


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lightweight CLI showcasing the Codex template layout."
    )
    parser.add_argument(
        "-n",
        "--name",
        default=DEFAULT_NAME,
        help="Name to include in the greeting.",
    )
    return parser


def cli(argv: Sequence[str] | None = None) -> int:
    """
    Parse CLI arguments and execute the greeting workflow.

    Parameters
    ----------
    argv : Sequence[str] or None, optional
        Command-line arguments to parse; defaults to `sys.argv` when not provided.

    Returns
    -------
    int
        Exit code indicating success (0) or failure.
    """

    args = _build_parser().parse_args(list(argv) if argv is not None else None)
    main(args.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
