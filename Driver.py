from ImageReader import Image
import sys

#myImage = Image('d35.jpg')
myImage = Image(sys.argv[1])

colors = myImage.pixel_map()
if len(sys.argv) > 2:
    myImage.print(int(sys.argv[2]))
else:
    myImage.print()

#print('\033[38;5;201m')
