#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo.py
@Time: 2019/12/5 15:02
@user：python-刘欢    
"""
# import  pytesseract
# from PIL import Image
#
# pytesseract.pytesseract.tesseract_cmd = 'E://Tesseract-OCR//tesseract.exe'
#
# tessdata_dir_config = '--tessdata-dir "E://Tesseract-OCR//tessdata"'
#
#
# im=Image.open(r'hello.png')
# print(im)
# print(pytesseract.image_to_string(im,lang='eng',config=tessdata_dir_config),111111)

from hashlib import md5


def encrypt_md5(s):
    new_md5 = md5()
    new_md5.update(s.encode(encoding='utf-8'))
    return new_md5.hexdigest()
print(encrypt_md5(encrypt_md5('http://m.120ask.com/jibing/bdxfy/202615.html')))

