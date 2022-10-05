import mysql.connector as connector

class DbRunner:

    def __init__(self):
        self.con = connector.connect(
            host='localhost', user='root', password='', port='3306', database='db_C0759921')
        print(self.con)

    def insertRec(self, id, name, age, gender, course, contact):
        query = "INSERT INTO STUDENTS (ID,NAME,AGE,GENDER,COURSE,CONTACT) VALUES({},'{}','{}','{}','{}','{}')".format(
            id, name, age, gender, course, contact)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Inserted Successfully!!!")

    def delRec(self, id):
        query = "Delete From Students Where id = {}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record deleted Successfully !!")

    def updateRec(self, u_id, u_name, u_city, u_contact, u_email, old_id):
        query = "Update Students set id = {},name = '{}', city = '{}',contact = '{}', email = '{}' where id = {}".format(
            u_id, u_name, u_city, u_contact, u_email, old_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Updated Successfully!!")

    def displayAll(self):
        query = "SELECT * FROM STUDENTS"
        cursor = self.con.cursor()
        cursor.execute(query)
        for rows in cursor:
            print(
                f"Student ID: {rows[0]} Name : {rows[1]} city : {rows[2]} contact : {rows[3]} email : {rows[4]}")


dbtest = DbRunner()
