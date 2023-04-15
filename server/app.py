from flask import Flask

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///demo.db'

if __name__ == '__main__':
    app.run( port = 5555, debug = True )