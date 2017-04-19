import sqlite3
import os


class BaseDBFunctions():
    def __init__(self):
        #get the directory of the file currently open
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        #Open a connection to the database
        self.conn = sqlite3.connect(os.path.join(self.dir_path, 'db', 'KGCars.db'))
        self.conn.enable_load_extension(True)
        #create the cursor for the connection
        self.curs = self.conn.cursor()

    def loadRecords(self, sqlString):
        self.curs.execute(sqlString)
        records = self.curs.fetchall()
        return records

    def AddNewRecord(self, sqlString):
        #Execute the SQL Statement
        self.curs.execute(sqlString)
        #Commit the Rows to the database
        self.conn.commit()
        self.curs.close()
        #TODO:  Find best way to do this...
        self.conn = sqlite3.connect(os.path.join(self.dir_path, 'db', 'KGCars.db'))
        self.conn.enable_load_extension(True)
        #create the cursor for the connection
        self.curs = self.conn.cursor()

    
    def CloseCursor(self):
        self.curs.close()


