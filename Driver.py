from ImageReader import Image
import sys

myImage = Image('d35.jpg')
#myImage = Image('comp.jpg')

colors = myImage.pixel_map()
if len(sys.argv) > 1:
    myImage.print(int(sys.argv[1]))
else:
    myImage.print()

#print('\033[38;5;201m')