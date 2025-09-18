"""Create a function, string_of_nums, that takes in a number as its input argument.
It should use an accumulator variable to build up a string.
The returned string should contain a string version of the numbers
from 1 up to the input value, separated by spaces.  Each time
through the loop, use the str function to convert the loop variable to
a string, and then use the plus operator to append a space and
that string to the accumulator"""

def string_of_nums(n):
    ans_str = ""   # initialize accumulator
    for x in range(1, n + 1):
        ans_str = ans_str + str(x) + " "
    return ans_str.strip()

print(string_of_nums(21))
