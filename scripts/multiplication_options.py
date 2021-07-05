"""Each number in the input.txt is multiplied by n, where n is configurable"""
from scripts.tracker import timeit


@timeit
def multiply_in_list_comprehension(input, n):
    result = [num*n for num in input]
    return result
