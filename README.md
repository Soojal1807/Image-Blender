# Image-Blender
This is a image blender which is made possible with help of libraries like numpy , pillow , tkinter.
numpy was used to load image data.
pillow is a library that helps with visualization of the picture.
tkinter is used here to give GUI to the application.

Basically what we are doing in this application is taking image data of two separate images and combining them , which is actually superimposing them on top of each other.
There are a constraints that this code has:
1. Both images have to be same resolution because numpy is converting image data like greyscale values into an array .
  
2. To save the Blended_image you have to write anything in the message box , anything is acceptable , initially that message box was added to name the image in the start but that functionality is not working
right now, user can give image a name later in separate window that opens up.

