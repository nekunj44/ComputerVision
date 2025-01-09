import cv2
import yt_dlp

# Get the video URL
url = "https://www.youtube.com/watch?v=WBiQulsQsqg"

# Use yt-dlp to extract the video URL
ydl_opts = {'format': 'best'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    video_info = ydl.extract_info(url, download=False)
    video_url = video_info['url']

# Capture video frames
cap = cv2.VideoCapture(video_url)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
