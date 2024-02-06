from flask import Flask,jsonify
from blueprints.user_details.user_details import user_details_bp
# from blueprints.employee_details.emp_details import emp_details_bp
from flask_sqlalchemy import SQLAlchemy
from db import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING')


db.init_app(app)
app.register_blueprint(user_details_bp)
# app.register_blueprint(emp_details_bp)

if __name__ == '__main__':
    app.run(debug=True)
