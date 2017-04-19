from tkinter import *
import CarsDBFunctions as db

#from MakesDBFunctions import *

class TVClassExample(object):
    def __init__(self):
        self.root = Tk()
        self.cMenu = Menu(self.root)
        self.cMenu.add_command(label="Reserve", command=self.reserve)

        tree = ttk.Treeview(self.root)
        tree["columns"] = ("Model","Doors", "Color", "IsRented")
        #tree.column("Make", width=175)
        tree.column("Model", width=175)
        tree.column("Doors", width=100)
        tree.column("Color", width=100)
        tree.column("IsRented", width=100)
        tree.heading("#0", text='CarID', anchor='w')
        #tree.column("#0", anchor="w")
        #tree.heading("Make", text="Make")
        tree.heading("Model", text="Model")
        tree.heading("Doors", text="Doors")
        tree.heading("Color", text="Color")
        tree.heading("IsRented", text="Rented")

        mkDB = db.CarsDBFunctions()
        models = mkDB.loadAllCars()

        #Get a distinct list of the models
        MakeNames = sorted(set(list(zip(*models))[1]))

        tvIndex = 0
        #loop throough each make and get its list of models
        for mk in MakeNames:
            #create the parent node
            nodeMake = tree.insert("", tvIndex, text=mk)
            tvIndex += 1
            #Get a list of all the Models for each make
            MakeModels = [m for m in models if m[1] == mk]
            for md in MakeModels:
                #create a node for each model for the make
                tree.insert(nodeMake, tvIndex, text=md[0], values=(md[2], md[3], md[4], md[5]))
                tvIndex += 1
                

        #for index, dat in enumerate(models):
        #    tree.insert("",index, text= dat[0], values=(dat[1], dat[2], dat[3]))

        tree.bind("<Button-3>", self.popup)


        tree.pack(side=TOP, fill=BOTH, expand=1)
        
    def popup(self, event):
        self.cMenu.post(event.x_root, event.y_root)

    def reserve(self):
            print("Do Something...")
