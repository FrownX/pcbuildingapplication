from django.shortcuts import render, redirect
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
import requests
import time

requests.packages.urllib3.disable_warnings()


def cpu():

    session = requests.Session()
    session.headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://www.techhypermart.com/pc-parts/pc-parts-cpu-processors?page=3'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")
    contents = soup.find('div', {'id': 'content'})
    cpu = contents.find_all('div', {'class': 'product-thumb'})
    
    try:
        for i in cpu:

            # for tech in soup.find_all('a',{'class':'product-thumb'}): # return as a list
        
            partname = i.find('h4').text
            print(partname)
            price = i.find('p', {'class': 'price'}).text
            print(price)
            image = i.find('img')['src']
            print(image)


    except:
        pass

    

cpu()