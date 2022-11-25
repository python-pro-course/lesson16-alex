from tkinter import *
import os
from PIL import Image, ImageTk


from login_session import LoginSession
class LogInWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("ВХОД!")
        self.geometry("400x200")
        self.login = StringVar()
        self.password = StringVar()
        # Labels
        Label(self, text="Введите свой логин и пароль").grid(row=0, sticky=N, pady=10)  # row  строка
        Label(self, text="Логин").grid(row=1, sticky=W)  # row  строка
        Label(self, text="Пароль").grid(row=2, sticky=W)  # row  строка
        self.notif = Label(self, font=("Calibri", 12))
        self.notif.grid(row=4, sticky=N, pady=10)
        # Entries
        Entry(self, textvariable=self.login).grid(row=1, column=1)
        Entry(self, textvariable=self.password, show="*").grid(row=2, column=1)

        # Buttons
        Button(self, text="ВХОД", font=("Calibri", 12), width=15, command=self.log_in_account).grid(row=3)

    def get_details(self,user_login):
        with open(user_login, 'r') as f:
            file_list = f.read().split("\n")
            name = file_list[0]
            password = file_list[2]
        return name, password

    def log_in_account(self):
        all_accounts = os.listdir()
        user_login = self.login.get()
        user_password = self.password.get()

        for name in all_accounts:
            if name == user_login:
                name, file_password = self.get_details(user_login)
                if user_password == file_password:
                    self.destroy()
                    LoginSession(self.parent, name, user_login, user_password)
                    return
                else:
                    self.notif.config(fg="red", text="Пароль неправильный")
                    return
        self.notif.config(fg="red", text="Такого аккаунта нет")


