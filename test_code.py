# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:51:01 2023

@author: ZREN9
"""

import easyocr

reader = easyocr.Reader(['en'],gpu=False) # this needs to run only once to load the model into memory
result = reader.readtext('C:/Users/zren9\Desktop\Zren9_Automate_Coding\OpenCv/image.png')
for i,j,k in result:
    if k < 0.9:
        print(i,j,k)