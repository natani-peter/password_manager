import customtkinter as ctk
from settings import *


class EntryWidget(ctk.CTkEntry):
    def __init__(self, parent, holder):
        super(EntryWidget, self).__init__(parent, border_color='#fff', text_color='#115', placeholder_text=holder,
                                          placeholder_text_color='black', fg_color='#ddd', height=35,
                                          font=('sans-serif', 14))


class ButtonWidget(ctk.CTkButton):
    def __init__(self, parent, function, text):
        super(ButtonWidget, self).__init__(parent, height=40, corner_radius=20, fg_color=blue, command=function,
                                           text_color='black', text=text, hover_color='#45f')


class RadioButton(ctk.CTkRadioButton):
    def __init__(self, parent, text, var, value):
        super(RadioButton, self).__init__(
            parent, text=text, variable=var, value=value, font=font,text_color='black',width=10)
