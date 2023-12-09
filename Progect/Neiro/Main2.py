from googletrans import Translator
from customtkinter import *
import customtkinter

customtkinter.set_default_color_theme("dark-blue") 

class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Переводчик")  
        main_frame = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row=0, column=0, padx=10, pady=60) 
app = App()
app.resizable(width=False, height=False)
app.geometry("250x230")
app.mainloop()