#TODO:  Find out why the import names must be unique
import tkinter as CRTK


class CarReserveDialog(object):
    root = None

    def __init__(self, parent):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        #self.tki = CRTK.Tk()
        self.top = CRTK.Toplevel(CarReserveDialog.root)
        self.CarRentedEvent = CRTK.Event
        self.frm = CRTK.Frame(self.top, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.label = CRTK.Label(self.frm, text="Reserving CarID {}".format(parent.carID))
        self.label.pack(padx=4, pady=4)

        self.lblCust = CRTK.Label(self.frm, text="Select the Customer Renting the Car")
        self.lblCust.pack(padx=4, pady=4)

        #TODO:  Add Combo Box or List Box of Customers to Select from....


        self.b_cancel = CRTK.Button(self.frm, text='Cancel')
        self.b_cancel['command'] = self.top.destroy
        self.b_cancel.pack(padx=4, pady=4)    

        self.b_OK = CRTK.Button(self.frm, text='OK')
        self.b_OK['command'] = self.rentCar
        self.b_OK.pack(padx=4, pady=4)  

    def rentCar(self):
        print("Insert the Row into the databse....")


