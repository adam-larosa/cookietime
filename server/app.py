
import ipdb
from flask import request, make_response, session
from flask_restful import Resource

from config import app, db, api, bcrypt

class Users( Resource ):
    def get( self ):
        #ipdb.set_trace()
        response = make_response( { 'hello': session.get( 'meow' ) }, 200 )
        
        session[ 'meow' ] = 'assign this object an attribute'
        
        return response

    def post( self ):
        #ipdb.set_trace()
        return make_response( { 'hello': 'postmeow' }, 200 )


api.add_resource( Users, '/users' )


if __name__ == '__main__':
    app.run(port=5555, debug=True)
