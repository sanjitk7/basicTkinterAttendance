import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Luckyusa1",
  database="attendance"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS attendance")
mycursor.execute("create table if NOT exists users(u_id int auto_increment primary key,password varchar(60),date_joined varchar(30),name varchar(40) not null);")
mycursor.execute("USE attendance")