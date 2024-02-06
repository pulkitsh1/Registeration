from flask import jsonify,request
from flask.views import MethodView
import bcrypt
from db import db,User_info
from schemas import DetailsSchema,SignupSchema, LoginSchema
from flask_smorest import Blueprint
from marshmallow import ValidationError

user_details_bp = Blueprint('userdetails',__name__)
salt = bcrypt.gensalt()


class UserOperation(MethodView):
    
    def get(self):
        try:
            res = User_info.query.all()
            if not res:
                    return {'error': 'No Information found'}, 404
            schema = DetailsSchema(many=True)
            return {"Info":schema.dump(res)}
        
        except Exception as e:
            return {f'Error: {str(e)}'},500

    def post(self):
        try:
            schema = SignupSchema()
            req_data = schema.load(request.json)
            hashed = bcrypt.hashpw(req_data.get('password').encode('utf-8'), salt)
            
            entry = User_info(name=req_data.get('name'), email=req_data.get('email'), password=hashed)
            db.session.add(entry)
            db.session.commit()
            return {"message":"User successfully registered."}, 200
        except Exception as e:
            return {"Error":f"{str(e)}"}, 500
    
    def put(self):
        try:
            schema = DetailsSchema(partial = True)
            get_data = schema.load(request.json)
            email_exist = User_info.query.filter_by(email=get_data.get('email')).first()

            if email_exist is None:
                return {'error':'Email does not exist in the database'}, 404
            
            email_exist.name = get_data.get('name')
            db.session.commit()

            return {'message': "Success"}, 200
        except Exception as e:
            return {'Error': f'{str(e)}'},500
        
    def delete(self):
        try:
            schema = LoginSchema()
            req_data = schema.load(request.json)

            res = User_info.query.filter_by(email=req_data.get('email')).first()
            email_exist = res.password

            if email_exist is None:
                return {'error': 'Email does not exist in the database'}, 404

            stored_pass = email_exist.encode('utf-8')
            provided_pass = req_data.get('password').encode('utf-8')
            check_pass = bcrypt.checkpw(provided_pass, stored_pass)

            if not check_pass:
                return {'Incorrect password'}, 401
            
            db.session.delete(res)
            db.session.commit()

            return {'message': "User sucessfully deleted"}, 200
        except Exception as e:
            return {'Error':f'{str(e)}'},500
        
user_details_bp.add_url_rule('/user', view_func=UserOperation.as_view('userOperation'))

class Login(MethodView):
    def post(self):
        try:
            schema = LoginSchema()
            req_data = schema.load(request.json)
            # email = data.get('email')
            # password = data.get('password')

            # if not email or not password:
            #     return jsonify('Email and Password are required', 400)
            
            # email_exist = None
            # if email_exist is None:
            res = User_info.query.filter_by(email=req_data.get('email')).first()
            if res != None:
                email_exist = res.password
            # else:
            #     res = Emp_info.query.filter_by(email=email).first()
            #     if res != None:
            #         email_exist = res.password

            if email_exist is None:
                return jsonify('Email does not exist in the database', 404)

            stored_pass = email_exist.encode('utf-8')
            provided_pass = req_data.get('password').encode('utf-8')
            check_pass = bcrypt.checkpw(provided_pass, stored_pass)
            if not check_pass:
                return jsonify('Incorrect password', 401)
            

            return jsonify("Login successful", 200)

        except Exception as e:
            return jsonify(f'Error: {str(e)}', 500)
        
user_details_bp.add_url_rule('/login', view_func=Login.as_view('Login'))


@user_details_bp.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400