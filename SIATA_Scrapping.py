# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:00:08 2020

@author: squintra
"""
from IPython.display import Image
import requests
from bs4 import BeautifulSoup
from PIL import Image  
import PIL  
import shutil
import urllib.request  
import time
from datetime import datetime
import numpy as np
import cv2

#Captura de fotos
while True:
    time.sleep(300)
    now = datetime.now()
    mes=now.month
    day=now.day
    hour=now.hour
    minute=now.minute
    minute
    second=now.second
    actual = str(mes)+str(day)+str(hour)+str(minute)+str(second)
    actual
    bulerias_url = 'https://siata.gov.co/ultimasFotosCamaras/ultimacam_dep_bulerias.jpg'
    bs = requests.get(bulerias_url, stream = True)
    filename = "bulerias" + str(actual)+'.jpg'
    try:
        if bs.status_code == 200:
            bs.raw.decode_content = True
            urllib.request.urlretrieve(bulerias_url, filename)
            print('La imagen se descargo correctamente: ',filename)
        else:
            print('La imagen no se pudo descargar: ',filename)
    except Exception as e:
        print('Error')
        print(e)
        print('\n')
    sanjuan_url = 'https://siata.gov.co/ultimasFotosCamaras/ultimacam_san_juan.jpg'
    sj = requests.get(sanjuan_url, stream = True)
    filename = "san_juan" + str(actual)+'.jpg'
    try:
        if sj.status_code == 200:
            sj.raw.decode_content = True
            urllib.request.urlretrieve(sanjuan_url, filename)
            print('La imagen se descargo correctamente: ',filename)
        else:
            print('La imagen no se pudo descargar: ',filename)
    except Exception as e:
        print('Error')
        print(e)
        print('\n')
    terminal_url = 'https://siata.gov.co/ultimasFotosCamaras/ultimacam_terminal_norte.jpg'
    tn = requests.get(terminal_url, stream = True)
    filename = "terminal" + str(actual)+'.jpg'
    try:
        if tn.status_code == 200:
            tn.raw.decode_content = True
            urllib.request.urlretrieve(terminal_url, filename)
            print('La imagen se descargo correctamente: ',filename)
        else:
            print('La imagen no se pudo descargar: ',filename)
    except Exception as e:
        print('Error')
        print(e)
        print('\n')
    musicos_url = 'https://siata.gov.co/ultimasFotosCamaras/ultimacam_puente_musicos.jpg'
    pm = requests.get(musicos_url, stream = True)
    filename = "musicos" + str(actual)+'.jpg'
    try:
        if pm.status_code == 200:
            pm.raw.decode_content = True
            urllib.request.urlretrieve(musicos_url, filename)
            print('La imagen se descargo correctamente: ',filename)
        else:
            print('La imagen no se pudo descargar: ',filename)
    except Exception as e:
        print('Error')
        print(e)
        print('\n')
    feria_url = 'https://siata.gov.co/ultimasFotosCamaras/ultimacam_dep_feria_ganado.jpg'
    fg = requests.get(feria_url, stream = True)
    filename = "feria" + str(actual)+'.jpg'
    try:
        if fg.status_code == 200:
            fg.raw.decode_content = True
            urllib.request.urlretrieve(feria_url, filename)
            print('La imagen se descargo correctamente: ',filename)
        else:
            print('La imagen no se pudo descargar: ',filename)
    except Exception as e:
        print('Error')
        print(e)
        print('\n')
    sanjuanochenta_url = 'https://siata.gov.co/ultimasFotosCamaras/ultimacam_dep_san_juan_con_80.jpg'
    sjo = requests.get(sanjuanochenta_url, stream = True)
    filename = "san_juan_80" + str(actual)+'.jpg'
    try:
        if sjo.status_code == 200:
            sjo.raw.decode_content = True
            urllib.request.urlretrieve(sanjuanochenta_url, filename)
            print('La imagen se descargo correctamente: ',filename)
        else:
            print('La imagen no se pudo descargar: ',filename)
    except Exception as e:
        print('Error')
        print(e)
        print('\n')

#Pre procesamiento de imagenes
##Recorte Bulerias
feria_url = 'bulerias1012131229.jpg'
img = cv2.imread(feria_url)
print(img.shape)
imgCropped = img[200:600,0:800]
cv2.imshow("recorte",imgCropped)
cv2.waitKey(0)


#Grises
im = Image.fromarray(np.uint8(img))
img2 = im.convert('L')
image2=np.uint8(img2)
cv2.imshow("gris",image2)
cv2.waitKey(0)



