def sum3(values):
    """Takes a list/tuple with at least 3 numeric values and returns
    the sum of the first three elements."""
    # checks
    assert type(values) in [list, tuple], "Input must be a list or tuple"
    assert len(values) >= 3, "Input must have at least 3 elements"
    assert type(values[0]) in [int, float], "First element must be a number"
    assert type(values[1]) in [int, float], "Second element must be a number"
    assert type(values[2]) in [int, float], "Third element must be a number"
    # assert type(values["hello"]) in [str], "Fourth element must be a number?"

    # add first 3 elements
    return values[0] + values[1] + values[2]


if __name__ == "__main__":
    print(sum3([5, 2, 8, -2, 6, 15]))   # ✅ works → 15
    # print(sum3([5, 2]))                 # ❌ error (not enough elements)
    # print(sum3(5))                      # ❌ error (not a list/tuple)
    # print(sum3(["h", "i", 1, 2, 3]))    # ❌ error (first 3 are not numbers)
    print(sum3([1, 2, 3, "h", "i"]))    # ✅ works → 6
    print(sum3([1.5, 2.5, 3.5]))        # ✅ works → 7.5 (floats)
