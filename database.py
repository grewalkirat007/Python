import mysql.connector as connector


class DbRunner:

    def __init__(self):
        self.con = connector.connect(
            host='localhost', user='root', password='', port='3306', database='db_C0757809')
        print(self.con)
        print("Connected to database Successfully!!!")

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

    def updateRec(self, u_id, u_name, u_age, u_gender, u_contact, u_course, old_id):
        query = "Update Students set id = {}, name = '{}', age = '{}', gender = '{}', course = '{}', contact = '{}' where id = {}".format(
            u_id, u_name, u_age, u_gender, u_course, u_contact, old_id)
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
                f"ID: {rows[0]} Name: {rows[1]} Age: {rows[2]} Gender: {rows[3]} Course: {rows[4]} Contact: {rows[5]}")

db = DbRunner()
# db.insertRec(6, 'Ramandeep', 18, 'F', 'CSD1111', '753-753-7539')
# db.displayAll()
# db.updateRec(7, 'Ramandeep', 19, 'F', 'CSD1458', '753-753-7539', 6)
db.delRec(7)
