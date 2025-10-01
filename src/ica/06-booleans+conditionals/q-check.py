"""
Create a function called has_q that takes in one input, a string. The function returns True if the
input string contains a lowercase q character.  Otherwise, it returns False.
"""

def has_q(name: str):
    if "q" in name:
        return True
    else:
        return False
print(has_q("q"))

# make sure the function works
if __name__ == "__main__":
  assert has_q("quick") == True        # assert is used to test whether the function works
  assert has_q("math") == False
  print("All tests passed!")





