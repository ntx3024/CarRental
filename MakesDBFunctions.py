import BaseDBFunctions as db

#Class for handling the Makes of Cars
class MakesDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()
 
    def loadAllMakes(self):
        records = super().loadRecords('SELECT * FROM MAKES ORDER BY Make')
        return records

    def loadAllMakesInput(self):
        records = super().loadRecords('SELECT * FROM MAKES ORDER BY Make')
        idVal = []
        makeText = []
        
        for row in records:
            #idVal.append(row[0])
            makeText.append(row[1])
    
        #TODO:  Figure out how to return and use a dictionary
        return makeText


makesDB = MakesDBFunctions()
allMakes = makesDB.loadAllMakes()


       
    


