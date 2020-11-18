import cv2
original = cv2.imread("resources/butterfly.jpg")
cv2.imshow("Original Image",original)
cv2.waitKey(0)

img = cv2.imread("resources/butterfly.jpg",0)# 0 is use to convert img into gray scale
cv2.imshow("gray image",img)
cv2.waitKey(0)

retn ,binary = cv2.threshold(img,120,250,cv2.THRESH_BINARY) #src,threshold value.max value,type of threshold
cv2.imshow("binary image",binary)
cv2.imwrite("resources/binary.jpg",binary)
cv2.waitKey(0)

