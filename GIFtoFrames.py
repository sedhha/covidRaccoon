# Reading an animated GIF file using Python Image Processing Library - Pillow
#Code taken from: https://pythontic.com/image-processing/pillow/extract%20frames%20from%20animated%20gif

from PIL import Image

from PIL import GifImagePlugin

 

imageObject = Image.open("walking_raccoon.gif")

print(imageObject.is_animated)

print(imageObject.n_frames)

 

# Display individual frames from the loaded animated GIF file
framess=1
for frame in range(0,imageObject.n_frames):

    imageObject.seek(frame)
    imageObject.save("img"+str(framess)+".png","PNG")
    imageObject.show()
    framess+=1
