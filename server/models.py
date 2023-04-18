from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from config import bcrypt

md = MetaData( naming_convention = {
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
} )

db = SQLAlchemy( metadata = md )
