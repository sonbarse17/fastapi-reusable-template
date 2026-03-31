"""
Application Logging Setup (logging.py)
======================================
Sets up structured logging pointing to `sys.stdout`. In modern containerized environments
(like Docker or Kubernetes), it is best practice to log to stdout and let the container orchestrator
handle log shipping (e.g., DataDog, ELK stack).
"""

import logging
import sys

def setup_logging():
    """Configure structured logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # You can add custom handlers here (e.g., file rotation, external sinks)
    logger = logging.getLogger("fastapi_starter")
    return logger

logger = setup_logging()
