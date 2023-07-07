"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, a smile face png
    :return: SimpleImage, a blur smile face png
    """
    # Todo: create a new blank img that is as big as the orignial one
    new_img = SimpleImage.blank(img.width, img.height)


    # loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            
            # Todo: get pixel of new_img at x,y
            new_pixel = new_img.get_pixel(x, y)

            # belows are 9 conditions of pixel filling, depending on pixels' x,y orientation. 
            
            if x == 0 and y == 0:
                p1 = img.get_pixel(x + 1, y)
                p2 = img.get_pixel(x + 1, y + 1)
                p3 = img.get_pixel(x, y + 1)

                new_pixel.red = (p1.red + p2.red + p3.red) / 3
                new_pixel.green = (p1.green + p2.green + p3.green) / 3
                new_pixel.blue = (p1.blue + p2.blue + p3.blue) / 3

            elif x == (img.width - 1) and y == 0:
                p1 = img.get_pixel(x - 1, y)
                p2 = img.get_pixel(x - 1, y + 1)
                p3 = img.get_pixel(x, y + 1)

                new_pixel.red = (p1.red + p2.red + p3.red) / 3
                new_pixel.green = (p1.green + p2.green + p3.green) / 3
                new_pixel.blue = (p1.blue + p2.blue + p3.blue) / 3

            elif x == 0 and y == (img.height - 1):
                p1 = img.get_pixel(x + 1, y)
                p2 = img.get_pixel(x + 1, y - 1)
                p3 = img.get_pixel(x, y - 1)

                new_pixel.red = (p1.red + p2.red + p3.red) / 3
                new_pixel.green = (p1.green + p2.green + p3.green) / 3
                new_pixel.blue = (p1.blue + p2.blue + p3.blue) / 3

            elif x == (img.width - 1) and y == (img.height - 1):
                p1 = img.get_pixel(x - 1, y)
                p2 = img.get_pixel(x - 1, y - 1)
                p3 = img.get_pixel(x, y - 1)

                new_pixel.red = (p1.red + p2.red + p3.red) / 3
                new_pixel.green = (p1.green + p2.green + p3.green) / 3
                new_pixel.blue = (p1.blue + p2.blue + p3.blue) / 3
 
            elif y == 0:
                p1 = img.get_pixel(x - 1, y)
                p2 = img.get_pixel(x - 1, y + 1)
                p3 = img.get_pixel(x, y + 1)
                p4 = img.get_pixel(x + 1, y + 1)
                p5 = img.get_pixel(x + 1, y)

                new_pixel.red = (p1.red + p2.red + p3.red + p4.red + p5.red) / 5
                new_pixel.green = (p1.green + p2.green + p3.green + p4.green + p5.blue) / 5
                new_pixel.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue) / 5

            elif y == (img.height - 1):
                p1 = img.get_pixel(x - 1, y)
                p2 = img.get_pixel(x - 1, y - 1)
                p3 = img.get_pixel(x, y - 1)
                p4 = img.get_pixel(x + 1, y - 1)
                p5 = img.get_pixel(x + 1, y)

                new_pixel.red = (p1.red + p2.red + p3.red + p4.red + p5.red) / 5
                new_pixel.green = (p1.green + p2.green + p3.green + p4.green + p5.blue) / 5
                new_pixel.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue) / 5

            elif x == 0:
                p1 = img.get_pixel(x, y - 1)
                p2 = img.get_pixel(x + 1, y - 1)
                p3 = img.get_pixel(x + 1, y)
                p4 = img.get_pixel(x + 1, y + 1)
                p5 = img.get_pixel(x, y + 1)

                new_pixel.red = (p1.red + p2.red + p3.red + p4.red + p5.red) / 5
                new_pixel.green = (p1.green + p2.green + p3.green + p4.green + p5.blue) / 5
                new_pixel.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue) / 5

            elif x == (img.width - 1):
                p1 = img.get_pixel(x, y - 1)
                p2 = img.get_pixel(x - 1, y - 1)
                p3 = img.get_pixel(x - 1, y)
                p4 = img.get_pixel(x - 1, y + 1)
                p5 = img.get_pixel(x, y + 1)

                new_pixel.red = (p1.red + p2.red + p3.red + p4.red + p5.red) / 5
                new_pixel.green = (p1.green + p2.green + p3.green + p4.green + p5.blue) / 5
                new_pixel.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue) / 5

            else:
                p1 = img.get_pixel(x - 1, y - 1)
                p2 = img.get_pixel(x, y - 1)
                p3 = img.get_pixel(x + 1, y - 1)
                p4 = img.get_pixel(x - 1, y)
                p5 = img.get_pixel(x + 1, y)
                p6 = img.get_pixel(x - 1, y + 1)
                p7 = img.get_pixel(x, y + 1)
                p8 = img.get_pixel(x + 1, y + 1)

                new_pixel.red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red + p7.red + p8.red) / 8
                new_pixel.green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green + p7.green + p8.green) / 8
                new_pixel.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue + p7.blue + p8.blue) / 8

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
