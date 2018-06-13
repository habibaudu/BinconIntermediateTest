'''
  Name : Habib Audu
  Bincom Test Answers
  email: auduhabib1990@gmail.com
'''
""".5.	If we have a confidence level of 0-100 on a Facebook user depending on the favorite pages, the groups they join, the number of female friends they have, the number of mutual friends they have, build a regression model that will tell us the confidence level of any Facebook user given all these parameters.
6.	Determine which of these parameters have a strong effect on the confidence level """
import mechanicalsoup
import time
import re
import json
import requests
my_facebook_friends_post_info=[]
groups_joined_by_my_facebookfriends=[]
mydictt={}

my_mutual_friends_info=[]
mydictt2={}
s = requests.Session()
from pprint import pprint


with open('cookies.json') as f:  #open the cookie file
    data = json.load(f)     

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
        matchstring = re.compile(r'EntRegularPersonalUser"><span>([a-zA-Z0-9\-\s]+)')#Extract mutual
        mobj = matchstring.search(i)
        matchstring2 = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
        mobj2 = matchstring2.search(i)
        matchstring3 = re.compile(r'class="_52eh">([a-zA-Z0-9.\-\s]+)')
        mobj3 = matchstring3.search(i)
        if mobj == None:
            continue
        else:
           mydictt2["name"]=mobj.group(1)
           mydictt2["info1"]=mobj2.group(1)
           mydictt2["info2"]=mobj3.group(1)
           my_mutual_friends_info.append(mydictt2.copy())
    mutual_no=len(mydictt["name"])
    return mutual_no



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
    jsondata = open("groups_joined_by_my_facebookfriends.json","w")
    json.dump(groups_joined_by_my_facebookfriends,jsondata)

    return jsondata




def get_female_friends():
    mydictt={}

    for cookie in data:
        s.cookies.set(cookie['name'], cookie['value']) #store the cookies in a session
    url = 'https://web.facebook.com/search/me/friends/females/intersect/?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s) #load the session
    browser.open(url)
    #go to bottom of page. force facebook to load up more friends
    #for x in range(0, 20):
    #browser.("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    page=str(browser.get_current_page())
    page = page.split('class="_32mo"')
    for i in page:
        matchstring = re.compile(r'EntRegularPersonalUser"><span>([a-zA-Z0-9\-\s]+)') #extracts female names
        mobj = matchstring.search(i)
        matchstring2 = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
        mobj2 = matchstring2.search(i)
        matchstring3 = re.compile(r'class="_52eh">([a-zA-Z0-9.\-\s]+)')
        mobj3 = matchstring3.search(i)
        if mobj == None:
            continue
        else:
           mydictt["name"]=mobj.group(1)
           mydictt["info1"]=mobj2.group(1)
           mydictt["info2"]=mobj3.group(1)
           my_mutual_friends_info.append(mydictt2.copy())
    female_no=len(mydictt["name"])
    return female_no


female_no=get_female_friends()
groupsjson=get_groups_joined_by_friends()
mutual_no=get_mutual()

import scipy as sp
import scipy.stats as st
import numpy as np

data=(female_no,mutual_no,groupsjson)


#taking Confidence Interval of 0.10 and confidence level of 90%

def mean_confidence_interval(data, confidence=0.90):
    data=(female_no,mutual_no,groupsjson)
    a = 1.0*np.array(data)
    n = len(a)
    loc, scale = np.mean(a), st.sem(a)
    st.t.interval(0.90, n-1, loc=np.mean(a), scale=st.sem(a))
    #h = scale * st.t._ppf((1+confidence)/2., n-1)
    #return m, m-h, m+h

    chosen_range = range(10,30)

    mean_confidence_interval(chosen_range)
    st.t.interval(0.90, len(a)-1, loc=np.mean(a), scale=st.sem(a))


mean_confidence_interval(data, confidence=0.90)