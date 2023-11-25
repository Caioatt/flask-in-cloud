from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretpassword'

if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///motivos.db'



from crm.models import db

db.init_app(app)

with app.app_context():
    db.create_all()

from crm import routes
