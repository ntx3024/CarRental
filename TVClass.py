from tkinter import *
import CarsDBFunctions as db

#from MakesDBFunctions import *

class TVClassExample(object):
    def __init__(self):
        self.root = Tk()
        tree = ttk.Treeview(self.root)
        tree["columns"] = ("CarID","Make" ,"Model" , "Doors")
        tree.column("CarID", width=100)
        tree.column("Make", width=175)
        tree.column("Model", width=175)
        tree.column("Doors", width=100)
        #tree.heading("#0", text='ID', anchor='w')
        #tree.column("#0", anchor="w")
        tree.heading("CarID", text="CarID")
        tree.heading("Make", text="Make")
        tree.heading("Model", text="Model")
        tree.heading("Doors", text="Doors")

        mkDB = db.CarsDBFunctions()
        models = mkDB.loadAllCars()

        for index, dat in enumerate(models):
            tree.insert("",index, values=(dat[0], dat[1], dat[2], dat[3]))


        tree.pack()
    

