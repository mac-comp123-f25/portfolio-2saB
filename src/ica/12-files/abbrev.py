"""
function called print_abbrev that takes one input which represents the name of a text file.
Your function should (1) open the file for reading, (2) read in the lines of the file using
the for loop technique, (3) slice just the first 20 characters of each line maybe using slicing operator,
(4) print the shortened string, and (5) close the file after all is done. Below is a sample call and what it should produce.
"""

def print_abbrev(filename):
    file_in = open(filename, 'r')
    count = 0
    for text_line in file_in:
        text_line = text_line.strip()[:20]
        print("Line", count, ":", text_line)
        count += 1
    file_in.close()
print_abbrev("../TextFiles/alice.txt")






