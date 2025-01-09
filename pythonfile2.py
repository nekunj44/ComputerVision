import cv2

cap = cv2.VideoCapture("/home/nekunj44/Videos/redbullvsferrari.mp4")
#The cv2.VideoCapture() function in OpenCV is used to capture video streams either from a video file or directly from a connected camera 
#(webcam or other camera devices). It provides an interface to work with video data frame-by-frame, enabling tasks like video processing, recording, 
#or even real-time applications.
#Common options for source:
#    Integer (e.g., 0, 1):
#       Used to select a camera device.
#        0: Refers to the default camera (e.g., built-in webcam).
#        1: Refers to an external or additional camera.
#    String (e.g., video.mp4):
#        Used to load a video file from disk.
#        Example: "video.mp4", "path/to/video.avi".


#to save the video
#available format - DIVX, MP4, MJPG, XVID, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#it contains 4 parameters i.e name, above_variable, fps, resolution size
output = cv2.VideoWriter("/home/nekunj44/Videos/output.avi", fourcc, 20.0, (450, 450)) 
#isme ek extra parameter 0 pass karna padega agar greyscale video hai to.


while True: #while cap.isOpened(): for webcam
    ret, frame = cap.read() #it return two values, first is boolean value which gets stored in ret variable, second is the frame which gets stored in frame variable.
    #if ret == True: should be added here for webcam
    frame = cv2.resize(frame, (450, 450)) #it resizes the window containing the frame to the dimensions passed.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #it converts the frame to gray scale.
    cv2.imshow("frame", frame) #it will show the passed frame in new window with specified frame name.
    k = cv2.waitKey(500) #it will wait 500ms for next frame to load
    #output.write(frame) #it will write the frame to the output video
    if k == ord("q"):
        break


cap.release()
output.release()
cap.destroyAllWindows()

