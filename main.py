from tkinter import *
import os
from PIL import Image, ImageTk

# Создание главного окна
main = Tk()
main.title("mycraft")
main.geometry("300x300") # размер

#reg
def sign_up():
    sign_up_screen = Toplevel(main)
    sign_up_screen.title("РЕГИСТРАЦИЯ!")
    sign_up_screen.geometry("200x200")

    #Labels
    Label(sign_up_screen, text="Введите логин и пароль").grid(row=0, sticky=N, pady=10) #row  строка
    Label(sign_up_screen, text="Как тебя звать?").grid(row=1, sticky=W) #row  строка
    Label(sign_up_screen, text="А какой пароль?").grid(row=2, sticky=W) #row  строка


#картинка
img = Image.open("data/images/mycraft.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

# Lablez
Label(main, text="САМАЯ КРУТАЯ ИГРА MYCRAFT").pack(side=TOP)
Label(main, image=img).pack(side=TOP)

# Buttons
Button(main, text="РЕГИСТРАЦИЯ", font=("Calibri", 12),width=15 ,command=sign_up).pack(side=TOP, pady=10)
Button(main, text="ВОЙТИ", font=("Calibri", 12),width=15).pack(side=TOP, pady=10)




mainloop()