import pymongo

DB_URL = "mongodb://localhost:27017/"
DB_Name = "DB_Gaming_Project"

CollectionName1 = "Games"
CollectionName2 = "Leadership"
CollectionName3 = "News"
CollectionName4 = "Players"
CollectionName5 = "Status"
CollectionName6 = "Updates"


dbServer = pymongo.MongoClient(DB_URL)
if dbServer:
    db = dbServer[DB_Name]


# Read  By Prabhjot Singh
def GetDataFromCollection(colName):
    col = db[colName]
    if(col):
        for x in col.find():
            print(x)



# GetDataFromCollection("Game")
# GetDataFromCollection("Leadership")
# GetDataFromCollection("News")
# GetDataFromCollection("Players")
# GetDataFromCollection("Status")
# GetDataFromCollection("Update")


# Insert/Create  By Lovepreet Singh
def InsertDocumentIntoCollection(colName, objectParam):
    col = db[colName]
    col.insert_one(objectParam)
    GetDataFromCollection(colName)

# Games

Games = {
    "GameID": 1,
    "GameName": "Clash of Clanes",
    "Type": "sports",
    "BuildYear": 2010,
    "Downloads": 5,
    "ActivePlayers": 4,
    "Size": 5,
    "Creater": "cryston",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 2,
    "GameName": "Call of duty",
    "Type": "action",
    "BuildYear": 2017,
    "Downloads": 4,
    "ActivePlayers": 6,
    "Size": 4,
    "Creater": "ritik",
    "Version": "4.1",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 3,
    "GameName": "poker",
    "Type": "puzzle",
    "BuildYear": 2000,
    "Downloads": 1,
    "ActivePlayers": 3,
    "Size": 3,
    "Creater": "peter",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 4,
    "GameName": "doom",
    "Type": "war",
    "BuildYear": 2016,
    "Downloads": 2,
    "ActivePlayers": 5,
    "Size": 6,
    "Creater": "charley",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 5,
    "GameName": "tic-tac-toe",
    "Type": "puzzle",
    "BuildYear": 2012,
    "Downloads": 7,
    "ActivePlayers": 2,
    "Size": 1,
    "Creater": "sachin",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 6,
    "GameName": "chess",
    "Type": "strategy",
    "BuildYear": 1999,
    "Downloads": 3,
    "ActivePlayers": 2,
    "Size": 2,
    "Creater": "sid",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 7,
    "GameName": "basket ball",
    "Type": "sports",
    "BuildYear": 1990,
    "Downloads": 7,
    "ActivePlayers": 4,
    "Size": 7,
    "Creater": "hideo",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 8,
    "GameName": "PUBG",
    "Type": "action",
    "BuildYear": 2011,
    "Downloads": 3,
    "ActivePlayers": 12,
    "Size": 9,
    "Creater": "gabe",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 9,
    "GameName": "cricket",
    "Type": "sports",
    "BuildYear": 1991,
    "Downloads": 2,
    "ActivePlayers": 11,
    "Size": 11,
    "Creater": "william",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)

Games = {
    "GameID": 10,
    "GameName": "tennis",
    "Type": "sports",
    "BuildYear": 1994,
    "Downloads": 8,
    "ActivePlayers": 4,
    "Size": 12,
    "Creater": "harry",
    "Version": "4.2",
    "DevicesAvailable": ["Android", "iOS", "PC", "PlayStation", "Xbox"]
}
# InsertDocumentIntoCollection("Game", Games)


# Leadership

Leadership = {
    "PlayerID": 1,
    "Rank": 1,
    "Score": 100,
    "GameID": 1,
    "Achievements": ["3rd", "winner"],
    "SessionNumber": 2
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 2,
    "Rank": 2,
    "Score": 90,
    "GameID": 2,
    "Achievements": ["winner", "1st runnerup "],
    "SessionNumber": 1
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 3,
    "Rank": 3,
    "Score": 80,
    "GameID": 3,
    "Achievements": ["2nd", "1st"],
    "SessionNumber": 3
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 4,
    "Rank": 4,
    "Score": 70,
    "GameID": 4,
    "Achievements": ["1st", "2nd"],
    "SessionNumber": 5
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 5,
    "Rank": 5,
    "Score": 60,
    "GameID": 5,
    "Achievements": ["1st runner up", "2nd runner up"],
    "SessionNumber": 6
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 6,
    "Rank": 6,
    "Score": 50,
    "GameID": 6,
    "Achievements": ["3rd", "2nd"],
    "SessionNumber": 10
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 7,
    "Rank": 7,
    "Score": 40,
    "GameID": 7,
    "Achievements": ["2nd", "1st"],
    "SessionNumber": 9
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 8,
    "Rank": 8,
    "Score": 30,
    "GameID": 8,
    "Achievements": ["2nd runner up", "1st runner up"],
    "SessionNumber": 8
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 9,
    "Rank": 9,
    "Score": 20,
    "GameID": 9,
    "Achievements": ["1st", "2nd"],
    "SessionNumber": 7
}
# InsertDocumentIntoCollection("Leadership", Leadership)

Leadership = {
    "PlayerID": 10,
    "Rank": 10,
    "Score": 10,
    "GameID": 10,
    "Achievements": ["winner", "1st runner up"],
    "SessionNumber": 1
}
# InsertDocumentIntoCollection("Leadership", Leadership)


# News

News = {
    "NewsID": 1,
    "Title": "War",
    "Description": "",
    "Likes": 3,
    "Comments": 11,
    "Category": ["One", "Two"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 4,
    "Title": " lost",
    "Description": "",
    "Likes": 0,
    "Comments": 10,
    "Category": ["three", "five"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 2,
    "Title": "winner",
    "Description": "",
    "Likes": 9,
    "Comments": 4,
    "Category": ["eight", "seven"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 3,
    "Title": "sports",
    "Description": "",
    "Likes": 1,
    "Comments": 5,
    "Category": ["five", "six"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 8,
    "Title": "fame",
    "Description": "",
    "Likes": 2,
    "Comments": 1,
    "Category": ["two", "one"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 7,
    "Title": "stocks",
    "Description": "",
    "Likes": 4,
    "Comments": 7,
    "Category": ["One", "Two"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 6,
    "Title": "currency",
    "Description": "",
    "Likes": 5,
    "Comments": 9,
    "Category": ["eight", "Three"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 5,
    "Title": "hollywood",
    "Description": "",
    "Likes": 6,
    "Comments": 3,
    "Category": ["nine", "Ten"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 9,
    "Title": "bollywood",
    "Description": "",
    "Likes": 8,
    "Comments": 6,
    "Category": ["seven", "five"]
}
# InsertDocumentIntoCollection("News", News)

News = {
    "NewsID": 10,
    "Title": "pollywood",
    "Description": "",
    "Likes": 10,
    "Comments": 2,
    "Category": ["One", "Two"]
}
# InsertDocumentIntoCollection("News", News)


# Players

Players = {
    "PlayerID": 1,
    "PlayerName": "rahul",
    "Age": 18,
    "Email": "",
    "Username": "ral",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 8,
    "PlayerName": "chris",
    "Age": 19,
    "Email": "",
    "Username": "chris",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 6,
    "PlayerName": "angela",
    "Age": 22,
    "Email": "",
    "Username": "angel",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 7,
    "PlayerName": "herry",
    "Age": 28,
    "Email": "",
    "Username": "hrr",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 9,
    "PlayerName": "berry",
    "Age": 19,
    "Email": "",
    "Username": "berry",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 2,
    "PlayerName": "rohit",
    "Age": 23,
    "Email": "",
    "Username": "roh",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 3,
    "PlayerName": "dhoni",
    "Age": 24,
    "Email": "",
    "Username": "mahinder",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 11,
    "PlayerName": "steve",
    "Age": 29,
    "Email": "",
    "Username": "goyal",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 12,
    "PlayerName": "johnson",
    "Age": 26,
    "Email": "",
    "Username": "john",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

Players = {
    "PlayerID": 5,
    "PlayerName": "smith",
    "Age": 26,
    "Email": "",
    "Username": "steven",
    "SignupDate": "",
    "LastLogin": ""
}
# InsertDocumentIntoCollection("Players", Players)

# Status

Status = {
    "PlayerID": 1,
    "Active": True,
    "GamesPlayed": ["basket ball", "PUBG"],
    "HourPlayed": 1.0,
    "Warnings": 1,
    "Banned": True
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 6,
    "Active": True,
    "GamesPlayed": ["chess", "PUBG"],
    "HourPlayed": 2.0,
    "Warnings": 10,
    "Banned": False
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 7,
    "Active": False,
    "GamesPlayed": ["tic-tac-toe", "cricket"],
    "HourPlayed": 1.0,
    "Warnings": 9,
    "Banned": True
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 9,
    "Active": True,
    "GamesPlayed": ["doom", "poker"],
    "HourPlayed": 5.0,
    "Warnings": 7,
    "Banned": True
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 10,
    "Active": False,
    "GamesPlayed": ["tennis", "basket ball"],
    "HourPlayed": 4.0,
    "Warnings": 6,
    "Banned": False
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 8,
    "Active": True,
    "GamesPlayed": ["doom", "cricket"],
    "HourPlayed": 8.0,
    "Warnings": 8,
    "Banned": True
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 5,
    "Active": True,
    "GamesPlayed": ["Clash of Clanes", "doom"],
    "HourPlayed": 1.0,
    "Warnings": 3,
    "Banned": False
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 4,
    "Active": False,
    "GamesPlayed": ["basket ball", "cricket"],
    "HourPlayed": 9.0,
    "Warnings": 2,
    "Banned": True
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 3,
    "Active": True,
    "GamesPlayed": ["Call of duty", "doom"],
    "HourPlayed": 1.0,
    "Warnings": 8,
    "Banned": True
}
# InsertDocumentIntoCollection("Status", Status)

Status = {
    "PlayerID": 2,
    "Active": True,
    "GamesPlayed": ["Clash of Clanes", "Call of duty"],
    "HourPlayed": 6.0,
    "Warnings": 1,
    "Banned": True
}
# InsertDocumentIntoCollection("Status", Status)


# Updates

Updates = {
    "GameID": 1,
    "UpdateAvailable": True,
    "LastUpdate": "Date/Version",
    "UpdateSize": 1.7,
    "UpdatedBy": "tesla",
    "UpdatePending": False
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 10,
    "UpdateAvailable": False,
    "LastUpdate": "Date/Version",
    "UpdateSize": 4.2,
    "UpdatedBy": "supercell",
    "UpdatePending": True
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 7,
    "UpdateAvailable": True,
    "LastUpdate": "Date/Version",
    "UpdateSize": 1.6,
    "UpdatedBy": "tencent",
    "UpdatePending": True
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 9,
    "UpdateAvailable": True,
    "LastUpdate": "Date/Version",
    "UpdateSize": 1.1,
    "UpdatedBy": "Square Enix.",
    "UpdatePending": True
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 5,
    "UpdateAvailable": False,
    "LastUpdate": "Date/Version",
    "UpdateSize": 1.6,
    "UpdatedBy": "Gameloft.",
    "UpdatePending": True
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 3,
    "UpdateAvailable": True,
    "LastUpdate": "Date/Version",
    "UpdateSize": 1.1,
    "UpdatedBy": "Activision Blizzard",
    "UpdatePending": True
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 8,
    "UpdateAvailable": True,
    "LastUpdate": "Date/Version",
    "UpdateSize": 1.2,
    "UpdatedBy": "Nintendo.",
    "UpdatePending": False
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 4,
    "UpdateAvailable": False,
    "LastUpdate": "Date/Version",
    "UpdateSize": 4.1,
    "UpdatedBy": "Ubisoft.",
    "UpdatePending": True
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 3,
    "UpdateAvailable": True,
    "LastUpdate": "Date/Version",
    "UpdateSize": 3.1,
    "UpdatedBy": "Sony",
    "UpdatePending": False
}
# InsertDocumentIntoCollection("Updates", Updates)

Updates = {
    "GameID": 2,
    "UpdateAvailable": True,
    "LastUpdate": "Date/Version",
    "UpdateSize": 5.1,
    "UpdatedBy": "Bungie",
    "UpdatePending": True
}
# InsertDocumentIntoCollection("Updates", Updates)




# Update By Prabhjot Singh
def UpdateOneDocumentFromCollection(colName, query, objectParam):
    col = db[colName]
    col.update_one(query, objectParam)
    GetDataFromCollection(colName)


# myquery = {"GameID": 2}
# newvalues = {"$set": {"Downloads": 10}}
# UpdateOneDocumentFromCollection("Game", myquery, newvalues)

# myquery = {"PlayerID": 8}
# newvalues = {"$set": {"Age": 20}}
# UpdateOneDocumentFromCollection("Players", myquery, newvalues)

# myquery = {"PlayerID": 6}
# newvalues = {"$set": {"Active": False}}
# UpdateOneDocumentFromCollection("Status", myquery, newvalues)




# Delete By Kiratveer Singh Grewal
def DeleteOneDocumentFromCollection(colName, query):
    col = db[colName]
    col.delete_one(query)
    GetDataFromCollection(colName)


# myquery = {"GameID": 3}
# DeleteOneDocumentFromCollection("Game", myquery)
# 
# myquery = {"NewsID": 1}
# DeleteOneDocumentFromCollection("News", myquery)
# 
# myquery = {"PlayerID": 3}
# DeleteOneDocumentFromCollection("Status", myquery)