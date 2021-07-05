import multiprocessing as mp
import concurrent.futures
import time

from scripts.multiplication_options import multiply_in_list_comprehension
from scripts.sum_options import sum_next_nums
from scripts.tracker import timeit
from scripts.logger import logger


@timeit
def run_step_by_step(numbers_list, func = multiply_in_list_comprehension, start_index = 0, step = 100):
    """The function that creates batches and applies the function to them

    Args:
        numbers_list (list): an array with nums
        start_index (int, optional): start index in a list. Defaults to 0.
        func: function to run step by step
        step (int, optional): number of elements in a batch to be processed per step. Defaults to 100.
    """
    batches = [numbers_list[i: i+step] for i in range(start_index, len(numbers_list), step)]
    for batch in batches:
        func(batch)
    logger.info(f"\nTotal amount of time ({func.__name__}):")
    return 

@timeit
def run_multiprocessing(numbers_list, func = multiply_in_list_comprehension, start_index = 0, step = 100):
    """The function that creates batches and applies the function to them using multiprocessing

    Args:
        numbers_list (list): an array with nums
        start_index (int, optional): start index in a list. Defaults to 0.
        func: function to run step by step
        step (int, optional): number of elements in a batch to be processed per step. Defaults to 100.
    """
    num_cpu = mp.cpu_count()
    pool = mp.Pool(num_cpu)
    batches = [numbers_list[i: i+step] for i in range(start_index, len(numbers_list), step)]
    pool.map(func, batches)
    pool.close()
    logger.info(f"\nTotal amount of time using multiprocessing ({num_cpu}, {func.__name__}):")

@timeit
def run_multithreading(numbers_list, func=multiply_in_list_comprehension, start_index = 0, step = 100):
    """The function that creates batches and applies the function to them using thread pool

    Args:
        numbers_list (list): an array with nums
        start_index (int, optional): start index in a list. Defaults to 0.
        func: function to run step by step
        step (int, optional): number of elements in a batch to be processed per step. Defaults to 100.
    """
    batches = [numbers_list[i: i+step] for i in range(start_index, len(numbers_list), step)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(func, batches)
    logger.info(f"\nTotal amount of time using threads ({func.__name__}):")


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as file:
        data = file.read().split(", ")
        numbers_list = [int(num) for num in data]
    
    break_time = 3
    run_multithreading(numbers_list, func=sum_next_nums)
    time.sleep(break_time)
    run_step_by_step(numbers_list, func=sum_next_nums)
    time.sleep(break_time)
    run_multiprocessing(numbers_list, func=sum_next_nums)
    time.sleep(break_time)
    run_step_by_step(numbers_list, func=multiply_in_list_comprehension)
    time.sleep(break_time)
    run_multithreading(numbers_list, func=multiply_in_list_comprehension)
    time.sleep(break_time)
    run_multiprocessing(numbers_list, func=multiply_in_list_comprehension)

