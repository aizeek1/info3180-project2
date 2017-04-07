from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '$up3r$3cretkey'

UPLOAD_FOLDER = './app/static/imgs'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:project2@localhost/project2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)


from app import views