"""
Name: Habib Audu
Bincom test
Email:auduhabib1990@gmail.com

"""
"""3. In order to avoid your Facebook account being locked, get the login cookies for your script."""
import mechanicalsoup
import requests
from http import cookiejar
s = requests.Session()
import time
import json
import re
from selenium import webdriver

chrome = webdriver.Chrome('C:/Users/HabibAudu/Desktop/chromedriver')

def get_Cookiess(chrome):
    chrome.get("https://www.facebook.com/login")
    email = chrome.find_element_by_id('email')
    email.send_keys('************@yahoo.com')
    password = chrome.find_element_by_id('pass')
    password.send_keys('******')
    password.submit()
    my_cookies =chrome.get_cookies()
    j = open("cookies.json","w")
    json.dump(my_cookies,j)
    chrome.close()

def use_cookiess():
    with open('cookies.json') as f:
       data = json.load(f)

    s = requests.Session()
    for cookie in data:
        s.cookies.set(cookie['name'], cookie['value'])
    url = 'https://web.facebook.com/search/me/friends/females/intersect/?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)


get_Cookiess(chrome)

use_cookiess()