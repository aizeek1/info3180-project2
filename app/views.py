"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, jsonify, flash
from bs4 import BeautifulSoup
import requests
import urlparse
from image_getter import get_image
from forms import WishlistForm,WishlistLoginForm
import time
from werkzeug.utils import secure_filename
import random
#from models import UserProfile


###
# Routing for your application.
###

def startup():
    """Render website's startup page."""
    return render_template('startup.html')
@app.route('/')    
@app.route('/api/users/login', methods=["GET","POST"])
def login():
   form = WishlistLoginForm()
   if request.method == "POST" and form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
   flash_errors(form)
   return render_template("login.html",form=form)
    
@app.route('/api/home')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/api/thumbnails', methods=["GET"])
def thumbnails():
    return jsonify(thumbnails=get_image())
    
@app.route('/api/users/register', methods=["GET","POST"])
def register():
    form = WishlistForm()
    #file_folder = app.config['UPLOAD_FOLDER']
    if request.method == "POST" and form.validate_on_submit():
        fname = request.form['firstname']
        lname = request.form['lastname']
        username = request.form['username']
        userid = randomnum()
        email=request.form['email']
        gender = request.form['gender']
        image = request.files['image']
        created=time.strftime("%-d,%b,%Y")
        filename = secure_filename(image.filename)
        image.save(os.path.join(file_folder, filename))
        
        user = UserProfile(fname, lname,username,userid,email, gender,filename,created)
        db.session.add(user) 
        db.session.commit()
        
        flash ('Profile Created')
        return redirect (url_for('login'))
    flash_errors(form)
    return render_template("register.html",form=form)
    
def randomnum():
    ran = random.randrange(1000000, 1000001, 3)
    user = UserProfile.query.filter_by(userid=ran).first()
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
    
@app.route('/reset')
def reset():
    return render_template("reset.html")
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
