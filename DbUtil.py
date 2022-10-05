import mysql.connector as connector

class DbRunner:

    def __init__(self):
        self.con = connector.connect(host='localhost', user='root', password='', port='3306', database='cestar_python')
        print(self.con)
        query = "CREATE TABLE IF NOT EXISTS STUDENT(ID INT PRIMARY KEY,NAME VARCHAR(20),CITY VARCHAR(20),CONTACT VARCHAR(20),EMAIL VARCHAR(20))"
        cursor = self.con.cursor()
        cursor.execute(query)
        print("Table Created Successfully!!!")

    def insertRec(self, id, name, city, contact, email):
        query = "INSERT INTO STUDENT (ID,NAME,CITY,CONTACT,EMAIL) VALUES({},'{}','{}','{}','{}')".format(id, name, city, contact, email)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Insert Successfully!!!")

    def delRec(self, id):
        query = "Delete From Student where id = {}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Deleted Successfully!!!")

    def updateRec(self, u_id, u_name, u_city, u_contact, u_email, old_id):
        query = "Update Student set id={}, name='{}', city='{}', contact='{}', email='{}' where id={}".format(u_id, u_name, u_city, u_contact, u_email, old_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Updated Successfully!!!")

dbtest = DbRunner()

# dbtest.insertRec(124, 'Jackson', 'Milton', '647-111-2222', 'Jackson@gmail.com')

# dbtest.delRec(124)

dbtest.updateRec(456, 'Jackson Updated', 'Milton Updated', '612-999-8888', 'JacksonUpdate@gmail.com', 124)















