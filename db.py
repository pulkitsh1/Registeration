import mysql.connector
import os

mysql_config = {
    'host': os.getenv('HOST_NAME'),
    'user': os.getenv('USER'),
    'password': os.getenv('DATABASE_KEY'),
    'database': os.getenv('DATABASE_NAME'),
    'auth_plugin': os.getenv('DATABASE_KEY'),
}

connection = mysql.connector.connect(**mysql_config)
cur=connection.cursor()