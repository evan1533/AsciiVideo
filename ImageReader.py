import numpy as np
import cv2


class Image:
    def __init__(self, img: str):
        # Load a color image
        self.image = cv2.imread(img, cv2.IMREAD_COLOR)
        self.height, self.width, self.channels = self.image.shape

    def get(self, x: int, y: int):
        """
        Returns the RGB information of the pixel at (x, y) in the image

        @param x: x location of the desired pixel
        @type x: int
        @param y: y location of the desired pixel
        @type y: int
        @return: the r,g,b value of the pixel
        @rtype: list
        """

        return self.image[x, y]

    def display_image(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def pixel_map(self):
        return self.image

    def print(self, factor=10):
        i = 0
        while i < self.height:
            j = 0
            if i % 2 == 0 or i % 3 == 0:
                pass
            while j < self.width:
                if j % 2 == 0 or j % 3 == 0:
                    pass
                pixel = self.get(i, j);
                color = '\x1b[38;2;%d;%d;%dm' % (pixel[0], pixel[1], pixel[2])
                print(color, 'n', end='')
                j += 1*factor
            i += 1*factor
            print()
        print('\033[00m')

    def __iter__(self):
        self.iX = 0
        self.iY = 0
        return self

    def __next__(self):
        if self.iX < self.height-1:
            if self.iY < self.width-1:
                self.iY += 1
            else:
                self.iX += 1
                self.iY = 0

            # print(self.iX, self.iY)
            return self.get(self.iX, self.iY)
        else:
            raise StopIteration
