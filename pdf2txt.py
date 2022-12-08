#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8 Dec 2022

@author: reg_user

"""
# import module
from PIL import Image

import numpy as np
# importing os module
import os

import pytesseract

from pdf2image import convert_from_path
#save pdf
pdf_name = input("Введите название PDF файла: ")

text_sum = ''
# Path jpg folder
path_jpg = os.path.join(pdf_name + '_jpg')
# Path txt folder
path_txt = os.path.join(pdf_name + '_txt') 
   
# Create the directory _jpg & _txt
os.mkdir(path_jpg)
os.mkdir(path_txt) 

print('Папки созданы....')

images = convert_from_path(pdf_name)

print('На конвертацию ' + str(len(images)) + ' страниц....')

for i in range(len(images)):
    # Save pages
    images[i].save(pdf_name + '_jpg/' + pdf_name + str(i) +'.jpg', 'JPEG')
    #open image
    imgIm = np.array(Image.open(pdf_name + '_jpg/' + pdf_name + str(i) +'.jpg'))
    #convert image to text
    text = pytesseract.image_to_string(imgIm, lang = 'rus')
    
    text_sum += text
    #save txt
    with open(pdf_name + '_txt/' + pdf_name + str(i) +'.txt', 'w') as f:
                
        f.write(text)
        
        print('Страница ' + str(i) + ' конвертирована....')
        
with open(pdf_name +'.txt', 'w') as fs:
    
    fs.write(text_sum)
        
print('Завершено....')