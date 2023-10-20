import customtkinter as ctk
from widgets import EntryWidget, ButtonWidget
from generate_password import Generator
from add_password import AddPassword


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent):
        super(Dashboard, self).__init__(parent, fg_color='#fff', corner_radius=20)
        parent.geometry('700x450')
        self.generate = Generator
        self.add = AddPassword
        UserInfo(self, self.generate,self.add).pack(fill='x', padx=20, pady=10)
        UserPasswords(self).pack(fill='both', padx=20, pady=10, expand=True)


class UserInfo(ctk.CTkFrame):
    def __init__(self, parent, func1, func2, user='peter'):
        super(UserInfo, self).__init__(parent, height=80, fg_color='#fff')
        self.user = user
        self.info = ctk.CTkFrame(self, fg_color='#eee')
        self.info.pack(side='left', padx=10, pady=10, expand=True, fill='x')
        ctk.CTkLabel(self.info, text=f'WELCOME, {self.user.upper()}', text_color='black',
                     font=('sans-serif', 20, 'bold')).pack(fill='x', pady=10, padx=20)
        self.search = EntryWidget(self.info, 'Search Your Passwords')
        self.search.pack(side='left', fill='x', pady=10, expand=True, padx=10)
        self.buttons = ctk.CTkFrame(self, fg_color='#fff')
        self.buttons.pack(side='left', padx=10, pady=10)

        self.create = ButtonWidget(self.buttons, func1, "GENERATE A PASSWORD")
        self.create.pack(side='top', expand=True, fill='x', padx=3, pady=10)
        self.create.configure(fg_color='#eee', hover_color='#ccc')

        self.add = ButtonWidget(self.buttons, func2, 'ADD NEW PASSWORD')
        self.add.pack(side='bottom', expand=True, fill='both', padx=3, pady=5)
        self.add.configure(fg_color='#eee', hover_color='#ccc')


class UserPasswords(ctk.CTkFrame):
    def __init__(self, parent):
        super(UserPasswords, self).__init__(parent, fg_color='#ccc')
        ctk.CTkLabel(self, text_color='black', font=('sans-serif', 20, 'bold'), text='You Have No Passwords') \
            .pack(expand=True, fill='both', padx=5, pady=5)
