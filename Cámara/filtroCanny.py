import cv2
video_path = 'C:/Users/Harol/Desktop/video2.mp4'
capture = cv2.VideoCapture(video_path)

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        #Aplicar blur a frame
        blur = cv2.blur(frame, (5, 5))
        #Aplicar Canny a frame
        bordesCanny = cv2.Canny(frame, 100, 200)
        CannyBlur = cv2.Canny(blur, 100, 200)
        bordeCannyNOT = cv2.bitwise_not(CannyBlur)

        #Mostrar Ventanas
        cv2.imshow("Ventana", frame)
        cv2.imshow("Canny", bordesCanny)
        cv2.imshow("CannyBlur", CannyBlur)
        cv2.imshow("Canny NOT", bordeCannyNOT)

        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
