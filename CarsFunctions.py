import tkinter as CTK
from CarsDBFunctions import *
from CarReserveDialog import *

dbCars = CarsDBFunctions()

class CarsFunctions(object):
    pass

    def selection(self):
        print(self.popup.selection)
            
    def popup(self, event):
        try:
            self.treeCars.set(self.treeCars.identify_row(event.y))
            self.cMenu.post(event.x_root, event.y_root)
        finally:
            print("Did it Show")

    def ReloadCars(self):
        carList = dbCars.loadAllCars()
        self.BuildTreeView(carList)

    def reserve(self):
        #Get the Selected node
        tvSelected = self.treeCars.selection()[0]
        #Get the ID For the Selected Car
        self.carID = self.treeCars.item(tvSelected, "text")
        dlg = CarReserveDialog(self)
        #TODO:  Force this call after the window closes
        self.ReloadCars()
        #self.ReserveCar(carID)
       

    def BuildTreeView(self, carResults):
        if hasattr(self, 'treeCars'):
            self.treeCars.delete(*self.treeCars.get_children())
        else:
            self.treeCars = CTK.ttk.Treeview(self.root)
            #self.treeCars['show']='headings'
            self.treeCars["columns"] = ("Model","Doors", "Color", "IsRented")
            self.treeCars.column("Model", width=100, anchor=CTK.W)
            self.treeCars.column("Doors", width=175, anchor=CTK.W)
            self.treeCars.column("Color", width=175, anchor=CTK.W)
            self.treeCars.column("IsRented", width=175, anchor=CTK.W)
            #tree.heading("#0", text='ID', anchor='w')
            #tree.column("#0", anchor="w")
            self.treeCars.heading("#0", text="CarID", anchor=CTK.W) 
            self.treeCars.heading("Model", text="Model", anchor=CTK.W)
            self.treeCars.heading("Doors", text="Doors", anchor=CTK.W)
            self.treeCars.heading("Color", text="Color", anchor=CTK.W)
            self.treeCars.heading("IsRented", text="IsRented", anchor=CTK.W)

            #Add the Right Click Event 
            self.treeCars.bind("<Button-3>", self.popup)
            self.treeCars.grid(row=0 ,sticky=CTK.W+CTK.E+CTK.N+CTK.S)
            self.treeCars.pack(side=CTK.LEFT, fill=CTK.BOTH, expand=1)

        #Get a distinct list of the models
        MakeNames = sorted(set(list(zip(*carResults))[1]))

        tvIndex = 0
        #loop throough each make and get its list of models
        for mk in MakeNames:
            #create the parent node
            nodeMake = self.treeCars.insert("", tvIndex, text=mk)
            tvIndex += 1
            #Get a list of all the Models for each make
            MakeModels = [m for m in carResults if m[1] == mk]
            for md in MakeModels:
                #create a node for each model for the make
                self.treeCars.insert(nodeMake, tvIndex, text=md[0], values=(md[2], md[3], md[4], md[5]))
                tvIndex += 1
                

    def BuildTabControl(self, object):
        self.root = object
        self.cMenu = CTK.Menu(self.root, tearoff=0)
        self.cMenu.add_command(label="Reserve", command=self.reserve)
        carList = dbCars.loadAllCars()
        self.BuildTreeView(carList)


       