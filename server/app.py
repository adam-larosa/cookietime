
import ipdb
from flask import request, make_response, session
from flask_restful import Resource

from config import app, db, api, bcrypt

class Users( Resource ):
    def get( self ):
        #ipdb.set_trace()
        response = make_response( { 'hello': 'meow' }, 200 )
        response.set_cookie( 'meow name', 'meow value' )
        return response

    def post( self ):
        #ipdb.set_trace()
        return make_response( { 'hello': session['meow'] }, 200 )


api.add_resource( Users, '/users' )


if __name__ == '__main__':
    app.run(port=5555, debug=True)
