import customtkinter as ctk
from widgets import EntryWidget, ButtonWidget
from settings import *


class Register(ctk.CTkFrame):
    def __init__(self, parent, func):
        super(Register, self).__init__(parent, fg_color='#efc')
        ctk.CTkLabel(self, text='REGISTER YOUR ACCOUNT', text_color='#000', font=('sans-serif', 20, 'bold')) \
            .pack(pady=40)

        self.email = EntryWidget(self, 'Enter Your Email')
        self.email.pack(padx=30, fill='x', pady=5)

        self.password = EntryWidget(self, 'Enter Your Password')
        self.password.configure(show='*')
        self.password.pack(padx=30, fill='x', pady=30)

        self.confirm_password = EntryWidget(self, 'Confirm Your Password')
        self.confirm_password.configure(show='*')
        self.confirm_password.pack(padx=30, fill='x', pady=0)

        self.register_button = ButtonWidget(self, self.enter, 'REGISTER')
        self.register_button.pack(padx=30, fill='x', pady=25)

        ctk.CTkLabel(self, text='Have account?', text_color='#000').place(x=200, y=370, anchor='ne')
        self.login_button = ButtonWidget(self, func, 'Log in')
        self.login_button.place(x=200, y=375, anchor='nw')

        self.login_button.configure(fg_color='#efc', hover_color='#efc', text_color=blue, height=0, width=0)

    def enter(self):
        pass

    def password_edit(self):
        pass
