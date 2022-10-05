from database import DbRunner


class AppMenu:
    def main(self):
        student_dao = DbRunner()
        while(True):
            print("Enter 1 to insert Record")
            print("Enter 2 to Display Record")
            print("Enter 3 to Update Record")
            print("Enter 4 to Delete Record")
            print("Enter 5 to Exit the Application ")

            Choice = int(input())
            if(Choice == 1):
                i_id = input("ID: ")
                i_name = input("Name: ")
                i_age = input("Age: ")
                i_gender = input("Gender: ")
                i_course = input("Course: ")
                i_contact = input("Contact: ")
                student_dao.insertRec(
                    i_id, i_name, i_age, i_gender, i_course, i_contact)
            elif(Choice == 2):
                student_dao.displayAll()
            elif(Choice == 3):
                o_id = input("Old ID: ")
                u_id = input("New ID: ")
                u_name = input("Name: ")
                u_age = input("Age: ")
                u_gender = input("Gender: ")
                u_course = input("Course: ")
                u_contact = input("Contact: ")
                student_dao.updateRec(u_id, u_name, u_age, u_gender, u_course, u_contact, o_id)
            elif(Choice == 4):
                d_id = input("Enter id:")
                student_dao.delRec(d_id)
            elif(Choice == 5):
                break
            else:
                print("Invalid Entry Please Try Again")


app = AppMenu()
app.main()
