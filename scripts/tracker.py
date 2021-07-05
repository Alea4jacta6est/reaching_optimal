from functools import wraps
from time import perf_counter

from scripts.logger import logger


def timeit(f):
    """This decorator tracks running time of functions and logs 
    timing and final results

    Args:
        f (function): any function
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = f(*args, **kwargs)

        end = perf_counter()
        run_time = end-start
        logger.info(f'Time spent: {run_time:.8f} seconds')
        try:
            logger.info(f"Nth result: {result[-1]}")
        except TypeError:
            pass
        return result
    return wrapper
