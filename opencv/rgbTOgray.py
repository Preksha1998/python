import cv2
img = cv2.imread("resources/butterfly.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("GrayScaleImage",gray_img)
cv2.imwrite("resources/grayimg.jpg",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()