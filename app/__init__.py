from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '$up3r$3cretkey'

UPLOAD_FOLDER = './app/static/imgs'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hgpwjmelqiiupg:f28f97b9293671ab1dfa3245dedd22ce2ce847fc88d5f1f4dae22ae5186e1ed7@ec2-23-23-222-147.compute-1.amazonaws.com:5432/dc37ue1i9cq2si'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

from app import views