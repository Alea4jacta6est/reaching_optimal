import logging
import sys
from logging.config import dictConfig

FORMAT = "%(message)s"

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": FORMAT,
            }
        },
        "root": {"level": "INFO"},
    }
)
logger = logging.getLogger()

ff = logging.FileHandler('out.log')
ff.setLevel(logging.INFO)
logger.addHandler(ff)
