from flask import Blueprint, render_template, abort
import os
import csv
import sqlite3 as sql
DB1 = 'database/e-learning.db'

users = Blueprint('AnyName', __name__, url_prefix='/user', template_folder='../templates')

@users.route('/')
def show():
    return render_template("Home.html")
