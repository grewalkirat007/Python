import mysql.connector as connector

class DbRunner:

    def __init__(self):
        self.con = connector.connect(host = 'localhost', user = 'root', password = '', port = '3306', database = 'cestar_python')
        print(self.con)
        query = "CREATE TABLE IF NOT EXISTS STUDENT(ID INT PRIMARY KEY,NAME VARCHAR(20),CITY VARCHAR(20),CONTACT VARCHAR(20),EMAIL VARCHAR(20))"
        cursor = self.con.cursor()
        cursor.execute(query)
        print("Table Created Successfully!!!")

    def insertRec(self,id,name,city,contact,email):
        query = "INSERT INTO STUDENT (ID,NAME,CITY,CONTACT,EMAIL) VALUES({},'{}','{}','{}','{}')".format(id,name,city,contact,email)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Inserted Successfully!!!")

    def delRec(self,id):
        query = "Delete From Student Where id = {}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record deleted Successfully !!")

    def updateRec(self,u_id,u_name,u_city,u_contact,u_email,old_id):
        query = "Update Student set id = {},name = '{}', city = '{}',contact = '{}', email = '{}' where id = {}".format(u_id, u_name, u_city, u_contact, u_email, old_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Updated Successfully!!")

    def displayAll(self):
        query = "SELECT * FROM STUDENT"
        cursor = self.con.cursor()
        cursor.execute(query)
        for rows in cursor:
            print(f"Student ID: {rows[0]} Name : {rows[1]} city : {rows[2]} contact : {rows[3]} email : {rows[4]}")
      

dbtest = DbRunner()

#dbtest.insertRec(999,'Jackson','Milton','647-114-335','Jackson@gmail.com')

# dbtest.delRec(124)

# dbtest.updateRec(125,'Harpreet','Brampton','568-666-8856','Harpreet@gmail.com',123)

# dbtest.displayAll()
#dbtest.insertRec(555,'Jagtar','B-Town','978-998-3364','Jaggudon@gmail.com')
