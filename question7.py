'''
  Name : Habib Audu
  Bincom Test Answers
  email: auduhabib1990@gmail.com
'''
"""7.	Extract male and female friends of different Facebook users and build a table to hold them for data analysis . Build a classification model that will tell the gender of a Facebook user given the amount of male and female friends he has.

"""
      
import json
import mechanicalsoup
import time
import re
import requests
s = requests.Session()
data1 = []
data2 = []
data3 ={}

from pprint import pprint

with open('cookies.json') as f:
    data = json.load(f)
def friends_anali():
    for cookie in data:
        s.cookies.set(cookie['name'], cookie['value'])
    url = 'https://web.facebook.com/search/100004012632607/friends?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)
    #go to bottom of page. force facebook to load up more friends
    #for x in range(0, 20):
    #browser.("window.scrollTo(0, document.body.scrollHeight);")
    #browser.launch_browser()
    time.sleep(6)
    page=str(browser.get_current_page())
    gender =''
    page = page.split('class="_32mo"')
    for i in page:
        matchstring = re.compile(r'EntRegularPersonalUser"><span>([a-zA-Z0-9\-\s]+)')
        mobj = matchstring.search(i)
        if mobj == None:
            continue      
        else:
            dat = mobj.group(1)
            dat =dat.lower()
            dat =dat.split()
            dat=".".join(dat)
            browser.open('https://web.facebook.com/'+ dat +'/about?section=contact-info')
            page2 =str(browser.get_current_page())
            page2 = page2.split('class="_3pw9 _2pi4 _2ge8 _3ms8"')
            
            for i in page2:
               
                 matchstring2 = re.compile(r'<div><span class="_2iem">([a-zA-Z]+)')
                 mobj2 = matchstring2.search(i)
                 if mobj2 == None:
                    continue
              
                 else: 
                    
                    gender = mobj2.group(1)
       
            
            browser.open('https://web.facebook.com/'+ dat +'/friends')
            #browser.launch_browser()
            time.sleep(6)
            page3=str(browser.get_current_page())
            page3 = page3.split('class="_698"')
            friends = {} 
            for i in page3:
                matchstring3 = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
                mobj3 = matchstring3.search(i)
                if mobj3 == None:
                   continue      
                else:
                   
                   friends['name'] = mobj3.group(1)
                   dat2 = mobj3.group(1)
                   dat2 =dat2.lower()
                   dat2 =dat2.split()
                   dat2=".".join(dat2)
                   browser.open('https://web.facebook.com/'+ dat2 +'/about?section=contact-info')
                   page4 =str(browser.get_current_page())
                   page4 = page4.split('class="_3pw9 _2pi4 _2ge8 _3ms8"')
                   for i in page4:
                         matchstring5 = re.compile(r'<div><span class="_2iem">([a-zA-Z]+)')
                         mobj4 = matchstring5.search(i)
                         if mobj4 == None:
                            continue      
                         else:
                            friends['gender']=mobj4.group(1)
                            data1.append(friends.copy())
                        
                   data3['name'] = mobj.group(1)
                   data3['gender'] =gender
                           
                   data3['friend'] =data1
                   data2.append(data3.copy())
                            
                            
                
            # data3['name'] = mobj.group(1)
            # data3['gender'] =gender
            # data1.append(friends.copy())
            # data3['friend'] =data1
            # data2.append(data3.copy())
    
    print(data2)
    j = open("assign.json","w")
    json.dump(data2,j)

#friends_anali()




# Using logistic Regression
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def learn_gender():
    # Importing the dataset
    dataset = pd.read_csv('friend.csv')
    X = dataset.iloc[:, 2:].values
    y = dataset.iloc[:, 1].values

    # print(X)
    # print(y)

    #splitting into test and training set
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # print(X_train)
    # print(y_train)

    # Feature Scaling,No need for feature scaling because no much gap btw data set

    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    # Predicting the Test set results

    y_pred = classifier.predict(X_test)
    # print(X_test)
    # print(y_pred)

    #The machine has learned from the dataset 
    # that males tend to have more female friends than 
    # male friends and vice versal on facebook

    # so giving it a higher number of female friend it predict the gender to be male
    X_test =[[100,300]]
    y_pred = classifier.predict(X_test)
    print(X_test)

    print(y_pred)

    # And giving it a higher number of Male friends it predict the gender to be Female
    X_test =[[1000,300]]
    y_pred = classifier.predict(X_test)
    print(X_test)

    print(y_pred)

#learn_gender()

