"""
Write a Python function called every_other that takes a list as an input and returns a new
list that contains every other value from the original input list. HINT: The easiest solution
is to use list slicing–look it up to recall how it works. However, you could also loop over
the list or its indices and use an accumulator variable.
"""
def every_other(list1):
    list2 = []
    for x in range(0, len(list1), 2):
        list2.append(list1[x])
    return list2
print(every_other([1, 2, 3, 4, 5, 6]))


"""
Write a Python function sum_positive that takes a list of numbers as an input and 
returns the sum of the positive numbers.
"""
def sum_positive(list1):
    total = 0
    for x in list1:
        if x > 0:
            total += x
    return (total)
print(sum_positive([-1, 2, -5, 4, 5, 6]))