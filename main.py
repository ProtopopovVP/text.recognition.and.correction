import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('data/image3.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=config)

print(pytesseract.image_to_string(img, config=config))

