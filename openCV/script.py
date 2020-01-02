import cv2
import numpy as np

img= cv2.imread(r"assets/galaxy.jpg", 0)

print("image dimensions: " + str((img).ndim))
print("image shape: " + str(img.shape))

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Galaxy", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("galaxy_resized.jpg", resized_img)