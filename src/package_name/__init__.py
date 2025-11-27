"""Codex template package exports."""

from importlib import metadata


def _distribution_name() -> str:
    """
    Return the distribution name matching this package.

    This derives the distribution identifier from the package namespace so renames
    stay consistent without manual edits.

    Returns
    -------
    str
        The normalised distribution name for the package.
    """

    return __package__.replace("_", "-")


try:
    __version__ = metadata.version(_distribution_name())
except metadata.PackageNotFoundError:  # pragma: no cover - during editable installs
    __version__ = "0.0.0"

__all__ = ["__version__"]
