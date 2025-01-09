#Screen Recorder
import cv2 as c
import pyautogui as p
import numpy as np

#create resolution
rs = p.size()

#filename in which we store recording
fn = input("Please enter any filename and path")
#fix the frame rate 
fps = 60.0

#to save the video
fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fn, fourcc, fps, rs)

#create recording module
c.namedWindow("Live_Recording", c.WINDOW_NORMAL)

while True:
    img = p.screenshot()
    f = np.array(img)
    output.write(f)
    c.imshow("Live_Recording",f)
    if c.waitKey() == ord("q"):
        break

c.destroyAllWindows()
output.release()

