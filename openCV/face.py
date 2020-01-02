import cv2

face_cascade = cv2.CascadeClassifier(r"assets/facial_recog/haarcascade_frontalface_default.xml")
img = cv2.imread(r"assets/facial_recog/news.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor = 1.05,
minNeighbors=10,
)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0))


cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(type(faces))
print(faces)