import datetime
class car:

    def __init__(self,model,make, purchasePrice, soldPrice, purchaseYear, purchaseMonth, purchaseDate, soldYear, soldMonth, soldDate):
        self.model = model
        self.make = make
        self.purchasePrice = purchasePrice
        self.soldPrice = soldPrice
        self.purchaseYear = purchaseYear
        self.purchaseMonth = purchaseMonth
        self.purchaseDate = purchaseDate
        self.soldYear = soldYear
        self.soldMonth = soldMonth
        self.soldDate = soldDate

    def getmodel(self):
        return self.model

    def setmodel(self,model):
        self.model = model


    def getmake(self):
        return self.make

    def setmake(self,make):
        self.make = make


    def getpurchasePrice(self):
        return self.purchasePrice

    def setpurchasePrice(self,purchasePrice):
        self.purchasePrice = purchasePrice


    def getsoldPrice(self):
        return self.soldPrice

    def setsoldPrice(self,soldPrice):
        self.soldPrice = soldPrice


    def getpurchaseYear(self):
        return self.purchaseYear

    def setpurchaseYear(self,purchaseYear):
        self.purchaseYear = purchaseYear

    def getpurchaseMonth(self):
            return self.purchaseMonth

    def setpurchaseMonth(self, purchaseMonth):
            self.purchaseMonth = purchaseMonth


    def getpurchaseDate(self):
        return self.purchaseDate

    def setpurchaseaDate(self,purchaseDate):
        self.purchaseDate = purchaseDate

    def getsoldYear(self):
            return self.soldDate

    def setsoldYear(self, soldYear):
            self.soldYear = soldYear


    def getsoldMonth(self):
        return self.soldMonth

    def setsoldMonth(self, soldMonth):
        self.soldMonth = soldMonth


    def getsoldDate(self):
        return self.soldDate

    def setsoldFate(self,soldDate):
        self.soldDate = soldDate


k1 = car(2016,"Corolla",16000,20000,2017,5,23,2019,7,12)
k2 = car(2019,"BMW",20000,21000,2019,4,16,2019,6,23)
k3 = car(2018,"Mercedes",15000,18000,2019,7,24,2019,8,27)
k4 = car(2013,"Mclaren",150000,160000,2015,9,30,2018,12,4)
k5 = car(2014,"Corbet",7000,10000,2016,7,16,2019,3,30)


f1= k1.getmake(),k1.model,k1.purchasePrice,k1.soldPrice,k1.purchaseYear,k1.purchaseMonth,k1.purchaseDate,k1.soldYear,k1.soldMonth,k1.soldDate
f2= k2.getmake(),k2.model,k2.purchasePrice,k2.soldPrice,k2.purchaseYear,k2.purchaseMonth,k2.purchaseDate,k2.soldYear,k2.soldMonth,k2.soldDate
f3= k3.getmake(),k3.model,k3.purchasePrice,k3.soldPrice,k3.purchaseYear,k3.purchaseMonth,k3.purchaseDate,k3.soldYear,k3.soldMonth,k3.soldDate
f4= k4.getmake(),k4.model,k4.purchasePrice,k4.soldPrice,k4.purchaseYear,k4.purchaseMonth,k4.purchaseDate,k4.soldYear,k4.soldMonth,k4.soldDate
f5= k5.getmake(),k5.model,k5.purchasePrice,k5.soldPrice,k5.purchaseYear,k5.purchaseMonth,k5.purchaseDate,k5.soldYear,k5.soldMonth,k5.soldDate


print(f1)
print(k1.soldYear-k1.purchaseYear)
print(f2)
print(f3)
print(f4)
print(f5)

