import mysql.connector

conn = mysql.connector.connect(
    host="localhost",       # or your remote host
    user="root",            # or your MySQL username
    password="testing@123",# your MySQL password
    database="learningdb" 
)

if conn.is_connected():
    print("Connection established successfully!")
else:
    print("Connection failed.")

