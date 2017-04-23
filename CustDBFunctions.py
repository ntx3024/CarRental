import BaseDBFunctions as db

#Class for handling the Customer Inventory
class CustDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadCustHist(self):
        records = super().loadRecords('SELECT C.FirstName, C.LastName, R.ReservationID, M.Model, R.StartDate, R.EndDate, R.RealStartDate, R.RealEndDate FROM RESERVATIONS AS R, CUSTOMERS AS C, CARS as M WHERE  R.CustomerID = C.CustomerID AND R.CarID = M.CarID ORDER BY R.RealStartDate')
        return records

    def loadCustomers(self):
        records = super().loadRecords('SELECT * FROM Customers')
        return records

    def loadCustomersByFName(self, FirstName):
        records = super().loadRecords("SELECT * FROM Customers WHERE FirstName LIKE '{}%'".format(FirstName))
        return records

    def loadCustomersByLName(self, LastName):
        records = super().loadRecords("SELECT * FROM Customers WHERE LastName LIKE '{}%'".format(LastName))
        return records

    def loadCustomerByID(self, custID):
        records = super().loadRecords("SELECT * FROM Customers WHERE CustomerID = '{}'".format(custID))
        return records

    def loadCustomersByName(self, FistName, LastName):
        records = super().loadRecords("SELECT * FROM Customers WHERE FirstName LIKE '{}%' AND LastName LIKE '{}%'".format(FistName, LastName))
        return records

    def AddNewCustomer(self, FirstName, LastName, Phone):
        super().AddNewRecord("INSERT INTO Customers(FirstName, LastName, PhoneNumber) VALUES('{}', '{}', '{}')".format(FirstName, LastName, Phone))

    def DeleteCustomer(self, CustomerID):
        super().loadRecords("DELETE FROM Customers WHERE CustomerID = '{}'".format(CustomerID))

    def UpdateCustomer(self, FirstName, LastName, PhoneNumber, CustomerID):
        super().AddNewRecord("UPDATE Customers Set FirstName = '{}', LastName = '{}', PhoneNumber = '{}' WHERE CustomerID = '{}'".format(FirstName, LastName, PhoneNumber, CustomerID))

        
