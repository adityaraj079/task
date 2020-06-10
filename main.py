import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Aditya\AppData\Local\Tesseract-OCR\tesseract.exe'   #Change the path with your tesseract ocr's path
from PIL import Image

img = Image.open('text.png')
text = tess.image_to_string(img)

print(text)
