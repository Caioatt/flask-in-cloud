from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretpassword'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///motivos.db'

from crm.models import db

db.init_app(app)

with app.app_context():
    db.create_all()

from crm import routes
