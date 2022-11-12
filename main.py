from tkinter import *
import os
from PIL import Image, ImageTk

# Создание главного окна
main = Tk()
main.title("mycraft")
main.geometry("300x300") # размер

class CoolAccount:
    def __init__(self, login, password, diamonds=0):
        self.login = login
        self.password = password
        self.diamonds = diamonds
        self.create_user()

    def create_user(self):
        if self.login == "" or self.password =="":
            notif.config(text="Необходимо заполнить все поля", fg="red")



def create_account():
    login = s_up_login.get()
    password = s_up_password.get()
    CoolAccount(login, password)


#reg
def sign_up():
    global s_up_login
    global s_up_password
    global notif
    s_up_login = StringVar()
    s_up_password = StringVar()

    sign_up_screen = Toplevel(main)
    sign_up_screen.title("РЕГИСТРАЦИЯ!")
    sign_up_screen.geometry("400x200")

    #Labels
    Label(sign_up_screen, text="Введите логин и пароль").grid(row=0, sticky=N, pady=10) #row  строка
    Label(sign_up_screen, text="Как тебя звать?").grid(row=1, sticky=W) #row  строка
    Label(sign_up_screen, text="А какой пароль?").grid(row=2, sticky=W) #row  строка
    notif = Label(sign_up_screen, font=("Calibri", 12))
    notif.grid(row=4, sticky=N, pady=10)
    # Entries
    Entry(sign_up_screen, textvariable=s_up_login).grid(row=1, column=1)
    Entry(sign_up_screen, textvariable=s_up_password).grid(row=2, column=1)

    # Buttons
    Button(sign_up_screen, text="РЕГИСТРАЦИЯ", font=("Calibri", 12), width=15, command=create_account).grid(row=3)


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