import pytesseract
from PIL import Image

image=Image.open('test1.png')

#将图片转文字
text=pytesseract.image_to_string(image)
print(text)