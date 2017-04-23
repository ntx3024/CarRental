import tkinter as CETK
from WindowFunctions import *

#from tkinter import messagebox
from CustDBFunctions import *
from CarsDBFunctions import *
from ResDBFunctions import *
from BaseDBFunctions import *
from CustFunctions import *

cstDB = CustDBFunctions()
carDB = CarsDBFunctions()
resDB = ResDBFunctions()
baseDB = BaseDBFunctions()

class CustEditDialog(object):
    root = None

    def __init__(self, parent):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        self._w = CETK.Toplevel(parent.root)
        self.frm = CETK.Frame(self._w, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.custID = parent.custID

        output = cstDB.loadCustomerByID(self.custID)
        FName = output[0][1]
        LName = output[0][2]
        num = output[0][3]



        self.label = CETK.Label(self.frm, text="Editing: {} {}".format(FName, LName))
        self.label.pack(padx=4, pady=4)

        self.lblFName = CETK.Label(self.frm, text='First Name')
        self.lblFName.pack(padx=4, pady=4)
        self.entryFName = CETK.Entry(self.frm)
        self.entryFName.pack(pady=4, padx=4)
        self.entryFName.insert(0, FName)


        self.lblLName = CETK.Label(self.frm, text = 'Last Name')
        self.lblLName.pack(padx=4, pady=4)
        self.entryLName = CETK.Entry(self.frm)
        self.entryLName.pack(pady=4, padx=4)
        self.entryLName.insert(0, LName)

        self.lblNum = CETK.Label(self.frm, text = 'Phone Number')
        self.lblNum.pack(padx=4, pady=4)
        self.entryNum = CETK.Entry(self.frm)
        self.entryNum.pack(pady=4, padx=4)
        self.entryNum.insert(0, num)

        self.b_cancel = CETK.Button(self.frm, text='Cancel')
        self.b_cancel['command'] = self._w.destroy
        self.b_cancel.pack(padx=4, pady=4)    

        self.b_OK = CETK.Button(self.frm, text='OK')
        self.b_OK['command'] = self.updateCust
        self.b_OK.pack(padx=4, pady=4)
        WindowFunctions.center(self._w)


    def updateCust(self):
        print("Updating the Name into the databse....")
        FirstName = self.entryFName.get()
        LastName = self.entryLName.get()
        PhoneNumber = self.entryNum.get()
        CustomerID = self.custID
        cstDB.UpdateCustomer(FirstName, LastName, PhoneNumber, CustomerID)

        
        

        



