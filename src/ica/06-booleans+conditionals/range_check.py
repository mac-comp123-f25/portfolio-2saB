"""
Create a function called range_limit that has one input parameter, num.  If the number is
between 1 and 10, the function returns the number itself. If num is less than 1, the function
returns 1, and if num is greater than 10, the function returns 10. This way, it converts
any number given to it into the range from 1 to 10.

"""

def range_limit(num: int):
    if  num < 1:
        return 1
    elif num > 10:
        return 10
    else:
        return num


if __name__ == "__main__":
  assert range_limit(8) == 8
  assert range_limit(-1) == 1
  assert range_limit(50) == 10
  print("All tests passed!")
