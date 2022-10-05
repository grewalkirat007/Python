import matplotlib as plt
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

x = []
y = []

for a in CollectionName5.find({}, {"_id": 0, "PlayerID": 1}):
    x.append(a)

for a in CollectionName5.find({}, {"_id": 0, "Warnings": 1}):
    y.append(a)

plt.ylabel("Warnings")
plt.xlabel("PlayerID")
plt.title("Data")
plt.grid(color='blue', linestyle='--', linewidth=1)
plt.scatter(x, y, color = 'r')
plt.plot(x, y, color = 'r')
plt.show()