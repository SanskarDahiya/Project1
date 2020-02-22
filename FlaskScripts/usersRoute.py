from flask import Blueprint, render_template, abort, request,session,redirect,g

users = Blueprint('usersRoute', __name__, url_prefix='/user', template_folder='../templates')

@users.route('/')
def index():
    return render_template("Home.html")

@users.route('/add')
def adduser():
    return render_template("Home.html")

@users.route('/show')
def show():
    return render_template("Home.html")
