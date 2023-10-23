import customtkinter as ctk
import tkinter as tk
import string as alphabet
from settings import *
from random import choice
from widgets import EntryWidget, RadioButton, ButtonWidget

characters = list(alphabet.printable[0:93])


def generate_password(length):
    password = ''
    for i in range(30):
        password += choice(characters)

    return password[0:length]


class Generator(ctk.CTkToplevel):
    def __init__(self):
        super(Generator, self).__init__(fg_color=blue)
        self.geometry('400x450+1100+200')
        self.title('GENERATE A PASSWORD')
        self.attributes('-topmost', 1)
        self.radio_value = tk.IntVar(value=8)
        self.master_frame = ctk.CTkFrame(self, fg_color='#fff')
        self.master_frame.pack(fill='both', expand=True, padx=20, pady=10)

        ctk.CTkLabel(self.master_frame, text='Generate A Password For...', text_color='black', font=font) \
            .pack(fill='x', padx=5, pady=30)
        self.website = EntryWidget(self.master_frame, 'Username, Website or App')
        self.website.pack(fill='x', padx=20, pady=15)
        ctk.CTkLabel(self.master_frame, text_color='black', text='Of Length...', font=font) \
            .pack(fill='x', padx=5, pady=30)

        self.radios = ctk.CTkFrame(self.master_frame, fg_color='#fff')
        self.radios.pack(fill='x', pady=30, padx=30)

        len8 = RadioButton(self.radios, '8', self.radio_value, 8)
        len8.pack(side='left', padx=15)
        len12 = RadioButton(self.radios, '12', self.radio_value, 12)
        len12.pack(side='left', padx=15)
        len16 = RadioButton(self.radios, '16', self.radio_value, 16)
        len16.pack(side='left', padx=15)
        len20 = RadioButton(self.radios, '20', self.radio_value, 20)
        len20.pack(side='left', padx=10)

        self.generate = ButtonWidget(self.master_frame, self.radio, 'Generate Password')
        self.generate.configure(font=('sans-serif', 18))
        self.generate.pack(fill='x', padx=20, pady=25)

    def radio(self):
        print(self.radio_value.get())
