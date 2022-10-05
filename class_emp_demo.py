# class Employee:

#     def __init__(self):
#         self.id = 786
#         self.name = "Roger"
#         self.address = "Torornto"
#         self.contact = "4563214555"
#         self.designation = "manager"
#         self.department = "Billing"
#         print(f"Employee id :{self.id} \n Name :{self.name} \n Address :{self.address} \n Contact :{self.contact} \n Designation :{self.designation} \n Department :{self.department} ")

# emp1 = Employee();

class Employee:

     def __init__(self, id, name, address, contact,designation, department ):
        self.id = id
        self.name = name
        self.address = address
        self.contact = contact
        self.designation = designation
    
        self.department = department
     def empInfo(self):
        print(f"Employee id :{self.id} \n Name :{self.name} \n Address :{self.address} \n Contact :{self.contact} \n Designation :{self.designation} \n Department :{self.department} ")
 
     def worksIn(self, shift):
         print(f"{self.name} works in {shift} Shift") 

     def maintainRecords(self):
       #  print(f"{self.name} maintain Records of HR Department")
         print(f"{self.name} maintain Records of {self.department} Department")

     def createreports(self):
         print(f"{self.name} creates Reports for {self.department} Department")  

emp1 = Employee(123,"Jackson","Brampton","4372256647","Manager","Billing");
emp1.empInfo()
emp1.worksIn("afternoon")
emp1.maintainRecords()
emp1.createreports()


emp2 = Employee(567,"Edward", "Windsor", "64125663", "General labour","Sales");
emp2.empInfo()
emp2.worksIn("afternoon")
emp2.maintainRecords()
emp2.createreports()
