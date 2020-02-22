from flask import Flask, render_template, request,session,redirect,g
from FlaskScripts.usersRoute import users
from FlaskScripts.blogRoute import blogs

import os
import csv

app = Flask(__name__)
app.secret_key = os.urandom(24)

#all /user will redirect here
app.register_blueprint(users)
app.register_blueprint(blogs)


@app.route("/", methods=['GET', 'POST'])
def index():
    if 'user' in session:
        return render_template('home_logIN.html', data = session['user'])
    else:
        return render_template("Home.html")

# @app.route('/getsession')
# def getsession():
#     data = session['user']
#     return data[0]+data[1]+data[2]+data[3]


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
