from flask import Flask, request
import db

def updateName():
    user = request.get_json()
    if 'name' not in user:
        return [{'error': 'User name is required'},400]
    if 'email' not in user:
        return [{'error': 'Email is required'},400]
    try:
        query_check_email ="SELECT COUNT(*) FROM user_info WHERE email = %s"
        db.cur.execute(query_check_email,(user['email'],))
        email_exist = db.cur.fetchone()[0]

        if email_exist == 0:
            return [{'error':'Email does not exist in the database'}, 404]
        
        query = """UPDATE user_info
                            SET name = %s
                            WHERE email = %s;"""
        db.cur.execute(query, (user['name'], user['email']))
        db.connection.commit()

        return [{'message': "Success"}, 200]
    except Exception as e:
        return [{'error': f'Error: {str(e)}'},500]
    finally:
        db.cur.close()