from flask import Flask, request
import bcrypt
import db

def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return [{'error': 'Email and Password are required'}, 400]

        query_check_email = "SELECT pass FROM user_info WHERE email = %s"
        db.cur.execute(query_check_email, (email,))
        email_exist = db.cur.fetchone()

        if email_exist is None:
            return [{'error': 'Email does not exist in the database'}, 404]

        stored_pass = email_exist[0].encode('utf-8')
        provided_pass = password.encode('utf-8')
        check_pass = bcrypt.checkpw(provided_pass, stored_pass)
        if not check_pass:
            return [{'error': 'Incorrect password'}, 401]
        

        return [{'message': "Login successful"}, 200]

    except Exception as e:
        return [{'error': f'Error: {str(e)}'}, 500]

    finally:
        db.cur.close()
        db.connection.commit()