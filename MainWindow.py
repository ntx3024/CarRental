from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from MakesDBFunctions import *
from CarsDBFunctions import *


#Not sure best way to call these
dbMk = MakesDBFunctions()
dbCars = CarsDBFunctions()

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
        self.tabVehicles = ttk.Frame(self.nb)
        self.tabCustomers = ttk.Frame(self.nb)
        self.tabReservations = ttk.Frame(self.nb)
        self.nb.add(self.tabVehicles, text="Vehicles")
        self.nb.add(self.tabCustomers, text="Customers")
        self.nb.add(self.tabReservations, text="Reservations")
        self.nb.pack(side=BOTTOM, fill=BOTH, expand=Y)
        
        self.lstMakes = Listbox(self.tabVehicles, selectmode=SINGLE, relief=FLAT)
        allMakes = dbMk.loadAllMakes()
        self.lstMakes.insert(END, "Makes")
        self.lstMakes.insert(END, "----------")
        self.lstMakes.insert(END, " ")
        for m in allMakes:
            self.lstMakes.insert(END, m[1])

        self.lstMakes.bind('<<ListboxSelect>>', self.lstMakeSelectionChanged)
        self.lstMakes.pack(side=LEFT, fill=BOTH)

        self.lstModels = Listbox(self.tabVehicles, selectmode=SINGLE, relief=FLAT)
        self.lstModels.insert(END, "Models")
        self.lstModels.insert(END, "----------")
        self.lstModels.insert(END, " ")
        
        self.lstModels.bind('<<ListboxSelect>>', self.lstModelSelectionChanged)
        self.lstModels.pack(side=LEFT, fill=BOTH)

        self.lstDetails = Listbox(self.tabVehicles, selectmode=SINGLE, relief=FLAT)
        self.lstDetails.insert(END, "Details")
        self.lstDetails.insert(END, "----------")
        self.lstDetails.insert(END, " ")
        self.lstDetails.pack(side=LEFT, fill=BOTH)

        Label(self.tabCustomers, text='First Name', relief=FLAT).grid(row = 1, column = 0)

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
        print("New File!")
    def OpenFile(self):
        print(name)
    def About(self):
        print("This is a program to track and create reservations for vehicles.")
    
    def lstMakeSelectionChanged(self, event):
        m = event.widget
        index = int(m.curselection()[0])
        value = m.get(index)
        cars = dbCars.loadCarsByMake(value)
        for index, dat in enumerate(cars):
            self.lstModels.delete(0, END)
            self.lstModels.insert(END, "Models")
            self.lstModels.insert(END, "----------")
            self.lstModels.insert(END, " ")
            self.lstModels.insert(END, '{}'.format(dat[2]))
            print("CarID: {} - Make: {} - Model: {} - Doors: {}".format(dat[0],dat[1],dat[2],dat[3]))

    def lstModelSelectionChanged(self, event):
        m = event.widget
        index = int(m.curselection()[0])
        value = m.get(index)
        model = dbcars.loadCarsByModel(value)
        for index, dat in enumerate(model):
            self.lstDetails.detete(0, END)
            self.lstDetails.insert(END, "Details")
            self.lstDetails.insert(END, "----------")
            self.lstDetails.insert(END, " ")
            self.lstDetails.insert(END, "Doors: {}".format(dat[3]))
            



root = Tk()
my_gui = MainWindow(root)
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoPanel = Label(root, image = logo)
logoPanel.pack(side="right", fill ="both", expand="no")
title = ImageTk.PhotoImage(Image.open("companytitle.png"))
titlePanel = Label(root, image = title)
titlePanel.pack(side="left" , fill ="both", expand="yes")
root.mainloop()



