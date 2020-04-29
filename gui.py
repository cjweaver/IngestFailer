from Tkinter import Tk, Button, Frame
import tkinter.messagebox as box

class Gui(object):

    def __init__(self):
        self.window = Tk()
        self.window.title('Ingest Failer')
        self.window.geometry("250x30")

    
class enter_SIP_ID(Gui):

    def __init__(self):
        super(enter_SIP_ID, self).__init__()
        self.frame = Frame(self.window)
        self.frame.pack(side=LEFT, padx=5)

    def set_sip_id(self):    
        
        def is_num(value):
            return value.isdigit() or value == ''
        
        num_check = self.frame.register(is_num)
    
        self.entry = Entry(self.frame, validate='key', validatecommand=(num_check, '%P'))
        self.entry.pack(side=LEFT)

        def confirm_SIP_ID(event=None):
            # Call the SIP API to check the SIP ID is valid
            if False: # type(self.entry.get()) is not int:
                box.showerror('Error', 'That is not a valid SIP ID')
                # self.entry.delete(0, 'end')
                # confirm_SIP_ID()
            else:
                confirm = box.askyesno('Confirm SIP ID', self.entry.get())
                if confirm:
                    
                    # sip.sip_id = int(self.entry.get())
                    pass
                    # call another api
            self.entry.delete(0, 'end')

        btn = Button(self.frame, text='Enter SIP ID', command=confirm_SIP_ID)
        btn.pack(side=RIGHT, padx=5)
        self.entry.bind("<Return>", confirm_SIP_ID)
        self.entry.focus()






# def enter_failure_msg(self):
#     pass


# prog_gui = Gui()
prog_gui = enter_SIP_ID()
prog_gui.set_sip_id()

prog_gui.window.mainloop()