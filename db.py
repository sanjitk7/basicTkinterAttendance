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
mycursor.execute("create table if NOT exists attendance_record(a_date date not null, a_detail varchar(10) not null,u_id int, constraint fk_attendance foreign key (u_id) references t_users(u_id));" )

mycursor.execute("USE attendance")