import pytesseract
from PIL import Image

img = Image.open('yzm1.jpg')
result = pytesseract.image_to_string(img)
print(result)