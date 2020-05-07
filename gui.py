from tkinter import Tk, Button, Frame, Entry, LEFT, RIGHT
import tkinter.messagebox as box
from api_requests import ApiRequests
from Ingest_Failer import SIP
# from api_requests import ApiRequests
from json_methods import json_methods

class Gui(object):

    def __init__(self):
        self.window = Tk()
        self.window.title('Ingest Failer')
        self.window.geometry("250x30")

    @staticmethod
    def is_num(value):
        return value.isdigit() or value == ''

    def valid_SIP_ID(self, event=None):
        self.response = ApiRequests.get_JSON(self.entry.get())
        if self.response is None:
            box.showerror('Error', 'That is not a valid SIP ID')
            # self.entry.delete(0, 'end')
            # confirm_SIP_ID()
        else:
            confirm = box.askyesno(f'Confirm SIP ID {self.entry.get()}', f'{self.response["Title"]}')
            if confirm:
                self.valid_sip = True
                self.sip_id = self.entry.get()
        self.entry.delete(0, 'end')

    def enter_SIP_ID(self):
        self.frame = Frame(self.window)
        self.frame.pack(side=LEFT, padx=5)
        num_check = self.frame.register(self.is_num)
        self.entry = Entry(self.frame, validate='key', validatecommand=(num_check, '%P'))
        self.entry.pack(side=LEFT)
        btn = Button(self.frame, text='Enter SIP ID', command=self.valid_SIP_ID)
        btn.pack(side=RIGHT, padx=5)
        self.entry.bind("<Return>", self.valid_SIP_ID)
        self.entry.focus()
        


                




# def enter_failure_msg(self):
#     pass


prog_gui = Gui()
prog_gui.enter_SIP_ID()
# my_sip = enter_SIP_ID()
# print(my_sip)
# # valid_sip = prog_gui.set_sip_id()

prog_gui.window.mainloop()
print(prog_gui.valid_sip, prog_gui.sip_id)