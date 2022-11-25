from tkinter import *
import os
from PIL import Image, ImageTk

class SignUpWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sign Up")
        self.geometry("300x300-800+300")
        self.name = StringVar()
        self.login = StringVar()
        self.password = StringVar()
        #Labels
        Label(self, text="Введите логин и пароль").grid(row=0, sticky=N, pady=10) #row  строка
        Label(self, text="Имя").grid(row=1, sticky=W) #row  строка
        Label(self, text="Логин").grid(row=2, sticky=W)  # row  строка
        Label(self, text="Пароль").grid(row=3, sticky=W) #row  строка
        self.notif = Label(self, font=("Calibri", 12))
        self.notif.grid(row=4, sticky=N, pady=10)
        # Entries
        Entry(self, textvariable=self.name).grid(row=1, column=1)
        Entry(self, textvariable=self.login).grid(row=2, column=1)
        Entry(self, textvariable=self.password, show="*").grid(row=3, column=1)
        # Buttons
        Button(self, text="РЕГИСТРАЦИЯ", font=("Calibri", 12), width=15, command=self.create_account).grid(row=4)

    def create_account(self):
        name = self.name.get()
        login = self.login.get()
        password = self.password.get()

        if login == "" or password =="" or name == "":
            self.notif.config(text="Необходимо заполнить все поля", fg="red")
            return
        self.notif.config(text="", fg="red")
        all_accounts = os.listdir()
        for line in all_accounts:
            if line == login:
                self.notif.config(text="Такой аккаунт уже существует", fg="red")
                return
        self.notif.config(text="", fg="red")

        with open(login, "w") as f:
            f.write(f"{name}\n"
                    f"{login}\n"
                    f"{password}\n"
                    f" 0")
        self.notif.config(text="Аккаунт успешно создан", fg="green")