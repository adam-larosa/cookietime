from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///demo.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False
migrate = Migrate( app, db )
db.init_app( app )
api = Api( app )


class Users( Resource ):
    def get( self ):
        return "meow"

api.add_resource( Users, '/users' )


@app.route( '/' )
def root():
    return 'website!\n'

if __name__ == '__main__':
    app.run( port = 5555, debug = True )