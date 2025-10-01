"""
Letter grades in the US are commonly assigned according to "deciles:" a score that is greater than or
equal to 90% is given an A, a score that is greater than or equal to 80%, but less than 90% is given a B,
a score similarly between 70% and 80% is a C, a score similarly between 60% and 70% is a D,
and anything below 60% is an F.

Write a function percent_to_letter that has one input parameter, ie, it should be passed a percentage,
which may be a floating-point number, as its input.  The function should return a string containing
the corresponding letter grade.

"""

def percent_to_letter(num: float):
    if  percent_to_letter >= 90:
        return "Congratulations you get an A"
    elif 90 < percent_to_letter >= 80:
        return "You got a B. Well done!"
    elif 80 < percent_to_letter >= 70:
        return "Good effort, you get a C"
    elif 70 < percent_to_letter >= 60:
        return "Well tried, you get a D"
    else:
        return num


if __name__ == "__main__":
  assert range_limit(8) == 8
  assert range_limit(-1) == 1
  assert range_limit(50) == 10
  print("All tests passed!")