import cv2
import numpy as np 
img = cv2.imread("resources/butterfly.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)

b,g,r = cv2.split(img)

zeros = np.zeros(img.shape[0:2],dtype="uint8")#shape function is used to store the height and width of image

cv2.imshow("Red image",cv2.merge([zeros,zeros,r]))
cv2.waitKey(0)

cv2.imshow("Green image",cv2.merge([zeros,g,zeros]))
cv2.waitKey(0)

cv2.imshow("Blue image",cv2.merge([b,zeros,zeros]))
cv2.waitKey(0)