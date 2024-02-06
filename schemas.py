from flask_marshmallow import Marshmallow
from db import User_info
from marshmallow.fields import String
from marshmallow import validate, validates_schema, ValidationError
from flask import request

ma = Marshmallow()

class DetailsSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True,validate=[validate.Length(min=3)])
    email = String(required=True,validate=[validate.Email()])
    class Meta:
        model = User_info
        exclude = ['password']


class SignupSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True,validate=[validate.Length(min=3)])
    email = String(required=True,validate=[validate.Email()])
    confirm_password = String(required=True)

    @validates_schema
    def validate_data(self, data, **kwargs):
        email = data.get('email')

        if User_info.query.filter_by(email=email).count():
            raise ValidationError(f"Email {email} already exists.")

    class Meta:
        model = User_info

class LoginSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True,validate=[validate.Length(min=3)])
    email = String(required=True,validate=[validate.Email()])

    class Meta:
        model = User_info
    

