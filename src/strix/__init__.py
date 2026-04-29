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

__all__ = [
    "Strix",
    "Scheduler",
    "Task",
    "Pipeline",
    "WorkflowRunner",
    "__version__",
]
