import tkinter as TK
from CustDBFunctions import *
from CustEditDialog import *
from ResDBFunctions import *

dbCst = CustDBFunctions()
dbRes = ResDBFunctions()


class CustFunctions(object):
    pass

    def popup(self, event):
        try:
            self.treeCust.selection_set(self.treeCust.identify('item', event.x, event.y))
            self.cMenu.post(event.x_root, event.y_root)
        finally:
            print("Did it Show, cust")

    #Filter/Reload the Results based of the entries
    def FindCustomer(self):
        fName = self.entry_FName.get()
        lName = self.entry_LName.get()

        #TODO: Find a better why to do the comparisons
        if fName == '' and lName == '':
            results = dbCst.loadCustomers()
        else:
            if fName != '' and lName != '':
                results = dbCst.loadCustomersByName(fName, lName)
            else:
                if fName != '' and lName == '':
                    results = dbCst.loadCustomersByFName(fName)
                else:
                    results = dbCst.loadCustomersByLName(lName)

        self.BuildTreeView(results)

    def Reload(self):
        results = dbCst.loadCustomers()
        self.BuildTreeView(results)
        self.entry_FName.delete(0, TK.END)
        self.entry_LName.delete(0, TK.END)
        self.entry_Phone.delete(0, TK.END)

    #Edit current customer
    def Edit(self):
        curItem = self.treeCust.selection()
        selected = self.treeCust.item(curItem)
        self.custID = selected["values"][0]
        self.root.wait_window(CustEditDialog(self))

        self.Reload()


    #Add a new Customer
    def AddNewCustomer(self):
        #Get the values from the Entry Controls
        fName = self.entry_FName.get()
        lName = self.entry_LName.get()
        phone = self.entry_Phone.get()

        #need to add a check that the new customer is not already listed
        dbCst.AddNewCustomer(fName, lName, phone)

        self.Reload()

    def Delete(self):
        curItem = self.treeCust.selection()[0]
        selected = self.treeCust.item(curItem)
        custID = selected["values"][0]
        dbCst.DeleteCustomer(custID)

        self.Reload()

    #TODO figure out if I will need this anywhere
##    def rentCar(self):
##        cus = self.customer_value.get()
##        spacePos = cus.find(' ')
##        print(cus[0:spacePos])
        

    def BuildTreeView(self, results):
        if hasattr(self, 'treeCust'):
            self.treeCust.delete(*self.treeCust.get_children())
        else:
            self.treeCust = TK.ttk.Treeview(self.dataFrame)
            self.treeCust['show']='headings'
            self.treeCust["columns"] = ("CustomerID","FirstName","LastName","PhoneNumber")
            self.treeCust.column("CustomerID", width=0)
            self.treeCust.column("FirstName", width=100, anchor=TK.W)
            self.treeCust.column("LastName", width=175, anchor=TK.W)
            self.treeCust.column("PhoneNumber", width=175, anchor=TK.W)
            #tree.heading("#0", text='ID', anchor='w')
            #tree.column("#0", anchor="w")
            self.treeCust.heading("CustomerID", text="ID", anchor=TK.W) 
            self.treeCust.heading("FirstName", text="First Name", anchor=TK.W) 
            self.treeCust.heading("LastName", text="Last Name", anchor=TK.W) 
            self.treeCust.heading("PhoneNumber", text="Phone", anchor=TK.W) 
            self.treeCust.bind('<ButtonRelease-1>', self.selectItem)
            self.treeCust.bind('<Button-3>', self.popup)

            self.treeCust.grid(row=0 ,sticky=TK.W+TK.E+TK.N+TK.S)
            self.treeCust.pack(side=TK.LEFT, fill=TK.BOTH, expand=1)

        for index, dat in enumerate(results):
            self.treeCust.insert("",index, values=(dat[0], dat[1], dat[2], dat[3]))

        self.treeCust.bind("<ButtonRelease-3>", self.popup)

    def selectItem(self, value):
        curItem = self.treeCust.focus()
        selected = self.treeCust.item(curItem)
        value = selected["values"][0]
        return(value)


    def BuildTabControl(self, object):
        self.root = object
        self.cMenu = TK.Menu(self.root, tearoff=0)
        self.cMenu.add_command(label="Delete", command=self.Delete)
        self.cMenu.add_command(label="Edit", command=self.Edit)


        self.topFrame = TK.Frame(self.root, pady=1, padx=0)
        self.lblFrame = TK.Frame(self.root, height=40, pady=3, padx=0)
        self.dataFrame = TK.Frame(self.root, pady=3, padx=0)

        self.topFrame.grid_rowconfigure(1, weight=1)
        self.topFrame.grid_columnconfigure(0, weight=1)

        self.lblFrame.grid_rowconfigure(1, weight=1)
        self.lblFrame.grid_columnconfigure(0, weight=1)
        
        self.dataFrame.grid_rowconfigure(10, weight=1)
        self.dataFrame.grid_columnconfigure(15, weight=1)

        self.topFrame.grid(row=0, sticky='ew')
        self.lblFrame.grid(row=1, sticky='nsew')
        self.dataFrame.grid(row=2, sticky='nsew')

        self.lblLName = TK.Label(self.lblFrame, text='Last Name')
        self.lblFName = TK.Label(self.lblFrame, text='First Name')
        self.lblPhone = TK.Label(self.lblFrame, text='Phone Number')
        self.chkHasRes = TK.Checkbutton(self.lblFrame, text='Has Reservations')
        self.btnFind = TK.Button(self.lblFrame, text='Find..', command=self.FindCustomer)
        self.btnAddNew = TK.Button(self.lblFrame, text='Add New', command=self.AddNewCustomer)
        self.btnReload = TK.Button(self.lblFrame, text='Reload Customers', command=self.Reload)
        self.btnDelete = TK.Button(self.lblFrame, text='Delete Customer', command=self.Delete)


        self.entry_FName = TK.Entry(self.lblFrame)
        self.entry_LName = TK.Entry(self.lblFrame)
        self.entry_Phone = TK.Entry(self.lblFrame)
        
        self.lblFName.grid(row=0, column=0, columnspan=3)
        self.lblLName.grid(row=0, column=4, columnspan=3)
        self.lblPhone.grid(row=0, column=9, columnspan=3)
        self.chkHasRes.grid(row=0, column=14, columnspan=3)
        self.btnFind.grid(row=0, column=18, columnspan=3)
        self.btnAddNew.grid(row=0, column=21, columnspan=3)
        self.btnReload.grid(row=1, column=14, columnspan=3)
        self.btnDelete.grid(row=1, column=19, columnspan=3)
        

        self.entry_FName.grid(row=1, column=0, columnspan=3)
        self.entry_LName.grid(row=1, column=4, columnspan=3, padx=3)
        self.entry_Phone.grid(row=1, column=9, columnspan=3, padx=3)

        #Set the Tab Order of the Entry boxes
        self.entry_FName.lift()
        self.entry_LName.lift()
        self.entry_Phone.lift()
        self.btnFind.lift()
        self.btnAddNew.lift()
        self.btnReload.lift()
        self.btnDelete.lift()
        lblCust = TK.Label(self.topFrame, text="Customers -- Filter and Add New Customers", font=("Helvetica", 16))

        lblCust.grid(row=0)

        self.Reload()




