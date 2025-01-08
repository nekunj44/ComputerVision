import cv2

img1 = cv2.imread("/home/nekunj44/Pictures/Screenshots/merc77.jpg", 1)
print(img1)
#it will output in form of [Blue Intensity, Green Intensity, Red Intensity] if coloured image
#[[]] means one complete row of pixels.
#second criteria number 0 - It will output a greyscale image.
#second criteria number 1 - It will output a colorful image. 
#second criteria number -1 - It will output a image as it is with alpha channel.
      #note - alpha channel is used for representing transparency or opacity in an image. It is a value between 0(Fully Transparent) and 255(Fully Opaque). 

print(img1.shape)
#it will output in form of (height/rows, width/columns, channel)
#channel can be 3 (if its colored image) or 1 (if its grayscale image)

cv2.imshow("newwindow", img1)
#it will show the passed image in a new window with specified name.
#without waitKey() it will not show the image, it will open image for a second and then close it.

cv2.waitKey()
#it will wait for any key to be pressed and then close the window.
#without the weightkey the window with passed image would simply open and close within a second.
#time can be passed in milliseconds as an argument to waitKey().

cv2.destroyAllWindows()
#Once a key is pressed, the program continues, and the window is closed using cv2.destroyAllWindows().

img2 = cv2.resize(img1, (200, 200))
#used to resize the image to specified height and width.

img3 = cv2.imread("/home/nekunj44/Pictures/Screenshots/merc77.jpg", 0)

k = cv2.waitkey()
if k == ord("s"):
    cv2.imwrite("/home/nekunj44/Pictures/Screenshots/merc77_greyscale.jpg", img3)
else:
    cv2.destroyAllWindows()
#saves the image if letter "s" is pressed and closes the window.

img4 = cv2.flip(img1, 0)
#0: Flip the image vertically (around the x-axis).
#1: Flip the image horizontally (around the y-axis).
#-1: Flip the image both horizontally and vertically (around both axes).
