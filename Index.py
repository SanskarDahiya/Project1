from flask import Flask, render_template, request,session,redirect,g
import os

import sqlite3 as sql
DB1 = 'database/e-learning.db'

app = Flask(__name__)
app.secret_key = os.urandom(24)
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
    if request.method=='POST':
        session.pop['user',None]
        if request.form['password'] == 'password':
            session['user'] = request.form['email']
            return redirect('home_logIN.html')
    # return render_template("Companies.html",data=C_List,len = len(C_List)-1)
    return render_template("Home.html")

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Please Login First'

@app.route('/dropsession')
def dropsession():
    session.pop['user',None]
    return 'Dropped!'


@app.route('/home_logIN')
def home_logIN():
    if g.user:
        return render_template("home_logIN,html")
    return redirect('Home')

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route("/blog/")
def blog_page():
    return render_template("blog.html")


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
