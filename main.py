import multiprocessing as mp

from scripts.multiplication_options import multiply_in_list_comprehension
from scripts.sum_options import sum_next_nums
from scripts.tracker import timeit
from scripts.logger import logger

filename = "input.txt"
with open(filename) as file:
    data = file.read().split(", ")
    numbers_list = [int(num) for num in data]


@timeit
def run_step_by_step(numbers_list, n=None, func=multiply_in_list_comprehension, start_index = 0, step = 100, save_out=True):
    """The function that multiplies numbers in list with n
    where n is a configurable number

    Args:
        start_index (int, optional): start index in a list. Defaults to 0.
        func: function to run step by step
        step (int, optional): number of elements in a batch to be processed per step. Defaults to 100.
        n (int, optional): multiplier for every num in the list.
        save_out (bool): save to file or not 

    Returns:
        final (list): the result of multiplication 
    """
    final = []
    for i in range(start_index, len(numbers_list), step):
        if n:
            result = func(numbers_list[i: i+step], n)
        else:
            result = func(numbers_list[i: i+step])
        final.extend(result)
    if save_out:
        with open("output.txt", "w") as file:
            out_data = ', '.join([str(num) for num in final])
            file.write(out_data)
    logger.info("\nTotal amount of time:")
    return final

def run_in_parallel():
    pass


if __name__ == "__main__":
    run_step_by_step(numbers_list, func=sum_next_nums)
    run_step_by_step(numbers_list, n=100)
