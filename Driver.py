from ImageReader import Image

myImage = Image('d35.jpg')
colors = myImage.pixel_map()

'''for pix in myImage:
    print(pix)'''

print(colors[100, 100])
for col in colors:
    print(col)
