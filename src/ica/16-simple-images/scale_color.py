from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

pic = Picture("../SampleImages/antiqueTractors.jpg")

def grayscale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

def weighted_scale(pic, w1, w2, w3):

    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = w1 * r + w2 * g + w3 * b
        new_pic.setColor(x, y, (lumin, lumin, lumin))
    return new_pic

gray_pic = grayscale(pic)
gray_pic.save("../SampleImages/antiqueTractors-grayscale.jpg")
gray_pic.explore()

# weighted scales
weighted_pic1 = weighted_scale(pic, 0.5, 0.25, 0.25)
weighted_pic2 = weighted_scale(pic, 0.8, 0.1, 0.1)
weighted_pic3 = weighted_scale(pic, 0.2, 0.6, 0.2)

weighted_pic1.explore()
weighted_pic2.explore()
weighted_pic3.explore()

keep_windows_open()

