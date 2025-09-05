# Suppose you want to plant a garden bed with flowers. Each flower must sit in the middle of a 6 inch by 6 inch square to ensure it has enough room to grow (if next to another flower, it should be 6 inches away). Because you are obsessive about order, you want the flowers laid out in a perfect grid: rows and columns. If your garden bed is 10 feet long and 2 feet wide, how many flowers would you need to buy to make your grid?  You can compute how many rows of flowers will fit in the bed, and how many columns for each row. Then multiply them out to find the total number of flowers.

bed_len = 10
bed_width = 2
flower_len = 0.5
flower_width = 0.5
bed = bed_len * bed_width
flower = flower_len * flower_width
x = bed / flower
print (x)

bed_len = 30
bed_width = 3.5
flower_len = 0.5
flower_width = 0.5
bed = bed_len * bed_width
flower = flower_len * flower_width
y = bed / flower
print (x)