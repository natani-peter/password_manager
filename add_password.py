import customtkinter as ctk
from settings import *
from widgets import EntryWidget, ButtonWidget


class AddPassword(ctk.CTkToplevel):
    def __init__(self):
        super(AddPassword, self).__init__(fg_color=blue)
        self.geometry('400x400+400+100')
        self.title('Add Password')
        self.attributes('-topmost', 1)
        self.master_ = ctk.CTkFrame(self, fg_color='#fff')
        self.master_.pack(fill='both', padx=30, pady=15, expand=True)
        ctk.CTkLabel(self.master_, text_color='black', text='Add Password For...', font=font).pack(fill='x', pady=30)
        self.app = EntryWidget(self.master_, 'App, Username Or Website')
        self.app.pack(fill='x', padx=15, pady=30)
        self.password = EntryWidget(self.master_, "Password")
        self.password.pack(fill='x', pady=20,padx=15)
        self.add = ButtonWidget(self.master_, '', "Add The Password")
        self.add.configure(font=('sans-serif', 18))
        self.add.pack(fill='x', padx=30,pady=30)
