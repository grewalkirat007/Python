import pymongo

DB_URL = "mongodb://localhost:27017/"
DB_Name = "test"
Col_Name = "Employee"

dbServer = pymongo.MongoClient(DB_URL)
if dbServer:
    db = dbServer[DB_Name]



def InsertDocumentIntoCollection(colName, objectParam):
    col = db[colName]
    col.insert_one(objectParam)

employee1 = {"Id":0, "Name":"Kirat", "JoinDate":"10-10-2000", "Department":"Sales", "YearlySalary":10000, "Position":"Manager", "Status":True}
employee2 = {"Id":1, "Name":"Kiratveer", "JoinDate":"11-11-2001", "Department":"Picking", "YearlySalary":20000, "Position":"Associate", "Status":True}
employee3 = {"Id":2, "Name":"KiratGrewal", "JoinDate":"10-12-2002", "Department":"Packing", "YearlySalary":15000, "Position":"HR", "Status":False}
# InsertDocumentIntoCollection("Employee", employee1)
# InsertDocumentIntoCollection("Employee", employee2)
# InsertDocumentIntoCollection("Employee", employee3)


def GetDataFromCollection(colName):
    col = db[colName]
    if(col):
        for x in col.find({"Status": True}):
            print(x)

GetDataFromCollection("Employee")

def DeleteDocumentFromCollection(colName):
    col = db[colName]
    col.delete_many({"Status":False})

DeleteDocumentFromCollection("Employees")