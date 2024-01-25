from flask import Flask, request
import bcrypt
import db

salt = bcrypt.gensalt()

def registeration():
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

        query = """INSERT INTO user_info
                                (name, email, pass)
                                VALUES (%s, %s, %s);"""
        db.cur.execute(query, (name, email, hashed))
        db.connection.commit()
        db.cur.close()
        return [{"message":"User successfully registered."}, 200]
    except Exception as e:
        return [{"error":f"An error occurred: {str(e)}"}, 500]
