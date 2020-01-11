import cv2, time

base_frame = None
video = cv2.VideoCapture(0)

while True:

    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0)

    if base_frame is None:
        base_frame = gray
        continue

    delta_frame=cv2.absdiff(base_frame,gray)

    threshold = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2)

    cnts, hierarchy = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) > 1000:
            continue
        else:
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3) 
    
    cv2.imshow("Gray", gray)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


print()
