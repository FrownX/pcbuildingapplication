from django.shortcuts import render, redirect
from .models import Cpu
import shutil
import ntpath
import os.path
from decimal import *
import os
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import json
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
import time
import requests
requests.packages.urllib3.disable_warnings()


def cpu(request):
    
    session = requests.Session()
    session.headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://www.techhypermart.com/pc-parts/pc-parts-cpu-processors'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")
    contents = soup.find('div', {'id': 'content'})
    cpuu = contents.find_all('div', {'class': 'product-thumb'})
    
    
    for i in cpuu:

        try:
        # for tech in soup.find_all('a',{'class':'product-thumb'}): # return as a list
    
            name = i.find('h4').text
            
            cpuprice = i.find('p', {'class': 'price'}).text
          
            
            image = i.find('img')['src']
            


            media_root = 'C:/Users/Faris/Desktop/fyp/pcbuildingapplication/media'
            if not image.startswith(("data:image", "javascript")):
                local_filename = image.split('/')[-1].split("?")[0]
                r = session.get(image, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)

                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media_root)

            

        except:
            pass

        new_cpu = Cpu()
        new_cpu.partname = name
        new_cpu.price = cpuprice
        new_cpu.image = local_filename
        new_cpu.save()




    context = {
        'cpu' : Cpu.objects.all()
    }

    return render(request, 'cpu/cpuscrape.html', context)

def Cpulist(request):

    context = {
        'cpu': Cpu.objects.all()
    }
    
    return render(request, 'cpu/cpulist.html',context)