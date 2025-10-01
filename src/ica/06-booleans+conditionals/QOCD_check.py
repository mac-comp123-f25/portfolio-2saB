"""
Create a function called has_QOCD that takes in one parameter: a string. The function
returns True if the input string contains at least one of capital Q, capital O, capital C,
or capital D.  Otherwise, the function returns False if none of those four is present.
"""

def has_QOCD(name: str):
    if "Q" in name or "O" in name or "C" in name or "D" in name:
        return True
    else:
        return False
# print(has_q("Q, O, C, D"))

if __name__ == "__main__":
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")
