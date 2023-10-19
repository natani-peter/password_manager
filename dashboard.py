import sqlite3
import customtkinter as ctk
import tkinter as tk
from settings import *

global rows__, columns__
global rows_, columns_


class MiddleFrame(ctk.CTkToplevel):
    def __init__(self, parent, user):
        global rows__, columns__
        super(MiddleFrame, self).__init__(master=parent)
        connection = sqlite3.connect('password_manager.db')
        self.cursor = connection.cursor()
        self.c1 = self.cursor.execute("select user_id from users where username = ?", (user,))

        self.query = None
        self.title('YOUR PASSWORDS')
        self.geometry('500x450')
        self.resizable(False, False)

        self.parent_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#555")
        self.parent_frame.pack(expand=True, fill='both')

        self.buttons = ctk.CTkFrame(self.parent_frame, corner_radius=10)
        self.buttons.columnconfigure(dash_columns, weight=1, uniform='a')
        self.buttons.rowconfigure(dash_rows, weight=1, uniform='a')
        self.buttons.pack(fill='x', padx=5, pady=5)

        self.passwords_frame = ctk.CTkFrame(self.parent_frame, corner_radius=10)
        self.passwords_frame.pack(expand=True, fill='both', padx=5, pady=5, ipadx=5)

        self.canvas = ctk.CTkCanvas(self.passwords_frame,background='blue')

        self.frame = ctk.CTkFrame(self.passwords_frame, corner_radius=0)

        self.scroll_frame = ctk.CTkFrame(self.passwords_frame, corner_radius=10, width=10)

        self.scroll_bar = ctk.CTkScrollbar(self.scroll_frame, width=20, height=self.scroll_frame.winfo_height(),
                                           command=self.canvas.yview)

        ctk.CTkLabel(self.buttons, text=f" WELCOME, {user.upper()}", text_color='blue', font=('Calibri', 20)) \
            .grid(column=0, row=1, columnspan=7, sticky='news')

        self.search = ctk.CTkEntry(self.buttons, placeholder_text='Search Passwords...')
        self.search.grid(column=2, row=3, sticky='news', columnspan=3)

        if self.c1:
            results = self.c1.fetchone()
            self.user_id = results[0]
        else:
            for child in self.frame.winfo_children():
                child.destroy()

            ctk.CTkLabel(self.frame, text='No Passwords').pack(expand=True, fill='both')

        connection = sqlite3.connect('password_manager.db')
        self.cursor = connection.cursor()
        self.cursor.execute('select app,password from passwords where user_id = ?', (self.user_id,))
        words = self.cursor.fetchall()

        if words:
            columns__ = len(words[0])
            rows__ = len(words)
        else:
            for child in self.frame.winfo_children():
                child.destroy()

            ctk.CTkLabel(self.frame, text='No Passwords').pack(expand=True, fill='both')
        try:
            for row in range(rows__):
                for column in range(columns__):
                    self.entry = ctk.CTkEntry(self.frame, width=200, fg_color='gray',
                                              font=('Arial', 16, 'bold'), text_color='red')
                    self.entry.grid(column=column, row=row, sticky='news', padx=10, pady=2)
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, words[row][column])
            self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        except:
            for child in self.frame.winfo_children():
                child.destroy()

            ctk.CTkLabel(self.frame, text='No Passwords').pack(expand=True, fill='both')
        self.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scroll_bar.set)
        self.canvas.pack(expand=True, fill='both', padx=5, pady=5, ipadx=5)
        self.scroll_frame.pack(side='left', fill='y', pady=3)
        self.scroll_bar.pack(fill='y')
        self.bind('<KeyRelease>', self.update_window)
        # self.bind_all("<MouseWheel>", lambda event: self.yview_scroll(-int(event.delta / 60), 'units'))

        self.mainloop()
        connection.close()

    def update_window(self, event):
        global rows_, columns_
        try:
            search_term = self.search.get()
            command = "select app,password from passwords where app like ? and user_id = ?;"
            self.query = self.cursor.execute(command, ('%' + search_term + '%', self.user_id))
            words = self.query.fetchall()
            if words:
                columns_ = len(words[0])
                rows_ = len(words)
            else:
                for child in self.frame.winfo_children():
                    child.grid_forget()
                    child.destroy()
                ctk.CTkLabel(self.frame, text='No results').pack(expand=True, fill='both')

            for child in self.frame.winfo_children():
                child.destroy()
            try:
                for row in range(rows_):
                    for column in range(columns_):
                        self.entry = ctk.CTkEntry(self.frame, width=200, fg_color='gray',
                                                  font=('Arial', 16, 'bold'), text_color='red')
                        self.entry.grid(column=column, row=row, sticky='ew', padx=10, pady=2)
                        self.entry.delete(0, tk.END)
                        self.entry.insert(tk.END, words[row][column])
            except:
                for child in self.frame.winfo_children():
                    child.grid_forget()
                    child.destroy()
                ctk.CTkLabel(self.frame, text='No results').pack(expand=True, fill='both')
        except UnboundLocalError:
            ctk.CTkLabel(self.frame, text='No results').pack(expand=True, fill='both')
            return event

    def close(self):
        self.destroy()
        # self.unbind_all('<MouseWheel>')
