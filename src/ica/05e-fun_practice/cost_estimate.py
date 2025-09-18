"""Suppose we want a program to help a company estimate costs for
putting in green roofs. The company needs to take in the dimension
of the roof space to be covered, in feet, and the cost per square
foot for a green roof installation. It should then print the number
of square feet for the roof, and the cost for that roof."""

def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

def rect_area(wid, len):
    return wid * len

def roof_cost(area, sqf_cost):
    return area * sqf_cost

wid = 1
len = 1
sqf_cost = 1

print(estimate_green_roof(wid, len, sqf_cost))