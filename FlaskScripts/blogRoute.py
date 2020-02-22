from flask import Blueprint, render_template, request, session, redirect
from FlaskScripts.database.database import blog as blogDB

blogs = Blueprint('blogRoute', __name__, url_prefix='/blog', template_folder='../templates')

@blogs.route("/")
def showBlogData():
    try:
        allblogs = blogDB.findblogs()
        return render_template("blog.html",data = allblogs)
        return 'Blogs are>> '+str(allblogs)
    except:
        return '/blog: Somthing Wrong'

@blogs.route("/addtoblog", methods=['GET', 'POST'])
def addBlogData():
    try:
        if request.method=='POST':
            data = dict(request.form)
            data['name'] = 'username'
            data['email'] = 'Email'
            data['date'] = 'Data-2020'
            data = blogDB.addblog(data)
            return redirect('/blog')
    except:
        return '/blog: Somthing Wrong'
