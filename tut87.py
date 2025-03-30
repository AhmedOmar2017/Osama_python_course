#---------------------------------------------------------------------------
#--- Practical => Image Manipulation with pillow --------------------------
#---------------------------------------------------------------------------

from PIL import Image

#open an image
myImage = Image.open("F:test.jpg")

# Show image
myImage.show()

# Crop image
box = (500,500,1000,1000)

myNewImage = myImage.crop(box)

myNewImage.show()

#convert Mode
myConverted = myImage.convert("L")
myConverted.show()