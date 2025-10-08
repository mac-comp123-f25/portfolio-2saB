"""
Write a function change_start that takes a value and a list as inputs. The function should
not build a new list.  The function should modify the input list by changing the value
in the zero position to be the input value. Below is an example of what should happen.
"""
def change_start(value, list1):
  list1.append = [0],(value)
  return list1
list1 = [1, 2, 3, 4, 5, 6]
print(change_start(10, list1))


