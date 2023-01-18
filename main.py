import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('img_3.jpg')

_, img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV_YV12)

print(pytesseract.image_to_string(img))

cv2.imshow('image', img)
cv2.waitKey(0)
