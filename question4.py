"""
Name: Habib Audu
Bincom test
Email:auduhabib1990@gmail.com

"""
"""4.	Extract the json for each of the above script, and save it into a database"""
import json
import psycopg2 #adaptor for postgres and pYthon

with open('groups_joined_by_my_facebookfriends.json') as f:
       Groupp = json.load(f)

def insert_groups_joined_by_my_facebookfriends():
    #creating a database connection
    conn = psycopg2.connect(database = "groupjoined", user = "postgres", password = "smirk***", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Groups
      (
      groupID SERIAL PRIMARY KEY,
      name_of_group    TEXT    NOT NULL,
      number_of_members  TEXT NOT NULL,
      friend_in_group  TEXT NOT NULL);''')
    print (" Table  created successfully")
    conn.commit()

    sql = """INSERT INTO Groups(name_of_group,number_of_members,friend_in_group)
             VALUES(%s,%s,%s);"""

    #extracting from json and inserting into database
    for KeY in Groupp:
      
        cur.execute(sql,(KeY['name_of_group'],KeY['number_of_members'],KeY['your_friends_in_group']))
        conn.commit()
          
    conn.close()

with open('cookies.json') as f:
       Cookkies = json.load(f)

def insert_cookiess_into_database():
    #creating a database connection
    conn = psycopg2.connect(database = "cookies", user = "postgres", password = "smirk***", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Cookiess
      (
      cookiesID SERIAL PRIMARY KEY,
      domain    TEXT    NOT NULL,
      expiry  TEXT NOT NULL,
      httpOnly  TEXT NOT NULL,
      name  TEXT NOT NULL,
      path  TEXT NOT NULL,
      secure  TEXT NOT NULL,
      value  TEXT NOT NULL);''')
    print (" Table  created successfully")
    conn.commit()

    sql = """INSERT INTO Cookiess(domain,expiry,httpOnly,name,path,secure,value)
             VALUES(%s,%s,%s,%s,%s,%s,%s);"""

    #extracting from json and inserting into database
    for KeY in Cookkies:
      
        cur.execute(sql,(KeY['domain'],KeY['expiry'],KeY['httpOnly'],KeY['name'],KeY['path'],KeY['secure'],KeY['value']))
        conn.commit()
          
    conn.close()

with open('mutual_friends.json') as f:
       MutualF = json.load(f)

def insert_mutual_friends():
    #creating a database connection
    conn = psycopg2.connect(database = "mutualfriends", user = "postgres", password = "smirk***", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE MutualFriends
      (
      friendID SERIAL PRIMARY KEY,
      name    TEXT    NOT NULL,
      info1  TEXT NOT NULL,
      info2  TEXT NOT NULL);''')
    print (" Table  created successfully")
    conn.commit()

    sql = """INSERT INTO Groups(name,info1,info2)
             VALUES(%s,%s,%s);"""

    #extracting from json and inserting into database
    for KeY in MutualF:
      
        cur.execute(sql,(KeY['name'],KeY['info1'],KeY['info2']))
        conn.commit()
          
    conn.close()

insert_cookiess_into_database()

insert_groups_joined_by_my_facebookfriends()

insert_mutual_friends()
