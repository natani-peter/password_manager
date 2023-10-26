import customtkinter as ctk
from settings import *
from widgets import EntryWidget, ButtonWidget
import sqlite3


class AddPassword(ctk.CTkToplevel):
    def __init__(self, user_email):
        super(AddPassword, self).__init__(fg_color=blue)
        self.geometry('400x400+400+100')
        self.title('Add Password')
        self.attributes('-topmost', 1)
        with sqlite3.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select user_id from users where email=?', (user_email,))
            self.user_id = cursor.fetchall()[0][0]
        self.master_ = ctk.CTkFrame(self, fg_color='#fff')
        self.master_.pack(fill='both', padx=30, pady=15, expand=True)
        ctk.CTkLabel(self.master_, text_color='black', text='Add Password For...', font=font).pack(fill='x', pady=30)
        self.app = EntryWidget(self.master_, 'App, Username Or Website')
        self.app.pack(fill='x', padx=15, pady=30)
        self.password = EntryWidget(self.master_, "Password")
        self.password.pack(fill='x', pady=20, padx=15)
        self.add = ButtonWidget(self.master_, self.add_password, "Add The Password")
        self.add.configure(font=('sans-serif', 18))
        self.add.pack(fill='x', padx=30, pady=30)

    def add_password(self):
        app = self.app.get()
        password = self.password.get()

        with sqlite3.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('insert into passwords (app,password,user_id) values (?,?,?)', (app, password, self.user_id))
            database.commit()
            self.destroy()
