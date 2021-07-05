"""Each number in the input.txt is added to the next number, eg: in the input file with numbers 1,2,3,4….., the result will look like 3,5,7,9…."""
from scripts.tracker import timeit


@timeit
def sum_next_nums(input):
    result = []
    for i, num in enumerate(input):
        try:
            result.append(num+input[i+1])
        except IndexError:
            return result
