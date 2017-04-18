from tkinter import *
from tkinter import ttk
import ipywidgets as ipyw
from PIL import ImageTk, Image
from MakesDBFunctions import *
from CarsDBFunctions import *
from HistDBFunctions import *
from TVClass import TVClassExample


#Not sure best way to call these
dbMk = MakesDBFunctions()
dbCars = CarsDBFunctions()
dbHist = HistDBFunctions()

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
        self.tabTree = ttk.Frame(self.nb)
        self.nb.add(self.tabVehicles, text="Vehicles")
        self.nb.add(self.tabCustomers, text="Customers")
        self.nb.add(self.tabReservations, text="Reservations")
        self.nb.add(self.tabTree, text="VehiclesTree")
        self.nb.pack(side=BOTTOM, fill=BOTH, expand=1)

        #make listbox for makes of vehicles and populate with all makes
        self.lstMakes = Listbox(self.tabVehicles, selectmode=SINGLE, relief=FLAT)
        allMakes = dbMk.loadAllMakes()
        self.lstMakes.insert(END, "Makes")
        self.lstMakes.insert(END, "----------")
        self.lstMakes.insert(END, " ")
        for m in allMakes:
            self.lstMakes.insert(END, m[1])
        #add information to listbox and raise event handles
        self.lstMakes.bind('<<ListboxSelect>>', self.lstMakeSelectionChanged)
        self.lstMakes.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.lstModels = Listbox(self.tabVehicles, selectmode=SINGLE, relief=FLAT)
        self.lstModels.insert(END, "Models")
        self.lstModels.insert(END, "----------")
        self.lstModels.insert(END, " ")
        
        self.lstModels.bind('<<ListboxSelect>>', self.lstModelSelectionChanged)
        self.lstModels.pack(side=LEFT, fill=BOTH, expand=1)

        self.lstDetails = Listbox(self.tabVehicles, selectmode=SINGLE, relief=FLAT)
        self.lstDetails.insert(END, "Details")
        self.lstDetails.insert(END, "----------")
        self.lstDetails.insert(END, " ")
        self.lstDetails.pack(side=LEFT, fill=BOTH, expand=1)

        #Add tree to Vehicle Tree Tab
        models = dbCars.loadAllCars()
        self.treeCars = ttk.Treeview(self.tabTree)
        self.treeCars['show']='headings'
        self.treeCars["columns"] = ("CarID","Make" ,"Model" , "Doors")
        self.treeCars.column("CarID", width=100, anchor=S)
        self.treeCars.column("Make", width=175, anchor=S)
        self.treeCars.column("Model", width=175, anchor=S)
        self.treeCars.column("Doors", width=100, anchor=S)
        self.treeCars.heading("CarID", text="CarID", anchor=W)
        self.treeCars.heading("Make", text="Make")
        self.treeCars.heading("Model", text="Model")
        self.treeCars.heading("Doors", text="Doors", anchor=E)
        for index, dat in enumerate(models):
            self.treeCars.insert("",index, values=(dat[0], dat[1], dat[2], dat[3]))
        self.treeCars.pack(side=TOP, fill=BOTH, expand=1)

        #Add tree to bottom of customer tab
        custHist = dbHist.loadCustHist()
        self.treeCust = ttk.Treeview(self.tabCustomers)
        self.treeCust['show']='headings'
        self.treeCust["columns"] = ("FirstName","LastName","ReservationID","Model","RealStartDate","RealEndDate")
        self.treeCust.column("FirstName", width=100, anchor=S)
        self.treeCust.column("LastName", width=100, anchor=S)
        self.treeCust.column("ReservationID", width=50, anchor=S)
        self.treeCust.column("Model", width=150, anchor=S)
        self.treeCust.column("RealStartDate", width=100, anchor=S)
        self.treeCust.column("RealEndDate", width=100, anchor=S)
        #add headings
        self.treeCust.heading("FirstName", text="First Name", anchor=W)
        self.treeCust.heading("LastName", text="Last Name")
        self.treeCust.heading("ReservationID", text="Reservation ID")
        self.treeCust.heading("Model", text="Model")
        self.treeCust.heading("RealStartDate", text="Start Date")
        self.treeCust.heading("RealEndDate", text="End Date", anchor=E)
        for index, dat in enumerate(custHist):
            self.treeCust.insert("",index, values=(dat[0], dat[1], dat[2], dat[3], dat[4]))
        self.treeCust.pack(side=BOTTOM, fill=BOTH, expand=1)

        #add labels and buttons to customer tab    
        Label(self.tabCustomers, text='First Name', relief=FLAT).pack(side=LEFT, anchor=N+W)
        self.fNameEntry = Entry(master=self.tabCustomers).pack(side=LEFT, anchor=N+W)

        Label(self.tabCustomers, text='Last Name', relief=FLAT).pack(side=LEFT, anchor=N+W)
        self.lNameEntry = Entry(master=self.tabCustomers).pack(side=LEFT, anchor=N+W)

        Label(self.tabCustomers, text='Phone Number', relief=FLAT).pack(side=LEFT, anchor=N+W)
        self.phoneNum = Entry(master=self.tabCustomers).pack(side=LEFT, anchor=N+W)
        
        self.addBtn = Button(self.tabCustomers, text='Add Customer')
        self.addBtn.pack(side=LEFT, anchor=N+W)

        self.histBtn = Button(self.tabCustomers, text='Show History')
        self.histBtn.pack(side=LEFT, anchor=N+W)

        #add tree to reservation tab
        reservation = dbHist.loadRes()
        self.treeRes = ttk.Treeview(self.tabReservations)
        self.treeRes['show']='headings'
        self.treeRes["columns"] = ("ReservationID","Model","FirstName","LastName","StartDate","EndDate")
        self.treeRes.column("ReservationID", width=100, anchor=S)
        self.treeRes.column("Model", width=100, anchor=S)
        self.treeRes.column("FirstName", width=50, anchor=S)
        self.treeRes.column("LastName", width=150, anchor=S)
        self.treeRes.column("StartDate", width=100, anchor=S)
        self.treeRes.column("EndDate", width=100, anchor=S)
        #add headings
        self.treeRes.heading("ReservationID", text="Reservation ID", anchor=W)
        self.treeRes.heading("Model", text="Model")
        self.treeRes.heading("FirstName", text="First Name")
        self.treeRes.heading("LastName", text="Last Name")
        self.treeRes.heading("StartDate", text="Start Date")
        self.treeRes.heading("EndDate", text="End Date", anchor=E)
        for index, dat in enumerate(reservation):
            self.treeRes.insert("",index, values=(dat[0], dat[1], dat[2], dat[3], dat[4]))
        self.treeRes.pack(side=RIGHT, fill=BOTH, expand=1)

        #add labels and button to reservation tab
        Label(self.tabReservations, text='First Name', relief=FLAT).pack(side=TOP, anchor=N+W)
        self.fNameEntry = Entry(master=self.tabReservations).pack(side=TOP, anchor=N+W)

        Label(self.tabReservations, text='Last Name', relief=FLAT).pack(side=TOP, anchor=N+W)
        self.lNameEntry = Entry(master=self.tabReservations).pack(side=TOP, anchor=N+W)

        Label(self.tabReservations, text='Pickup Day', relief=FLAT).pack(side=TOP, anchor=N+W)
        self.puEntry = Entry(master=self.tabReservations).pack(side=TOP, anchor=N+W)
        self.puEntry#(8, 'MM-DD-YYYY')

        Label(self.tabReservations, text='Drop Off Day', relief=FLAT).pack(side=TOP, anchor=N+W)
        self.doEntry = Entry(master=self.tabReservations).pack(side=TOP, anchor=N+W)

        self.findResBtn = Button(self.tabReservations, text='Find Reservation')
        self.findResBtn.pack(side=TOP, anchor=N+W)

        

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
        print("This is a program to track and create reservations for vehicles.")
    
    def lstMakeSelectionChanged(self, event):
        m = event.widget
        if m.curselection() != '':
            index = int(m.curselection()[0])
            value = m.get(index)
            cars = dbCars.loadCarsByMake(value)
            self.lstModels.delete(0, END)
            self.lstModels.insert(END, "Models")
            self.lstModels.insert(END, "----------")
            self.lstModels.insert(END, " ")
            self.lstDetails.delete(0, END)
            self.lstDetails.insert(END, "Details")
            self.lstDetails.insert(END, "----------")
            self.lstDetails.insert(END, " ")
            for index, dat in enumerate(cars):
                self.lstModels.insert(END, '{}'.format(dat[1]))



    def lstModelSelectionChanged(self, event):
        m = event.widget
        if m.curselection() != '':
            index = int(m.curselection()[0])
            value = m.get(index)
            cars = dbCars.loadCarsByModel(value)
            self.lstDetails.delete(0, END)
            self.lstDetails.insert(END, "Details")
            self.lstDetails.insert(END, "----------")
            self.lstDetails.insert(END, " ")
            self.lstDetails.insert(END, "Colors:\n")
            for index, dat in enumerate(cars):
                self.lstDetails.insert(END, "              {}".format(dat[2]))
            self.lstDetails.insert(END, "Doors: {}".format(dat[1]))



root = Tk()
my_gui = MainWindow(root)
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoPanel = Label(root, image = logo)
logoPanel.pack(side="right", fill ="both", expand="no")
title = ImageTk.PhotoImage(Image.open("companytitle.png"))
titlePanel = Label(root, image = title)
titlePanel.pack(side="left" , fill ="both", expand="yes")
root.mainloop()



