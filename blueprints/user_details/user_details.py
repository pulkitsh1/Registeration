from flask import Flask, Blueprint,url_for,redirect,jsonify,request
from flask.views import MethodView
# from function import sign_up,sign_in,update,fetch,delete
import bcrypt,db

user_details_bp = Blueprint('userdetails',__name__)

salt = bcrypt.gensalt()

class UserOperation(MethodView):
    # def get(self):
    #     response = fetch.display_info()
    #     return jsonify(response[0]),response[1]
    def post(self):
        try:
            name = request.json['name']
            email = request.json['email']
            password = request.json['password']
            confirm_password = request.json['confirm_password']

            if name == None:
                return [{"error":"Name is required."}, 400]
            elif email == None:
                return [{"error":"Email is required."}, 400]
            elif password == None:
                return [{"error":"Password is required."}, 400]
            elif confirm_password == None:
                return [{"error":"Confirm Password is required."}, 400]

            if password != confirm_password:
                return [{"error":"Passwords do not match."},400]

            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

            entry = db.User_info(name=name, email=email, password=hashed)
            db.db.session.add(entry)
            db.db.session.commit()
            return [{"message":"User successfully registered."}, 200]
        except Exception as e:
            return [{"error":f"An error occurred: {str(e)}"}, 500]
    # def put(self):
    #     response = update.updateName()
    #     return jsonify(response[0]),response[1]
    # def delete(self):
    #     response = delete.delete()
    #     return jsonify(response[0]),response[1]

user_details_bp.add_url_rule('/user', view_func=UserOperation.as_view('useroperation'))

# @user_details_bp.route('/login')
# def login():
#     response = sign_in.login()
#     return jsonify(response[0]),response[1]