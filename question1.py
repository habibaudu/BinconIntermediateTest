'''
  Name : Habib Audu
  Bincom Test Answers
  email: auduhabib1990@gmail.com
'''
"""1.	Write a script that crawls posts of your Facebook friends."""

#Note
#The url for get post get_post() is problematic 
# so I did mutual get_mutual() friends along with it...

import mechanicalsoup
import time
import re
import json
import requests
my_facebook_friends_post_info=[]
mydictt={}
s = requests.Session()
from pprint import pprint


with open('cookies.json') as f:  #open the cookie file
    data = json.load(f)          #load it into data

def get_post():
    for cookie in data:
        s.cookies.set(cookie['name'], cookie['value'])  #store inside the session
    url = 'https://web.facebook.com/search/100004012632607/friends/stories-by?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)   #inters page without loging in

    #go to bottom of page. force facebook to load up more friends
    #for x in range(0, 20):
    #browser.("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(9)
 
    page=str(browser.get_current_page())  #gets snap shot of the page
    page = page.split('id="u_ps_0_3_i"')
    for i in page:
        matchstring = re.compile(r'show="1">([a-zA-Z0-9\-\s]+)') 
        mobj = matchstring.search(i)
        matchstring2 = re.compile(r'pContent">([a-zA-Z0-9.\-\s]+)')
        mobj2 = matchstring2.search(i)
        matchstring3 = re.compile(r'<span.*? data-ft.*?>([a-zA-Z0-9.\s]+)')
        mobj3 = matchstring3.search(i)
        if mobj == None:
            print("no match")
            continue

        else:

            mydictt["name"]=mobj.group(1)
            mydictt["How_long_ago"]=mobj2.group(1)
            mydictt["Post"]=mobj3.group(1)
            my_facebook_friends_post_info.append(mydictt.copy())

    j = open("female_friends.json","w")
    json.dump(my_facebook_friends_post_info,j)


my_mutual_friends_info=[]
mydictt={}

def get_mutual():
    s = requests.Session()
    for cookie in data:
        s.cookies.set(cookie['name'], cookie['value'])
    url = 'https://web.facebook.com/search/me/friends/100004012632607/friends/intersect?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)
    #go to bottom of page. force facebook to load up more friends
    #for x in range(0, 20):
    #browser.("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(9)
    page=str(browser.get_current_page())
    page = page.split('class="_32mo"')
    for i in page:
        matchstring = re.compile(r'EntRegularPersonalUser"><span>([a-zA-Z0-9\-\s]+)')
        mobj = matchstring.search(i)
        matchstring2 = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
        mobj2 = matchstring2.search(i)
        matchstring3 = re.compile(r'class="_52eh">([a-zA-Z0-9.\-\s]+)')
        mobj3 = matchstring3.search(i)
        if mobj == None or mobj2 == None:
            continue
        else:
           mydictt["name"]=mobj.group(1)
           mydictt["info1"]=mobj2.group(1)
           mydictt["info2"]=mobj3.group(1)
           my_mutual_friends_info.append(mydictt.copy())
    j = open("mutual_friends.json","w")
    json.dump(my_mutual_friends_info,j)