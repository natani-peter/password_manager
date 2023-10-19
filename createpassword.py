import customtkinter as ctk
from settings import *
from tkinter import messagebox as box
import sqlite3
import bcrypt


connection = sqlite3.connect('password_manager.db')
cursor = connection.cursor()


class AddPassword(ctk.CTkToplevel):
    def __init__(self, user):
        super(AddPassword, self).__init__()
        self.title('ADD NEW PASSWORD')
        self.geometry('350x300')
        self.resizable(False, False)
        self.user = user
        c1 = cursor.execute("select user_id from users where username = ?", (self.user,))
        self.user_id = c1.fetchone()[0]

        # layout
        self.columnconfigure(create_columns, weight=1, uniform='a')
        self.rowconfigure(create_rows, weight=1, uniform='a')

        # widgets
        self.app = ctk.CTkEntry(self, placeholder_text='App name or Website or Username')
        self.app.grid(column=1, row=1, columnspan=5, sticky='ew')
        self.password = ctk.CTkEntry(self, placeholder_text="Password For the above")
        self.password.grid(column=1, row=3, columnspan=5, sticky='ew')
        self.add = ctk.CTkButton(self, text='ADD THE PASSWORD', command=self.create)
        self.add.grid(column=2, row=5, columnspan=3, sticky='we')

    def create(self):
        app = self.app.get()
        password = self.password.get()
        if (len(app) and len(password)) > 1:
            cursor.execute("insert into passwords (app,password,user_id) values (?,?,?)",
                                (app, password, self.user_id))
            connection.commit()
            self.destroy()
        else:
            box.showerror('ERROR', 'Too short')
