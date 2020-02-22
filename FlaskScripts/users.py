from flask import Blueprint, render_template, abort

users = Blueprint('AnyName', __name__,url_prefix='/cstm',template_folder='../templates')

@users.route('/')
def show():
    return render_template("Home.html")
