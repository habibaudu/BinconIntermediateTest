'''
  Name : Habib Audu
  Bincom Test Answers
  email: auduhabib1990@gmail.com
'''
"""2.	Write a script that crawls the groups joined by your Facebook friends"""
import mechanicalsoup
import time
import re
import json
import requests
groups_joined_by_my_facebookfriends=[]
mydictt={}
s = requests.Session()
from pprint import pprint

with open('cookies.json') as f:  #Open the cookies
    data = json.load(f)          #load the cookies into data

def get_groups_joined_by_friends():

    for cookie in data:
        s.cookies.set(cookie['name'], cookie['value']) #store the cookies in a session
    url = 'https://web.facebook.com/search/100004012632607/friends/groups?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s) #load the session
    browser.open(url)
    #go to bottom of page. force facebook to load up more friends
    #for x in range(0, 20):
    #browser.("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(30)
    page=str(browser.get_current_page())   #snap shot of the page
    page = page.split('class="_42ef"')     
    #print(page)
    for i in page:
        matchstring = re.compile(r'ref=br.rs">([a-zA-Z0-9\-\s]+)</a>')
        mobj = matchstring.search(i)
        matchstring2 = re.compile(r'(<div class="_pac")(.*?)([a-zA-Z0-9\s]+)<')
        mobj2 = matchstring2.search(i)
        matchstring3 = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
        mobj3 = matchstring3.search(i)
        if mobj == None:
            print("No match")
            continue
        else:
           mydictt["name_of_group"]=mobj.group(1)
           mydictt["number_of_members"]=mobj2.group(3)
           mydictt["your_friends_in_group"]=mobj3.group(1)
           groups_joined_by_my_facebookfriends.append(mydictt.copy())  #creates a json
    #pprint(groups_joined_by_my_facebookfriends)
    j = open("groups_joined_by_my_facebookfriends.json","w")
    json.dump(groups_joined_by_my_facebookfriends,j)