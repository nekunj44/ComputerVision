import cv2

img1 = cv2.imread("/home/nekunj44/Pictures/Screenshots/merc77.jpg")
print(img1)
#it will output in form of [Blue Intensity, Green Intensity, Red Intensity] if coloured image
#[[]] means one complete row of pixels.

print(img1.shape)
#it will output in form of (height/rows, width/columns, channel)
#channel can be 3 (if its colored image) or 1 (if its grayscale image)

cv2.imshow("newwindow", img1)
cv2.waitKey()

cv2.destroyAllWindows()