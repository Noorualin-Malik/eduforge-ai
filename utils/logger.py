"""Logging utilities for EduForge."""

from __future__ import annotations

import logging
import sys
from functools import lru_cache
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "eduforge.log"


@lru_cache(maxsize=1)
def get_logger(name: str = "EduForge") -> logging.Logger:
    """
    Return a configured application logger.

    The logger is created only once and reused throughout the project.

    Args:
        name: Logger name.

    Returns:
        Configured Logger instance.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger