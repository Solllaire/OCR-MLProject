import _mysql_connector
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="some password"
)
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS TestDB')
mycursor.execute("SHOW DATABASES")
mycursor.execute("CREATE TABLE IF NOT EXISTS something(name VARCHAR(255), age INTEGER(10)")

for db in mycursor:
    print(db)
def table_creator(tablename):
    sqlFormula = "INSERT INTO "+tablename+" (column1, column2) VALUES (%s, %s)"