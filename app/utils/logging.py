import logging
import sys


def setup_logging(level=logging.INFO):
    """
    Global logging configuration.
    Call once at application startup.
    """
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def get_logger(name: str) -> logging.Logger:
    """
    Module-level logger.
    """
    return logging.getLogger(name)
