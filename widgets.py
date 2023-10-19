import customtkinter as ctk


class GeneralButton(ctk.CTkButton):
    def __init__(self, parent, name, func, fg_color='blue', corner=5, wid=50):
        super(GeneralButton, self).__init__(master=parent, text=name, command=func, fg_color=fg_color,
                                            corner_radius=corner, width=wid)
