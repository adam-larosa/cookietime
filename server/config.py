from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from sqlalchemy import MetaData
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = '>C\xbe\x0c\x83\xf8\xbf\x03\x0eT.[\xb3Pzu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

md = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata = md)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

CORS(app)
bcrypt = Bcrypt( app )
