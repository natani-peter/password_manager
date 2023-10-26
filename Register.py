import customtkinter as ctk
from widgets import EntryWidget, ButtonWidget
from settings import *
from dashboard import Dashboard
import sqlite3 as lite
import random as rand
from tkinter import messagebox as box
import re
import bcrypt


class Register(ctk.CTkFrame):
    def __init__(self, parent, func):
        super(Register, self).__init__(parent, fg_color='#efc')
        self.parent = parent
        ctk.CTkLabel(self, text='REGISTER YOUR ACCOUNT', text_color='#000', font=('sans-serif', 20, 'bold')) \
            .pack(pady=40)

        self.name = EntryWidget(self, 'Enter Your Username')
        self.name.pack(padx=30, fill='x', pady=5)

        self.email = EntryWidget(self, 'Enter Your Email')
        self.email.pack(padx=30, fill='x', pady=5)

        self.password = EntryWidget(self, 'Enter Your Password')
        self.password.configure(show='*')
        self.password.pack(padx=30, fill='x', pady=20)

        self.confirm_password = EntryWidget(self, 'Confirm Your Password')
        self.confirm_password.configure(show='*')
        self.confirm_password.pack(padx=30, fill='x', pady=0)

        self.register_button = ButtonWidget(self, self.enter, 'REGISTER')
        self.register_button.pack(padx=30, fill='x', pady=15)

        ctk.CTkLabel(self, text='Have account?', text_color='#000').place(x=200, y=380, anchor='ne')
        self.login_button = ButtonWidget(self, func, 'Log in')
        self.login_button.place(x=200, y=385, anchor='nw')

        self.login_button.configure(fg_color='#efc', hover_color='#efc', text_color=blue, height=0, width=0)

    def enter(self):
        # user data

        username = self.name.get()
        email = self.email.get()
        user_password = self.password.get()
        user_password2 = self.confirm_password.get()
        secret_number = rand.randint(1000, 9999)

        # validation
        if len(username) == 0 or len(email) == 0 or len(user_password) == 0 or len(user_password2) == 0:
            box.showerror('ERROR', 'All Fields Are Required')
        else:
            if len(username) >= 4:
                with lite.connect('password_manager.db') as database:
                    cursor = database.cursor()
                    cursor.execute('select user_name from users where user_name= ?', (username,))
                    user = cursor.fetchall()

                if user:
                    box.showinfo("INFO", 'Username Not Available')
                else:
                    with lite.connect('password_manager.db') as database:
                        cursor = database.cursor()
                        cursor.execute('select email from users where email=?', (email,))
                        user_email = cursor.fetchall()

                    if user_email:
                        box.showinfo('INFO', 'You are advised to use your email')
                    else:
                        if user_password == user_password2:
                            pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[.,!@#%&?=])[\w.,!@#%&?=]{8,}$'
                            gateposts = re.match(pattern, user_password)
                            if gateposts:
                                salt = bcrypt.gensalt()
                                hashed_password = bcrypt.hashpw(user_password.encode(), salt)
                                with lite.connect('password_manager.db') as database:
                                    cursor = database.cursor()
                                    cursor.execute('insert into users (user_name,email,user_password,secret_number) '
                                                   'values (?,?,?,?)',
                                                   (username, email, hashed_password, secret_number))
                                    database.commit()
                                    box.showinfo('SUCCESS', 'Account Created Successfully')
                                    box.showwarning('WARNING', f"\tYour Secret Number is {secret_number}\n"
                                                               f"Keep This number Safely and Dont Share it.")
                                    self.destroy()
                                    Dashboard(self.parent, email).pack(expand=True, fill='both', padx=10, pady=10)
                            else:
                                box.showinfo('INFO', 'Password Is too Weak\n To Protect Your Passwords')
                        else:
                            box.showerror('ERROR', 'Please Confirm Your Password')
            else:
                box.showinfo('INFO', 'The Username Is Too Short')
