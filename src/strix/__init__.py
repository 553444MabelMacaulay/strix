"""Strix - A lightweight task scheduling and workflow automation library."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("strix")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__author__ = "Strix Contributors"
__license__ = "Apache-2.0"

from strix.core import Strix
from strix.scheduler import Scheduler
from strix.task import Task

__all__ = [
    "Strix",
    "Scheduler",
    "Task",
    "__version__",
]
