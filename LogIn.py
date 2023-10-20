import customtkinter as ctk
from widgets import EntryWidget, ButtonWidget
from dashboard import Dashboard
from settings import *


class LogIn(ctk.CTkFrame):
    def __init__(self, parent, func):
        super(LogIn, self).__init__(parent, fg_color='#efc')
        self.parent = parent
        ctk.CTkLabel(self, text='LOG INTO YOUR ACCOUNT', text_color='#000', font=('sans-serif', 20, 'bold')) \
            .pack(pady=40)

        self.email = EntryWidget(self, 'Enter Your Email')
        self.email.pack(padx=30, fill='x', pady=5)

        self.password = EntryWidget(self, 'Enter Your Password')
        self.password.configure(show='*')
        self.password.pack(padx=30, fill='x', pady=30)

        self.login_button = ButtonWidget(self, self.login, 'LOG IN')
        self.login_button.pack(padx=30, fill='x', pady=0)

        self.forgot_password = ButtonWidget(self, self.password_edit, 'Forgot Password ?')
        self.forgot_password.pack(pady=30)

        self.forgot_password.configure(fg_color='#efc', hover_color='#efc', text_color=blue, height=0)

        ctk.CTkLabel(self, text='Have no account?', text_color='#000').place(x=200, y=370, anchor='ne')
        self.register_button = ButtonWidget(self, func, 'Register')
        self.register_button.place(x=200, y=375, anchor='nw')

        self.register_button.configure(fg_color='#efc', hover_color='#efc', text_color=blue, height=0, width=0)

    def login(self):
        self.pack_forget()
        Dashboard(self.parent).pack(expand=True,fill='both',padx=10,pady=10)

    def password_edit(self):
        pass
