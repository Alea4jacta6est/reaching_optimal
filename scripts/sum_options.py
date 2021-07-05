"""Each number in the input.txt is added to the next number, eg: in the input file with numbers 1,2,3,4….., the result will look like 3,5,7,9…."""
from scripts.tracker import timeit


@timeit
def sum_next_nums(input, save_out=True):
    result = [num+input[i+1] for i, num in enumerate(input) if i < len(input)-1]
    if save_out:
        with open("sum_up.txt", "a") as file:
            out_data = ', '.join([str(num) for num in result])
            file.write(out_data)
    return result