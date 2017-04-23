from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from WindowFunctions import *
from PIL import ImageTk, Image
from MakesDBFunctions import *
from CarsDBFunctions import *
from CustDBFunctions import *
from TVClass import TVClassExample
from CustFunctions import *
from CarsFunctions import *
from ResFunctions import *

#Not sure best way to call these
dbMk = MakesDBFunctions()
dbCars = CarsDBFunctions()
dbCust = CustDBFunctions()
CustF = CustFunctions()
CarsF = CarsFunctions()
ResF = ResFunctions()

class MainWindow:
    def __init__(self, master): 
        #Create a Variable for Makes class
        self.master = master
        self.master.geometry("800x500")
        self.demoPanel = Frame(master)
        self.initMenu()
        self.demoPanel.pack(side=BOTTOM) #, fill=BOTH, expand=Y)
                    
        
        master.title("O\'Brien Car Rental")

        allModels = dbMk.loadAllMakes()
        self.model_value = StringVar()


        #Create tabs
        self.nb = ttk.Notebook(master)
        #self.tabVehicles = ttk.Frame(self.nb)
        self.tabCustomers = ttk.Frame(self.nb)
        self.tabReservations = ttk.Frame(self.nb)
        self.tabVehicles = ttk.Frame(self.nb)


        
        self.nb.add(self.tabVehicles, text="Vehicles")
        self.nb.add(self.tabCustomers, text="Customers")
        self.nb.add(self.tabReservations, text="Reservations")
        #self.nb.add(self.tabVehicles, text="Vehicles")
        self.nb.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.tabCustomers = CustF.BuildTabControl(self.tabCustomers)
        self.tabVehicles = CarsF.BuildTabControl(self.tabVehicles)
        self.tabReservations= ResF.BuildTabControl(self.tabReservations)
        WindowFunctions.center(self.master)
        

    
    def greet(self):
        print("Greetings!")

    def model_selected(self, event) :
        print("They selected a model {0}".format(self.model_value.get()))
    
    #Build the menu for the main window
    

        
    def initMenu(self):
       root.iconbitmap(default='logo.ico')
       menu = Menu(self.master)
       root.config(menu=menu)
       filemenu = Menu(menu)
       menu.add_cascade(label="File", menu=filemenu)

       #build the File -> New Menus
       filemenuNew = Menu(menu)
       filemenuNew.add_command(label="Make", command=self.NewFile)
       filemenuNew.add_command(label="Model", command=self.NewFile)
       filemenuNew.add_separator()
       filemenuNew.add_command(label="Customer", command=self.NewFile)
       filemenu.add_cascade(label="New", menu=filemenuNew)
       filemenu.add_separator()
       filemenu.add_command(label="Exit", command=root.quit)
       helpmenu = Menu(menu)
       menu.add_cascade(label="Help", menu=helpmenu)
       helpmenu.add_command(label="About...", command=self.About)


    def NewFile(self):
        print("THis is a test...")
        TkC = TVClassExample()
    def OpenFile(self):
        print(name)
    def About(self):
        messagebox.showinfo("About O\'Brien Car Rental", "Thank you for using my application")
        
    



root = Tk()
my_gui = MainWindow(root)
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoPanel = Label(root, image = logo)
logoPanel.pack(side="right", fill ="both", expand="no")
title = ImageTk.PhotoImage(Image.open("companytitle.png"))
titlePanel = Label(root, image = title)
titlePanel.pack(side="left" , fill ="both", expand="yes")
root.mainloop()



