"""Each number in the input.txt is multiplied by n, where n is configurable"""
from scripts.tracker import timeit


@timeit
def multiply_in_list_comprehension(input, n=123, save_out=True):
    result = [num*n for num in input]
    if save_out:
        with open(f"multiply_by_{n}.txt", "a") as file:
            out_data = ', '.join([str(num) for num in result])
            file.write(out_data)
    return result
