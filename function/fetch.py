from flask import Flask, render_template, request, redirect, url_for,make_response,jsonify
import db

def display_info():
    try:
        query = """SELECT name, email FROM user_info;"""
        db.cur.execute(query)
        res = db.cur.fetchall()
        if not res:
                return [{'error': 'No Information found'}, 404]
        user_data = [{'Name': row[0], 'Email': row[1]} for row in res]
        return [user_data,200]
    
    except Exception as e:
        return [{'error': f'Error: {str(e)}'},500]
    finally:
        db.cur.close()