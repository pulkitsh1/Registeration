from flask import Flask, render_template, request, redirect, url_for,make_response,jsonify
import mysql.connector
import bcrypt
import os
import db

def delete():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']

        if email == None:
            return [{'error': 'Email is required'}, 400]
        elif password == None:
            return [{'error': 'Password is required'}, 400]

        query_check_email = "SELECT pass FROM user_info WHERE email = %s"
        db.cur.execute(query_check_email, (email,))
        email_exist = db.cur.fetchone()

        if email_exist is None:
            return jsonify({'error': 'Email does not exist in the database'}), 404
        
        stored_pass = email_exist[0].encode('utf-8')
        provided_pass = password.encode('utf-8')
        check_pass = bcrypt.checkpw(provided_pass, stored_pass)
        
        if not check_pass:
            return [{'error': 'Incorrect password'}, 401]
        
        query = "DELETE FROM user_info WHERE email = %s;"
        db.cur.execute(query, ( email,))
        return [{'message': "User sucessfully deleted"}, 200]
    except Exception as e:
        return [{'error': f'Error: {str(e)}'},500]
    finally:
        db.connection.commit()
        db.cur.close()