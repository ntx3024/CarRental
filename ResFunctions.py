import tkinter as RTK
from ResDBFunctions import *
from CustDBFunctions import *


dbRes = ResDBFunctions()
cstDB = CustDBFunctions()

class ResFunctions(object):
    pass

    def popup(self, event):
        try:
            self.treeRes.selection_set(self.treeRes.identify('item', event.x, event.y))
            self.cMenu.post(event.x_root, event.y_root)
        finally:
            print("Did it Show for Res")

    def Reload(self):
        #Clear the existing entry fields
        self.cbNames.set('')
        self.entry_StartDate.delete(0, RTK.END)
        self.entry_EndDate.delete(0, RTK.END)

        #reload the reservations
        results = dbRes.loadAllRes()
        self.BuildTreeView(results)
        

    
        print("Reservations reloaded")

    def AddNewRes(self):
        #Get the values from the Entry Controls
        print("Insert the Row into the databse....")
        cus = self.customer_value.get()
        spacePos = cus.find(' ')
        print(cus[0:spacePos])
        custID = cus[0:spacePos]
        sDate = self.entry_StartDate.get()
        eDate = self.entry_EndDate.get()

        #need to add a check that the new customer is not already listed
        dbCst.AddNewCustomer(fName, lName, phone)

        self.Reload()

    def FindRes(self):
        cus = self.customer_value.get()
        spacePos = cus.find(' ')
        print(cus[0:spacePos])
        custID = cus[0:spacePos]
        sDate = self.entry_StartDate.get()
        eDate = self.entry_EndDate.get()

        print(custID, sDate, eDate)
        #TODO: Find a better why to do the comparisons
        if custID == '' and sDate == '' and eDate=='':
            results = dbRes.loadAllRes()
        else:
            if custID != '':
                results = dbRes.loadResByID(custID)
            else:
                if sDate != '' and eDate == '':
                    results = dbRes.loadResBySDate(sDate)
                else: 
                    if sDate == '' and eDate != '':
                        results = dbRes.loadResByEDate(eDate)
                    else:
                        if sDate != '' and eDate != '':
                            results = dbRes.loadResByDates(sDate, eDate)
                        else:
                            results = dbRes.loadResByAll(custID, sDate, eDate)

     
        self.BuildTreeView(results)

    def Delete(self):
        curItem = self.treeRes.selection()[0]
        selected = self.treeRes.item(curItem)
        resID = selected["values"][0]
        print(resID)
        #dbRes.DeleteReservation(resID)
        print('{} was deleted'.format(resID))

        self.Reload()
       

    def BuildTreeView(self, results):
        if hasattr(self, 'treeRes'):
            self.treeRes.delete(*self.treeRes.get_children())
        else:
            self.treeRes = RTK.ttk.Treeview(self.dataFrame)
            self.treeRes['show']='headings'
            self.treeRes["columns"] = ("ReservationID","Model", "Customer", "StartDate", "EndDate", "RealStartDate", "RealEndDate")
            self.treeRes.column("ReservationID", width=100, anchor=RTK.W)
            self.treeRes.column("Model", width=50, anchor=RTK.W)
            self.treeRes.column("Customer", width=100, anchor=RTK.W)
            self.treeRes.column("StartDate", width=115, anchor=RTK.W)
            self.treeRes.column("EndDate", width=115, anchor=RTK.W)
            self.treeRes.column("RealStartDate", width=115, anchor=RTK.W)
            self.treeRes.column("RealEndDate", width=115, anchor=RTK.W)
            #tree.heading("#0", text='ID', anchor='w')
            #tree.column("#0", anchor="w")
            self.treeRes.heading("ReservationID", text=" ReservationID", anchor=RTK.W) #, anchor=TK.W)
            self.treeRes.heading("Model", text="Model", anchor=RTK.W)
            self.treeRes.heading("Customer", text="Customer", anchor=RTK.W)
            self.treeRes.heading("StartDate", text="Start Date", anchor=RTK.W)
            self.treeRes.heading("EndDate", text="End Date", anchor=RTK.W)
            self.treeRes.heading("RealStartDate", text="Real Start Date", anchor=RTK.W)
            self.treeRes.heading("RealEndDate", text="Real End Date", anchor=RTK.W)
            
            self.treeRes.grid(row=0 ,sticky=RTK.W+RTK.E+RTK.N+RTK.S)
            self.treeRes.pack(side=RTK.LEFT, fill=RTK.BOTH, expand=1)

        for index, dat in enumerate(results):
            self.treeRes.insert("",index, values=(dat[0], dat[1], dat[2], self.FormatDates(dat[3]) , self.FormatDates(dat[4]), self.FormatDates(dat[5]), self.FormatDates(dat[6])))

        #Add the Right Click Event 
        self.treeRes.bind("<ButtonRelease-3>", self.popup)
            

    def FormatDates(self, dateValue):
         dtElements = dateValue.split("-")
         dtFormat = ''
         if len(dtElements) > 1:
            dtFormat = "{:<2}/{:<2}/{:<4}".format(dtElements[1],dtElements[2],dtElements[0])
         return dtFormat
                         

    def BuildTabControl(self, object):
        self.root = object
        self.cMenu = RTK.Menu(self.root, tearoff=0)
        self.cMenu.add_command(label="Delete", command=self.Delete)


        self.topFrame = RTK.Frame(self.root, pady=1, padx=0)
        self.lblFrame = RTK.Frame(self.root, height=40, pady=3, padx=0)
        self.dataFrame = RTK.Frame(self.root, pady=3, padx=0)

        self.topFrame.grid_rowconfigure(1, weight=1)
        self.topFrame.grid_columnconfigure(0, weight=1)

        self.lblFrame.grid_rowconfigure(1, weight=1)
        self.lblFrame.grid_columnconfigure(0, weight=1)
        
        self.dataFrame.grid_rowconfigure(10, weight=1)
        self.dataFrame.grid_columnconfigure(15, weight=1)

        self.topFrame.grid(row=0, sticky='ew')
        self.lblFrame.grid(row=1, sticky='nsew')
        self.dataFrame.grid(row=2, sticky='nsew')


        self.lblCust = RTK.Label(self.lblFrame, text='Select Customer')
        self.lblStartDate = RTK.Label(self.lblFrame, text='Start Date')
        self.lblEndDate = RTK.Label(self.lblFrame, text='End Date')        
        self.btnFind = RTK.Button(self.lblFrame, text='Find..', command=self.FindRes)
        self.btnAddNew = RTK.Button(self.lblFrame, text='Add New', command=self.AddNewRes)
        self.btnReload = RTK.Button(self.lblFrame, text='Reload Reservations', command=self.Reload)
        self.btnDelete = RTK.Button(self.lblFrame, text='Delete Reservation', command=self.Delete)

        self.customer_value = RTK.StringVar()
        self.cbNames = RTK.ttk.Combobox(self.lblFrame, textvariable=self.customer_value, width=45)
        self.cbNames['values'] = cstDB.loadCustomers()

        self.entry_StartDate = RTK.Entry(self.lblFrame)
        self.entry_EndDate = RTK.Entry(self.lblFrame)
        self.entry_Phone = RTK.Entry(self.lblFrame)
        
        self.lblCust.grid(row=0, column=0, columnspan=3)
        self.lblStartDate.grid(row=0, column=3, columnspan=3)
        self.lblEndDate.grid(row=0, column=6, columnspan=3)
#        self.chkHasRes.grid(row=0, column=14, columnspan=3)
        self.btnFind.grid(row=0, column=12, columnspan=3)
        self.btnAddNew.grid(row=0, column=15, columnspan=3)
        self.btnReload.grid(row=1, column=14, columnspan=3)
        self.btnDelete.grid(row=1, column=19, columnspan=3)
        
        self.cbNames.grid(row=1, column=0, columnspan=3)
        self.entry_StartDate.grid(row=1, column=3, columnspan=3)
        self.entry_EndDate.grid(row=1, column=6, columnspan=3, padx=3)

        #Set the Tab Order of the Entry boxes
        self.entry_StartDate.lift()
        self.entry_EndDate.lift()
        self.entry_Phone.lift()
        self.btnFind.lift()
        self.btnAddNew.lift()
        self.btnReload.lift()
        self.btnDelete.lift()
        lblCust = RTK.Label(self.topFrame, text="Reservations -- Filter and Add New Reservations", font=("Helvetica", 16))

        lblCust.grid(row=0)

        self.Reload()
        


       


