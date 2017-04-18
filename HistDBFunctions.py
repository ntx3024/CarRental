import BaseDBFunctions as db

#Class for handling the Customer Inventory
class HistDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadCustHist(self):
        records = super().loadRecords('SELECT C.FirstName , C.LastName , R.ReservationID , M.Model , R.RealStartDate , R.RealEndDate FROM RESERVATIONS AS R INNER JOIN CUSTOMERS AS C ON R.CustomerID = R.CustomerID INNER JOIN CARS AS M ON R.CarID = M.CarID WHERE R.CustomerID = C.CustomerID AND R.CarID = M.CarID ORDER BY R.RealStartDate')
        return records

    def loadRes(self):
        records = super().loadRecords('SELECT C.FirstName , C.LastName, R.ReservationID , M.Model , R.StartDate , R.EndDate FROM RESERVATIONS AS R INNER JOIN CUSTOMERS AS C ON R.CustomerID = R.CustomerID INNER JOIN CARS AS M ON R.CarID = M.CarID WHERE R.CustomerID = C.CustomerID AND R.CarID = M.CarID ORDER BY R.StartDate')
        return records
