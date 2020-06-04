# Ingest Failer
# Simulates a submission call back failure from the DLS for stuck SIPs
#
# The SIP Tool submits SIPs to be ingested by the AVRC ingest stream.
# Once a SIP has been processed, and submission has either succeeded
# or failed, a callback with that result is sent to the SIP Tool.
# In the vast majority of cases, the AVRC ingest stream and
# the SIP Tool communicate reliably. When it does not,
# the SIP will need to be force-failed using the AVSIP API.
#
# christopher.weaver@bl.uk 21/04/2020
import tkinter.messagebox as box
import tkinter.ttk as ttk
from tkinter import (LEFT, RIGHT, Button, Entry, Frame, Scrollbar, Text, Tk,
                     Toplevel)

import pywintypes
import win32api
import win32net

from ingestfailer import api_requests
from ingestfailer.sip import Sip


class Gui():
    """Class for the GUI"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Ingest Failer')
        self.window.geometry("250x30")
        self.enter_sip_id()

    @staticmethod
    def is_num(value):
        return value.isdigit() or value == ''

    def confirm_stuck(self):
        if self.sip.SubmissionInProgress:
            confirm = box.askyesno(f'The SIP is appears stuck', 'Force timeout failure?')
            if confirm:
                if api_requests.post_callback(self.sip.json_methods.get_CallBackURI(), self.sip.json_methods.get_ExternalID(), f"Forced timeout by {full_name}"):
                    box.showinfo('Unlocked', f'{self.sip.title} is now able to be edited')
                else:
                    box.showerror('Error', 'Unable to force time out failure')

        if self.sip.status == 'Failed ingest':
            # box.showerror('Error', f'This pSIP failed ingest\n\n{self.sip.json_methods.get_CallBackMessage()}')
            title = 'Error'
            message = "The pSIP has failed ingest.\n\nFix any errors and retry submission. Check details for possible clues!"
            detail = f"{self.sip.json_methods.get_CallBackMessage()}"
            TopErrorWindow(title, message, detail)
        elif self.sip.status == 'Idle':
            box.showwarning('Idle', 'This pSIP has not yet been completed.')
        elif self.sip.status == 'Ingested':
            box.showinfo('Ingested', 'This SIP has been sucessfully ingested')

    def valid_sip_id(self, event): 
        self.response = api_requests.get_JSON(self.entry.get())
        if self.response is None:
            box.showerror('Error', 'That is not a valid SIP ID')
            # self.entry.delete(0, 'end')
            # confirm_SIP_ID()
        else:
            confirm = box.askyesno(f'Confirm SIP ID {self.entry.get()}', f'{self.response["Title"]}')
            if confirm:
                self.sip = Sip(self.entry.get())
                self.sip.title = self.response["Title"]
                self.confirm_stuck()
        self.entry.delete(0, 'end')

    def enter_sip_id(self):
        self.frame = Frame(self.window)
        self.frame.pack(side=LEFT, padx=5)
        num_check = self.frame.register(self.is_num)
        self.entry = Entry(self.frame, validate='key', validatecommand=(num_check, '%P'))
        self.entry.pack(side=LEFT)
        btn = Button(self.frame, text='Enter SIP ID', command=self.valid_sip_id)
        btn.pack(side=RIGHT, padx=5)
        self.entry.bind("<Return>", self.valid_sip_id)
        self.entry.focus()

# This is a great Message box with an expandable details section taken from:
# https://stackoverflow.com/questions/49072942/how-can-i-add-a-show-details-button-to-a-tkinter-messagebox
class TopErrorWindow(Toplevel):
    def __init__(self, title, message, detail):
        Toplevel.__init__(self)
        self.details_expanded = False
        self.title(title)
        self.geometry('380x95')
        self.minsize(380, 95)
        self.maxsize(425, 250)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        button_frame = Frame(self)
        button_frame.grid(row=0, column=0, sticky='nsew')
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        text_frame = Frame(self)
        text_frame.grid(row=1, column=0, padx=(7, 7), pady=(7, 7), sticky='nsew')
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)

        ttk.Label(button_frame, text=message).grid(row=0, column=0, columnspan=2, pady=(7, 7))
        ttk.Button(button_frame, text='OK', command=self.destroy).grid(row=1, column=0, sticky='e')
        ttk.Button(button_frame, text='Details', command=self.toggle_details).grid(row=1, column=1, sticky='w')

        self.textbox = Text(text_frame, height=6)
        self.textbox.insert('1.0', detail)
        self.textbox.config(state='disabled')
        self.scrollb = Scrollbar(text_frame, command=self.textbox.yview)
        self.textbox.config(yscrollcommand=self.scrollb.set)

    def toggle_details(self):
        if self.details_expanded:
            self.textbox.grid_forget()
            self.scrollb.grid_forget()
            self.geometry('380x95')
            self.details_expanded = False
        else:
            self.textbox.grid(row=0, column=0, sticky='nsew')
            self.scrollb.grid(row=0, column=1, sticky='nsew')
            self.geometry('380x160')
            self.details_expanded = True


# https://superuser.com/questions/1239773/full-name-of-windows-user-name-in-domain-using-python
user_info = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(), win32api.GetUserName(), 2)
full_name = user_info["full_name"]

def main():
    prog_gui = Gui()
    prog_gui.window.mainloop()

if __name__ == "__main__":
    main()
