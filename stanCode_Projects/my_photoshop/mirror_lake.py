"""
File: mirror_lake.py
Name: 陳大再
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: SimpleImage
    :return: SimpleImage, with mirror effect
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            b_p1 = b_img.get_pixel(x, y)
            b_p2 = b_img.get_pixel(x, b_img.height - y -1)
            b_p1.red = b_p2.red = pixel.red
            b_p1.green = b_p2.green = pixel.green
            b_p1.blue = b_p2.blue = pixel.blue
    return b_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
