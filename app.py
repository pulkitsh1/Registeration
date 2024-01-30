from flask import Flask,jsonify
from blueprints.user_details.user_details import user_details_bp
from flask_sqlalchemy import SQLAlchemy
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:iamthe13002@localhost:3306/data'
db.init_app(app)
app.register_blueprint(user_details_bp)

# @app.route('/', methods=['POST'])
# def add():
#     response = sign_up.registeration()
#     return jsonify(response[0]),response[1]
    
# @app.route('/login', methods=['POST'])
# def login():
#     response = sign_in.login()
#     return jsonify(response[0]),response[1]
    
# @app.route("/updateName", methods=['POST'])
# def updateName():
#     response = update.updateName()
#     return jsonify(response[0]),response[1]

# @app.route('/display_info', methods=['GET'])
# def display_info():
#     response = fetch.display_info()
#     return jsonify(response[0]),response[1]

# @app.route('/delete', methods=['POST'])
# def remove_user():
#     response = delete.delete()
#     return jsonify(response[0]),response[1]
    

if __name__ == '__main__':
    app.run(debug=True)
