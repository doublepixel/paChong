import pytesseract
from PIL import Image

img = Image.open('code3.jpeg')
result = pytesseract.image_to_string(img)
print(result)
