# Efficient Computations in Python

Instructions to do the task

•	Create a text file that has numbers from 1 to 100000, save it as 'input.txt'

•	In the Python code, read in the input file

•	Now, perform following operations in parallel :

o	Each number in the input.txt is multiplied by n, where n is configurable

o	Each number in the input.txt is added to the next number, eg: in the input file with numbers 1,2,3,4….., the result will look like 3,5,7,9….

o	For each operation, the start time and end time as well as every 100th result should be logged using the logging module of Python

•	This assignment will not be judged on the basis of correct functional result but on the basis of approach and efficiency of writing Python code

•	You should use Python as the programming language

•	Wherever possible, expose the service as an API.

•	It is fine if the given assignment is not completed in the given timeframe or does not meet your standards. We will discuss the content of what has been submitted.

## Assumptions

As we need to compute a lot, the operation is CPU bound -> python processes should be more effective than multiple threads. Let's check it running the code below containing 3 functions that run the code as it is, using threads and processes:

`python main.py`

(In the file out.log, it's easy to ctrl+f and find "Total amount of time.." for six cases to compare it)