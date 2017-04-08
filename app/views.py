"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, jsonify, flash
from flask_login import login_user, logout_user, current_user, login_required
from bs4 import BeautifulSoup
import requests
import urlparse
from image_getter import get_image
from forms import WishlistForm,WishlistLoginForm,ResetForm
import time
from werkzeug.utils import secure_filename
import random
from models import UserProfile
import hashlib


###
# Routing for your application.
###

# --------------- Routing Functions -----------------

@app.route('/', methods=["GET","POST"])
def startup():
    return  redirect(url_for('login'))
    
    # =============== Register Function ================
    
@app.route('/api/users/login', methods=["GET","POST"])
def login():
   form = WishlistLoginForm()
   if request.method == "POST" and form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        
        user = UserProfile.query.filter_by(email=email, password=password).first()
        if user is not None:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('home'))
        else:
            flash('E-mail or Password is incorrect.', 'danger')
   flash_errors(form)
   return render_template("login.html",form=form)
    
@app.route('/api/home')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/api/thumbnails', methods=["GET"])
def thumbnails():
    return jsonify(thumbnails=get_image())
    
    # =============== Register Function ================
    
@app.route('/api/users/register', methods=["GET","POST"])
def register():
    form = WishlistForm()
    file_folder = app.config['UPLOAD_FOLDER']
    if request.method == "POST" and form.validate_on_submit():
        fname = request.form['firstname']
        lname = request.form['lastname']
        username = request.form['username']
        userid = randomnum()
        email=request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        secretques=request.form['secretques']
        secretans=request.form['secretans']
        image = request.files['image']
        accept_tos=request.form['accept_tos']
        created=time.strftime("%-d,%b,%Y")
        filename = secure_filename(image.filename)
        image.save(os.path.join(file_folder, filename))
        hash_num = random.randrange(10,9999)
        hash_number=str(hash_num)
        password_hash=  create_hash(password,hash_number )
    
        user = UserProfile(fname, lname, username, userid, email, password_hash, hash_number, secretques, secretans, gender, filename, accept_tos, created)
        db.session.add(user) 
        db.session.commit()
        
        flash ('Profile Created')
        return redirect (url_for('login'))
    flash_errors(form)
    return render_template("register.html",form=form)
    
    # --------------- Random Functions -----------------
    
    
def create_hash(password, hash_num):
    new_password = password + hash_num
    return hashlib.md5(new_password).hexdigest()
    
def randomnum():
    ran = random.randrange(1000000, 1000001, 3)
    user = UserProfile.query.filter_by(userid=ran).first() # try this line without the query it should work if it doesn't you can alway put it back.
    #checks if ran is already in the database,if it exists it recalculates ran and returns that value
    if user:
        ran = random.randrange(1000000, 1000001, 5)
        return ran 
    else:
        #if ran does not already exist in the database it returns the original calculate ran
        return ran
    
@app.route('/api/users/{userid}/wishlist', methods=["GET","POST"])
def user_wishlist():
    if request.method == "GET":
        return render_template("addtolist.html") 
    return render_template("wishlist.html")  
    
@app.route('/api/users/{userid}/wishlist/{itemid}', methods=["DELETE"])
def view_thumbnails():
    return render_template('thumbnails.html')
    
@app.route('/reset', methods=["GET","POST"])
def reset():
    form=ResetForm()
    if request.method == "POST" and form.validate_on_submit():
        email = request.form['email']
        secretques=request.form['secretques']
        secretans=request.form['secretans']
        return redirect (url_for('resetpass'))
    flash_errors(form)
    return render_template("reset.html",form=form)
    
@app.route('/reset/newpass', methods=["GET","POST"])
def resetpass():
    return render_template("resetpass.html")
###
# The functions below should be applicable to all Flask apps.
###
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')
            
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8081")
