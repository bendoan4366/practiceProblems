import cv2, time

video = cv2.VideoCapture(0)

frame_count = 0

while True:
    frame_count = frame_count + 1
    check, frame = video.read()

    #print(check)
    #print(frame.shape)
    #time.sleep(2)
    
    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("Total Frames Captured: " + str(frame_count))
