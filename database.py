import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssw0rd'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute('CREATE DATABASE BEPCO_CRM')

print('All Done!')