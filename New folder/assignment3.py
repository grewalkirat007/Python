import mysql.connector as connector


class MysqlAssignment:

    def __init__(self):
        self.con = connector.connect(
            host='localhost', user='root', password='', port='3306', database='assignment3')
        print(self.con)
        print("Connected to database Successfully!!!")

    # INSERT
    def insertProject(self, project_id, project_name, student_id, teacher_id, description):
        query = "INSERT INTO project (project_id,project_name,student_id,teacher_id,description) VALUES({},'{}','{}','{}','{}')".format(
            project_id, project_name, student_id, teacher_id, description)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Inserted Successfully!!!")

    def insertStudent(self, student_id, name, age, email, course, grade):
        query = "INSERT INTO student (student_id,name,age,email,course,grade) VALUES({},'{}','{}','{}','{}','{}')".format(
            student_id, name, age, email, course, grade)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Inserted Successfully!!!")

    def insertTeacher(self, teacher_id, name, age, email, course, contact):
        query = "INSERT INTO teacher (teacher_id,name,age,email,course,contact) VALUES({},'{}','{}','{}','{}','{}')".format(
            teacher_id, name, age, email, course, contact)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Inserted Successfully!!!")

    # DELETE
    def delProject(self, id):
        query = "Delete From project Where project_id = {}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record deleted Successfully!!!")

    def delStudent(self, id):
        query = "Delete From student Where student_id = {}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record deleted Successfully !!")

    def delTeacher(self, id):
        query = "Delete From teacher Where teacher_id = {}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record deleted Successfully !!")

    # UPDATE
    def updateProject(self, u_project_id, u_project_name, u_student_id, u_teacher_id, u_description, old_id):
        query = "Update Project set project_id = {}, project_name = '{}', student_id = '{}', teacher_id = '{}', description = '{}' where project_id = {}".format(
            u_project_id, u_project_name, u_student_id, u_teacher_id, u_description, old_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Updated Successfully!!")

    def updateStudent(self, u_student_id, u_name, u_age, u_email, u_course, u_grade, old_id):
        query = "Update Student set student_id = {}, name = '{}', age = '{}', email = '{}', course = '{}', grade = '{}' where student_id = {}".format(
            u_student_id, u_name, u_age, u_email, u_course, u_grade, old_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Updated Successfully!!")
    
    def updateTeacher(self, u_teacher_id, u_name, u_age, u_email, u_course, u_contact, old_id):
        query = "Update Teacher set teacher_id = {}, name = '{}', age = '{}', email = '{}', course = '{}', contact = '{}' where teacher_id = {}".format(
            u_teacher_id, u_name, u_age, u_email, u_course, u_contact, old_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("Record Updated Successfully!!")

    # DISPLAY
    def displayAllProject(self):
        query = "SELECT * FROM Project"
        cursor = self.con.cursor()
        cursor.execute(query)
        for rows in cursor:
            print(
                f"project_id: {rows[0]} project_name: {rows[1]} student_id: {rows[2]} teacher_id: {rows[3]} description: {rows[4]}")

    def displayAllStudent(self):
        query = "SELECT * FROM Student"
        cursor = self.con.cursor()
        cursor.execute(query)
        for rows in cursor:
            print(
                f"student_id: {rows[0]} name: {rows[1]} age: {rows[2]} email: {rows[3]} course: {rows[4]} grade: {rows[5]}")

    def displayAllTeacher(self):
        query = "SELECT * FROM Teacher"
        cursor = self.con.cursor()
        cursor.execute(query)
        for rows in cursor:
            print(
                f"teacher_id: {rows[0]} name: {rows[1]} age: {rows[2]} email: {rows[3]} course: {rows[4]} contact: {rows[5]}")


data = MysqlAssignment()

# INSERT
# data.insertProject(1, "Project1", 1, 1, "Main Project 1")
# data.insertProject(2, "Project2", 2, 1, "Main Project 2")
# data.insertProject(3, "Project3", 1, 2, "Main Project 3")
# data.insertProject(4, "Project4", 2, 2, "Sub Project 1")
# data.insertProject(5, "Project5", 2, 1, "Sub Project 2")
# data.insertProject(6, "Project6", 1, 2, "Sub Project 3")

# data.insertStudent(1, "Student1", 18, "stud1@mail.com", "CSD1111", "123-123-1234")
# data.insertStudent(2, "Student2", 25, "stud2@mail.com", "CSD1112", "456-456-4567")
# data.insertStudent(3, "Student3", 22, "stud3@mail.com", "CSD1111", "789-789-7890")

# data.insertTeacher(1, "Teacher1", 35, "teacher1@mail.com", "CSD1111", "753-753-7530")
# data.insertTeacher(2, "Teacher2", 29, "teacher2@mail.com", "CSD1112", "951-951-9510")








# UPDATE
# data.updateProject(9, "Project1", 2, 1, "Sub Project 4", 1)
# data.updateStudent(5, "Student6", 19, "stud6@mail.com", "CSD1112", "123-123-1234", 1)
# data.updateTeacher(3, "Teacher3", 29, "teacher3@mail.com", "CSD1112", "951-951-9510", 2)




# DELETE
# data.delProject(9)
# data.delStudent(5)
# data.delTeacher(3)






# DISPLAY
# data.displayAllProject()
# data.displayAllStudent()
# data.displayAllTeacher()

