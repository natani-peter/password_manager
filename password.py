import customtkinter as ctk
from login import LogIn
from register import Register

from settings import *


class Password(ctk.CTk):
    def __init__(self):
        super(Password, self).__init__(fg_color=blue)
        self.geometry('400x450+600+200')
        self.resizable(False, False)

        self.title('')
        self.login = LogIn(self, self.bring_register)
        self.login.pack(expand=True, fill='both', padx=25, pady=10)
        self.register = Register(self, self.bring_login)
        self.mainloop()

    def bring_register(self):
        self.login.pack_forget()
        self.register.pack(expand=True, fill='both', padx=25, pady=10)

    def bring_login(self):
        self.register.pack_forget()
        self.login.pack(expand=True, fill='both', padx=25, pady=10)


Password()
