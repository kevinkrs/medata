from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db
from api import api
from create_real_data import create_mock_data

#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
#/// for relative location of db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(api)

#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


#create real data
# try:
#     with app.app_context():
#         db.create_all()
#         create_mock_data()
# except Exception as e:
#     print(e)



if __name__ == '__main__':
    app.run()
