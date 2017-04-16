import BaseDBFunctions as db

#Class for handling the Car Inventory
class CarsDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadAllCars(self):
        records = super().loadRecords('SELECT C.CarID, M.Make, C.Model, C.Doors FROM MAKES AS M INNER JOIN CARS AS C ON M.MakeID = C.MakeID ORDER BY M.Make, C.Model')
        return records

    def loadCarsByMake(self, make):
        records = super().loadRecords("SELECT C.CarID, M.Make, C.Model, C.Doors FROM MAKES AS M INNER JOIN CARS AS C ON M.MakeID = C.MakeID WHERE M.MAKE = '{}' ORDER BY M.Make, C.Model".format(make))
        return records

    def loadCarsByModel(self, model):
        records = super().loadRecords("SELECT C.CarID, M.Make, C.Model, C.Doors from MODELS as M INNER JOIN CARS AS C ON M.MakeID = C.MakeID WHERE M.MODEL = '{}' ORDER BY M.MAKE, C.MODEL".format(model))
        return records
