import customtkinter as ctk
from widgets import EntryWidget, ButtonWidget
from dashboard import Dashboard
from settings import *
import bcrypt
import sqlite3 as lite
from tkinter import messagebox as box
import re


class LogIn(ctk.CTkFrame):
    def __init__(self, parent, func):
        super(LogIn, self).__init__(parent, fg_color='#efc')
        self.confirm = None
        self.confirm_password = None
        self.password2 = None
        self.frame2 = None
        self.frame1 = None
        self.email1 = None
        self.secret = None
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
        # current_user
        # email = self.email.get()
        # password = self.password.get()
        email = 'natanipeter@gmail.com'
        password = '@Natan1.'
        with lite.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select email from users where email=?', (email,))
            user = cursor.fetchall()

        if user:
            with lite.connect('password_manager.db') as database:
                cursor = database.cursor()
                cursor.execute('select user_password from users where email=?', (email,))
                hashed = cursor.fetchone()[0]
            check_password = bcrypt.checkpw(password.encode(), hashed)
            if check_password:
                self.pack_forget()
                Dashboard(self.parent, email).pack(expand=True, fill='both', padx=10, pady=10)
            else:
                box.showerror('ERROR', 'Invalid Password')
        else:
            box.showinfo('INFO', 'Invalid Email\nUser with that email does not exist')

    def password_edit(self):
        self.pack_forget()
        self.frame1 = ctk.CTkFrame(self.parent, fg_color='#fff')
        self.frame1.pack(expand=True, fill='both', padx=25, pady=10)

        self.email1 = EntryWidget(self.frame1, 'Enter Your Email')
        self.email1.pack(padx=30, fill='x', pady=90)

        self.secret = EntryWidget(self.frame1, 'Enter Your Secret Number')
        self.secret.pack(fill='x', padx=30)

        continue_ = ButtonWidget(self.frame1, self.go_on, 'Continue')
        continue_.configure(width=50)
        continue_.place(relx=0.5, rely=0.77, anchor='center')

    def go_on(self):
        email = self.email1.get()
        secret = self.secret.get()

        with lite.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select secret_number from users where email=?', (email,))
            try:
                user_secret = cursor.fetchall()[0][0]
            except IndexError:
                box.showinfo('INFO', 'Check Your Email')

        if str(user_secret) == secret:
            self.frame1.pack_forget()
            self.frame2 = ctk.CTkFrame(self.parent, fg_color='#fff')
            self.frame2.pack(expand=True, fill='both', padx=25, pady=100)

            self.password2 = EntryWidget(self.frame2, 'New Password')
            self.password2.configure(show='*')
            self.password2.pack(padx=30, fill='x', pady=30)

            self.confirm_password = EntryWidget(self.frame2, 'Confirm New Your Password')
            self.confirm_password.configure(show='*')
            self.confirm_password.pack(padx=30, fill='x', pady=5)

            self.confirm = ButtonWidget(self.frame2, lambda: self.update_(email), 'CHANGE PASSWORD')
            self.confirm.pack(padx=40, fill='x', pady=30)
        else:
            box.showerror('ERROR', 'Invalid Secret Number')

    def update_(self, email):
        user_password = self.password2.get()
        user_password2 = self.confirm_password.get()
        with lite.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select user_password from users where email=?', (email,))
            hashed = cursor.fetchone()[0]
        check_password = bcrypt.checkpw(user_password.encode(), hashed)

        if check_password:
            box.showerror('ERROR', 'New password cant be the same as old')
        else:
            if user_password == user_password2:
                pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[.,!@#%&?=])[\w.,!@#%&?=]{8,}$'
                gateposts = re.match(pattern, user_password)
                if gateposts:
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(user_password.encode(), salt)
                    with lite.connect('password_manager.db') as database:
                        cursor = database.cursor()
                        cursor.execute('update users set user_password = ? where email = ?',
                                       (hashed_password, email,))
                        box.showinfo('SUCCESS', 'Password Changed Successfully')
                        Dashboard(self.parent).pack(expand=True, fill='both', padx=10, pady=10)
                else:
                    box.showinfo('INFO', 'Password Is too Weak\n To Protect Your Passwords')
            else:
                box.showerror('ERROR', 'Please Confirm Your Password')
