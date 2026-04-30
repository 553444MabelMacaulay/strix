"""Strix - A lightweight task scheduling and workflow automation library."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("strix")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__author__ = "Strix Contributors"
__license__ = "Apache-2.0"

# Personal fork - added Pipeline to top-level imports for convenience
from strix.core import Strix
from strix.scheduler import Scheduler
from strix.task import Task
from strix.pipeline import Pipeline

# Personal note: WorkflowRunner is also useful at the top level
from strix.workflow import WorkflowRunner

# Personal fork: expose __version__ and author info via a helper for quick debugging
def version_info() -> str:
    """Return a human-readable version string for quick debugging.

    Example::

        >>> import strix
        >>> print(strix.version_info())
        strix v1.2.3 (fork) — Strix Contributors, Apache-2.0
    """
    return f"strix v{__version__} (fork) — {__author__}, {__license__}"

__all__ = [
    "Strix",
    "Scheduler",
    "Task",
    "Pipeline",
    "WorkflowRunner",
    "version_info",
    "__version__",
]
