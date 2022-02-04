from flask import Flask, render_template, request, session, redirect, flash, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from werkzeug.utils import secure_filename
#from flask_ngrok_st import run_with_ngrok
# from flask_mail import MAIL
import math
import os
import json
from datetime import datetime
from forms import ContactForm, AdminForm

# After changes in config.json restart server manually
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
#run_with_ngrok(app)
app.secret_key = 'super-secret-key'

app.config['UPLOAD_FOLDER'] = params['upload_location']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

'''smtp server configaration (But this is not in use)'''
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_pass'], 
)

app.config['SQLALCHEMY_DATABASE_URI'] = params['sqlite_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
from models import *
bcrypt = Bcrypt()

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page= int(page)
    posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]

    if (page == 1):
        prev = "#"
        next = "/?page="+ str(page+1)
        s_num = page
        e_num = page + 3
    elif(page == last):
        prev = "/?page=" + str(page - 1)
        next = "#"
        s_num = page - 2
        e_num = last + 1
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)
        s_num = page - 1
        e_num = page + 2

    return render_template('index.html', params=params, posts = posts, prev=prev, next=next, page=page, last=last, s_num=s_num, e_num=e_num)

@app.route("/post/<string:post_slug>", methods = ['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html', params=params, post = post)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        entry = Msg(name=(form.name.data), message = (form.message.data), date= (datetime.now()),email = (form.email.data) )
        db.session.add(entry)
        db.session.commit()
        flash("Your message has been sent", "success")
        return redirect((url_for('home')))
    return render_template('/contact.html', params=params, form=form)

@app.route("/about")
def about():
    return render_template('about.html', params=params)

@app.route("/search", methods = ['GET', 'POST'])
def search():
    q = request.args.get('q')
    search = "%{0}%".format(q)
    postsTitle =  Posts.query.filter(Posts.title.like(search))
    postsContent =  Posts.query.filter(Posts.content.like(search))
    posts = postsTitle.union(postsContent).all()
    if posts == []:
        flash("Your seach query not found, try some diffrent word", "warning")
        return redirect((url_for('home')))
    return render_template('search.html', params=params, posts = posts)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        return redirect("/dashboard")
    form = AdminForm()
    if request.method == 'POST':
        user = Admin.query.filter_by(name=(form.name.data)).first()
        if user and bcrypt.check_password_hash(user.password, (form.password.data)):
            session['user'] = user.name
            return redirect(session['url'])
        else:
            abort(405)
    return render_template('admin/login.html', params=params, form=form)

@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():   
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        posts = Posts.query.all()
        return render_template('admin/dashboard.html', params = params, posts = posts) 
        
    session['url'] = request.path
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        session.pop('user')
        return redirect('/dashboard')
    abort(403)

@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        post = Posts.query.filter_by(sno=sno).first_or_404()
        current_ssession  = db.session.object_session(post)
        current_ssession.delete(post)
        current_ssession.commit()
        # flash('deleted successfully')
        return '1'
    abort(403)

@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        if request.method == 'POST':
            title = request.form.get('title')
            tagline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno == '0':
                post = Posts(title=title, slug=slug, content=content, img_file=img_file, tagline=tagline, date=date)
                db.session.add(post)
                db.session.commit()
                flash("Post has been added successfully")
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.slug = slug
                post.content = content
                post.tagline = tagline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                flash("Post has been edited successfully")
                return redirect('/edit/'+sno)
        
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('admin/edit.html', params=params,post=post, sno=sno)
    abort(403)

def allowed_image(filename):
    if not "." in filename:
        return False
        
    ext = filename.rsplit(".",1)[1]
    if ext.lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

@app.route("/upload", methods = ['POST'])
def upload():
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        if(request.method=='POST'):
            f = request.files['file1']
            if f.filename == "":
                flash('No file selected')
            elif f and allowed_image(f.filename):
                f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename) ) )
                flash('Image successfully uploaded')
            else:
                flash('That file extension is not allowed, only png, jpg, jpeg allowed')
            return redirect('/dashboard')
        else:
            abort(405)
    abort(403)
    
@app.route("/msg", methods = ['GET', 'POST'])
def msg():
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        msgs = Msg.query.filter_by().all()
        return render_template('admin/msg.html',params=params, msgs = msgs) 

    session['url'] = request.path
    return redirect('/login',code=401)

@app.route("/msg/delete/<string:sno>")
def msgdelete(sno):
    if ('user' in session and session['user'] == (Admin.query.filter_by(name=session['user']).first()).name):
        msg = Msg.query.filter_by(sno=sno).first_or_404()
        current_ssession  = db.session.object_session(msg)
        current_ssession.delete(msg)
        current_ssession.commit()
        # flash('deleted successfully')
        return '1'
    abort(403)
    
@app.errorhandler(404)
def error_404(error):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def error_500(error):
    return render_template('error/500.html'), 500     

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
