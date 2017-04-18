import BaseDBFunctions as db

#Class for handling the Customer Inventory
class CustDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadCustHist(self):
        records = super().loadRecords('SELECT C.FirstName, C.LastName, R.ReservationID, M.Model, R.StartDate, R.EndDate, R.RealStartDate, R.RealEndDate FROM RESERVATIONS AS R, CUSTOMERS AS C, CARS as M WHERE  R.CustomerID = C.CustomerID AND R.CarID = M.CarID ORDER BY R.RealStartDate')
        return records
