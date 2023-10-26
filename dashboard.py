import tkinter
import customtkinter as ctk
from widgets import EntryWidget, ButtonWidget
from generate_password import Generator
from add_password import AddPassword
import sqlite3


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent, user_email):
        super(Dashboard, self).__init__(parent, fg_color='#fff', corner_radius=20)
        parent.geometry('700x450')
        self.email = user_email

        with sqlite3.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select user_name from users where email=?', (self.email,))
            username = cursor.fetchall()[0][0]

        with sqlite3.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select user_id from users where email=?', (self.email,))
            user_id = cursor.fetchall()[0][0]
        self.generate = lambda: Generator(self.email)
        self.add = lambda: AddPassword(self.email)
        UserInfo(self, self.generate, self.add, username, user_id).pack(fill='both', expand=True)


class UserInfo(ctk.CTkFrame):
    def __init__(self, parent, func1, func2, user, user_id):
        super(UserInfo, self).__init__(parent, fg_color='#fff', corner_radius=0)
        self.user = user
        self.parent = parent
        self.record = None
        self.user_id = user_id

        self.up_part = ctk.CTkFrame(self, height=80, fg_color='#fff')
        self.up_part.pack(fill='x', padx=20, pady=10)

        self.info = ctk.CTkFrame(self.up_part, fg_color='#eee')
        self.info.pack(side='left', padx=10, pady=10, expand=True, fill='x')
        ctk.CTkLabel(self.info, text=f'WELCOME, {self.user.upper()}', text_color='black',
                     font=('sans-serif', 20, 'bold')).pack(fill='x', pady=10, padx=20)

        self.search = EntryWidget(self.info, 'Search Your Passwords')
        self.search.pack(side='left', fill='x', pady=10, expand=True, padx=10)
        self.search.bind('<KeyRelease>', self.search_passwords)

        self.buttons = ctk.CTkFrame(self.up_part, fg_color='#fff')
        self.buttons.pack(side='left', padx=10, pady=10)

        self.create = ButtonWidget(self.buttons, func1, "GENERATE A PASSWORD")
        self.create.pack(side='top', expand=True, fill='x', padx=3, pady=10)
        self.create.configure(fg_color='#eee', hover_color='#ccc')

        self.add = ButtonWidget(self.buttons, func2, 'ADD NEW PASSWORD')
        self.add.pack(side='bottom', expand=True, fill='both', padx=3, pady=5)
        self.add.configure(fg_color='#eee', hover_color='#ccc')

        self.password_frame = ctk.CTkFrame(self, fg_color='#ccc')
        self.password_frame.pack(fill='both', padx=20, pady=10, expand=True)
        self.show_passwords(self.password_frame)

    def show_passwords(self, parent):
        query = ''
        with sqlite3.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select app, password from passwords where user_id = ? and app like ?',
                           (self.user_id, '%' + query + '%'))
            results = cursor.fetchall()
        if results:
            rows = len(results)
            columns = len(results[0])
            for row in range(rows):
                for column in range(columns):
                    self.record = EntryWidget(self.password_frame)
                    self.record.configure(width=300)
                    self.record.grid(row=row, column=column, padx=10, pady=5)
                    self.record.insert(tkinter.END, results[row][column])
                    self.record.configure(state='readonly')
        else:
            ctk.CTkLabel(parent, text_color='black', font=('sans-serif', 20, 'bold'), text='You Have No Passwords') \
                .pack(expand=True, fill='both', padx=5, pady=5)

    def search_passwords(self, event):
        query = self.search.get()
        with sqlite3.connect('password_manager.db') as database:
            cursor = database.cursor()
            cursor.execute('select app, password from passwords where user_id = ? and app like ?',
                           (self.user_id, '%' + query + '%'))
            results = cursor.fetchall()
        if results:
            rows = len(results)
            columns = len(results[0])
            for child in self.password_frame.winfo_children():
                child.destroy()
            for row in range(rows):
                for column in range(columns):
                    self.record = EntryWidget(self.password_frame)
                    self.record.configure(width=300)
                    self.record.grid(row=row, column=column, padx=10, pady=5)
                    self.record.insert(tkinter.END, results[row][column])
                    self.record.configure(state='readonly')
        else:
            for child in self.password_frame.winfo_children():
                child.destroy()
            ctk.CTkLabel(self.password_frame, text_color='black', font=('sans-serif', 20, 'bold'), text='No Results') \
                .pack(expand=True, fill='both', padx=5, pady=5)
