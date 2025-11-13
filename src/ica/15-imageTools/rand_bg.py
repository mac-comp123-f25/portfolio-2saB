
from src.ica.helpers.imageTools import *
from random import randrange


def get_rand_bg():
    # Generate random RGB values between 0 and 255
    r = randrange(0, 256)
    g = randrange(0, 256)
    b = randrange(0, 256)

    # Create a 100x100 blank picture
    pic = Picture(100, 100)

    # Set all pixels to the random color
    pic.setAllPixels((r, g, b))

    # Return the picture
    return pic


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()
