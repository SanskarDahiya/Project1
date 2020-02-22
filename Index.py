from flask import Flask, render_template, request,session,redirect,g
from flask import Blueprint, abort
import os
import csv
import sqlite3 as sql
from FlaskScripts.users import users
DB1 = 'database/e-learning.db'

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(users)

"""
Variables
"""
d1="""We at Unthinkable Software are on the lookout for people who are passionate about building quality software products. In this regard, I am reaching out to you today to invite your college to register for our Campus Recruitment Program. At Unthinkable, we help our customers to disrupt faster by decreasing time-to-market via reducing the time gap between an idea and working software. Combining our experience of building 100+ software solutions and developing products using decoupled software components to reduce redundant code, we are in a unique position to take this unconventional approach to software development. Unthinkable is the software services brand of Applane Solutions LLP, and a group company of Daffodil Software."""
c1=["2017","DAFFODIL SOFTWARE LTD., GURUGRAM","http://www.unthinkable.co/","---","---,","WT/TR/HR","With in India","January","--- LPA","--- year"]
c2=["2018","DAFFODIL SOFTWARE LTD., GURUGRAM","http://www.unthinkable.co/","---","---","2WT/TR/HR","---","January","--- LPA","--- year"]
c3=["2019","DAFFODIL SOFTWARE LTD., GURUGRAM","http://www.unthinkable.co/",d1,"None","Tech Test(Online),Wrriten Test,TR,HR","Gurugram","January","4-5 LPA","1.5 year"]
C_List=[c1,c2,c3]

@app.route("/", methods=['GET', 'POST'])
def index():
    if 'user' in session:
        return render_template('home_logIN.html',data = session['user'])
    else:
        return render_template("Home.html")

@app.route('/getsession')
def getsession():
    data = session['user']
    return data[0]+data[1]+data[2]+data[3]


@app.route("/addblog", methods=['GET', 'POST'])
def addblog():
    global pqr
    if 'user' in session:
        data = 0
        data1 = session['user']
        if request.method=='POST':
            data = request.form
        with open('blogdata.csv','+a') as fd:
            fieldnames = ["Name","Email","Date","Title","Content"]
            writer=csv.DictWriter(fd, fieldnames=fieldnames)
            writer.writerow({"Name":str(data1[0]),"Email":str(data1[1]),'Date':str('12-12-2020'),"Title":str(data['title']),"Content":str(data['desc'])})
        pqr = []
        with open('blogdata.csv','rt')as f:
            data = csv.reader(f)
            for row in data:
                if(row):
                    pqr.append(row)
        return render_template("blog.html",data = pqr)
    else:
        return render_template('Home.html',data='PLease Login To add BLOG')

pqr = []
with open('blogdata.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        if(row):
            pqr.append(row)


@app.route("/blog/")
def blog_page():
    pqr = []
    with open('blogdata.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            if(row):
                pqr.append(row)

    return render_template("blog.html",data = pqr)


@app.route("/getdata/", methods=['POST', 'GET'])
def getdata():
    data = 0
    if request.method=='POST':
        data = request.form
        #print(data)
    if len(data)==4:
        try:
            con = sql.connect(DB1)
            cur = con.cursor()
            cur.execute('INSERT INTO userlogin VALUES ("'+str(data['name'])+'","'+str(data['email'])+'","'+str(data['password'])+'","'+str(data['contact'])+'");')
            con.commit()
            data = "Sucess"
        except Exception as e:
            data = e
            con.rollback()
    else:
        u = data['email']
        p = data['password']
        try:
            con = sql.connect(DB1)
            cur = con.cursor()
            cur.execute("select * from userlogin where mail like '"+u+"' AND pwd like '"+p+"'")
            con.commit()
            data = cur.fetchall()

            if data:
                session['user'] = data[0]
                return render_template('home_logIN.html',data = data)
            else:
                return render_template('Home.html',data='Invalid Username or Password')
        except Exception as e:
            con.rollback()
    return render_template('Home.html',data = data)


@app.route('/database/',methods=['POST','GET'])
def dataabse():
    data = 0
    if request.method=='POST':
        data = str(request.form['name'])
    try:
        con = sql.connect(DB1)
        cur = con.cursor()
        cur.execute(data)
        con.commit()
        data = "Sucess"
        data = cur.fetchall()
    except Exception as e:
        data = e
        con.rollback()
    return render_template('database.html',data = data)

if __name__ == '__main__':
   app.run(debug = True)
