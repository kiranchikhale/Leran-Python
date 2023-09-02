import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user="kiran",passwd = "1234",database="myDB")
mycursor = mydb.cursor()
#mycursor.execute("show databases")
mycursor.execute("select * from student")
for i in mycursor:
    print(i)