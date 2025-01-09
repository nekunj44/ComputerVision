#how to connect android device to laptop
import cv2

#declare variable to access camera
camera = "http://100.83.66.133:8080/video"
#declare cap to capture video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.open(camera)

#fourcc to save the video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("/home/nekunj44/Videos/output1.mp4", fourcc, 20.0, (450, 450))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (450, 450))
        cv2.imshow("frame", frame)
        output.write(frame)
        if cv2.waitKey() == ord("q"):
            break

cap.release()
output.release()
cv2.destroyAllWindows()
