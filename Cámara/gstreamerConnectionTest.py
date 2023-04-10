# Pipeline Gstreamer usando una webcam desde la raspberry Pi 4 model B:
# gst-launch-1.0 -v v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! jpegenc ! rtpjpegpay ! udpsink host=192.168.43.54 port=9999

# En resolución 2592x1944
# gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw,width=2592,height=1944 ! videoconvert ! x264enc ! rtph264pay ! udpsink host=192.168.43.54 port=9999


import cv2

cap = cv2.VideoCapture("udpsrc port=9999 ! application/x-rtp,media=(string)video,clock-rate=(int)90000,encoding-name=(string)JPEG,payload=(int)26 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
