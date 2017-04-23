import BaseDBFunctions as db

#Class for handling the Car Inventory
class ResDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadAllRes(self):
        #records = super().loadRecords("SELECT * FROM Reservations")
        records = super().loadRecords("SELECT R.RESERVATIONID , C.MODEL , CT.FIRSTNAME ||' ' || CT.LASTNAME as Customer , R.STARTDATE , R.ENDDATE , ifnull(R.REALSTARTDATE, '') AS REALSTARTDATE , ifnull(R.REALENDDATE, '') AS REALENDDATE FROM Reservations AS R INNER JOIN CARS AS C ON R.CARID = C.CARID INNER JOIN CUSTOMERS AS CT ON R.CUSTOMERID = CT.CUSTOMERID")
        return records

    def loadResByID(self, custID):
        records = super().loadRecords("SELECT R.RESERVATIONID , C.MODEL , CT.FIRSTNAME ||' ' || CT.LASTNAME as Customer , R.STARTDATE , R.ENDDATE , ifnull(R.REALSTARTDATE, '') AS REALSTARTDATE , ifnull(R.REALENDDATE, '') AS REALENDDATE FROM Reservations AS R INNER JOIN CARS AS C ON R.CARID = C.CARID INNER JOIN CUSTOMERS AS CT ON R.CUSTOMERID = CT.CUSTOMERID WHERE CT.CustomerID = '{}'".format(custID))
        return records

    def loadResBySDate(self,sDate):
        records = super().loadRecords("SELECT R.RESERVATIONID , C.MODEL , CT.FIRSTNAME ||' ' || CT.LASTNAME as Customer , R.STARTDATE , R.ENDDATE , ifnull(R.REALSTARTDATE, '') AS REALSTARTDATE , ifnull(R.REALENDDATE, '') AS REALENDDATE FROM Reservations AS R INNER JOIN CARS AS C ON R.CARID = C.CARID INNER JOIN CUSTOMERS AS CT ON R.CUSTOMERID = CT.CUSTOMERID WHERE StartDate = '{}'".format(sDate))
        return records

    def loadResByEDate(self,eDate):
        records = super().loadRecords("SELECT R.RESERVATIONID , C.MODEL , CT.FIRSTNAME ||' ' || CT.LASTNAME as Customer , R.STARTDATE , R.ENDDATE , ifnull(R.REALSTARTDATE, '') AS REALSTARTDATE , ifnull(R.REALENDDATE, '') AS REALENDDATE FROM Reservations AS R INNER JOIN CARS AS C ON R.CARID = C.CARID INNER JOIN CUSTOMERS AS CT ON R.CUSTOMERID = CT.CUSTOMERID WHERE R.EndDate = '{}'".format(eDate))
        return records

    def loadResByDates(self,sDate, eDate):
        records = super().loadRecords("SELECT R.RESERVATIONID , C.MODEL , CT.FIRSTNAME ||' ' || CT.LASTNAME as Customer , R.STARTDATE , R.ENDDATE , ifnull(R.REALSTARTDATE, '') AS REALSTARTDATE , ifnull(R.REALENDDATE, '') AS REALENDDATE FROM Reservations AS R INNER JOIN CARS AS C ON R.CARID = C.CARID INNER JOIN CUSTOMERS AS CT ON R.CUSTOMERID = CT.CUSTOMERID WHERE StartDate = '{}' AND EndDate = '{}'".format(sDate, eDate))
        return records
    
    def loadResByAll(self,custID, sDate, eDate):
        records = super().loadRecords("SELECT R.RESERVATIONID , C.MODEL , CT.FIRSTNAME ||' ' || CT.LASTNAME as Customer , R.STARTDATE , R.ENDDATE , ifnull(R.REALSTARTDATE, '') AS REALSTARTDATE , ifnull(R.REALENDDATE, '') AS REALENDDATE FROM Reservations AS R INNER JOIN CARS AS C ON R.CARID = C.CARID INNER JOIN CUSTOMERS AS CT ON R.CUSTOMERID = CT.CUSTOMERID WHERE CT.CustomerID = '{}' AND StartDate = '{}' AND EndDate = '{}'".format(custID, sDate, eDate))
        return records

    def AddNewReservation(self, carID,  custID, sDate, eDate):
        super().AddNewRecord("INSERT INTO Reservations(CarID, CustomerID, StartDate, EndDate) VALUES('{}', '{}', '{}', '{}')".format(carID, custID, sDate, eDate))

    def DeleteReservation(self, reservationID):
        super().AddRecords("DELETE FROM Reservations WHERE ReservationID = '{}'".format(reservationID))
