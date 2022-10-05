# from matplotlib import ylabel, xlabel, title, grid, scatter, plot, show
import matplotlib.pyplot as plt
import pymongo


DB_URL = "mongodb://localhost:27017/"
DB_Name = "DB_Gaming_Project"

CollectionName1 = "Games"
# CollectionName2 = "Leadership"
# CollectionName3 = "News"
# CollectionName4 = "Players"
# CollectionName5 = "Status"
# CollectionName6 = "Updates"

dbServer = pymongo.MongoClient(DB_URL)
if dbServer:
    db = dbServer[DB_Name]

x = [1,2,3,7,10,13]
y = [1,2,3,4,5,9]
# x = []
# y = []

a = 0

# for a in CollectionName1.find({}, { "Downloads": 1}):
    # x.append(a)

a = 0

# for a in CollectionName1.find({}, { "ActivePlayers": 1}):
    # y.append(a)

plt.ylabel("ActivePlayers")
plt.xlabel("Downloads")
plt.title("Data")
plt.grid(color='red', linestyle='--', linewidth=1)
plt.scatter(x, y, color = 'r')
plt.plot(x, y, color = 'r')
plt.show()
