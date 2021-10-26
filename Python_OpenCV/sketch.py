
import cv2 # import the library

varImage = cv2.imread("flowers.jpg") #created variable, invoke the imread method/funcion and pass the image file

varGrayImage = cv2.cvtColor(varImage, cv2.COLOR_BGR2GRAY) # convert to greysclae

varInvertImg = 55 - varGrayImage

varBlur = cv2.GaussianBlur(varInvertImg, (21, 21), 0)

varinvertBlur = 255 - varBlur

varSketched = cv2.divide(varGrayImage, varinvertBlur, scale=256.0 )

cv2.imshow("Originnal image", varImage)
cv2.imshow("Sketched image", varSketched)
cv2.waitKey(0)

cv2.exit()