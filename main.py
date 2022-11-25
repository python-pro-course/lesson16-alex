from tkinter import *
import os
from PIL import Image, ImageTk

from sign_up_window import SignUpWindow
from log_in_window import LogInWindow

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("mycraft")
        self.geometry("300x300-800+300")  # размеp
        img = Image.open("data/images/mycraft.png")
        img = img.resize((150, 150))
        self.img = ImageTk.PhotoImage(img)

        # Lablez
        Label(self, text="САМАЯ КРУТАЯ ИГРА MYCRAFT").pack(side=TOP)
        Label(self, image=self.img).pack(side=TOP)

        # Buttons
        Button(self, text="РЕГИСТРАЦИЯ", font=("Calibri", 12), width=15,command=self.sign_up_window).pack(side=TOP, pady=10)
        Button(self, text="ВОЙТИ", font=("Calibri", 12), width=15 ,command=self.log_in_window).pack(side=TOP, pady=10)


    def sign_up_window(self):
        SignUpWindow(self)

    def log_in_window(self):
        LogInWindow(self)



app = App()
app.mainloop()