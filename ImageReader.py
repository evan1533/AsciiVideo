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
