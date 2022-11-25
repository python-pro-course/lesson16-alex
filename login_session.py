from tkinter import *
import os

from update_balance_window import UpdadeBalance

class LoginSession(Toplevel):
    def __init__(self, parent,user_name,user_login,user_password):
        super().__init__(parent)
        self.parent = parent
        self.title("Алмазики!")
        self.geometry("300x300-800+300")
        self.parent = parent
        self.name = user_name
        self.login = user_login
        self.password = user_password
        self.diamonds = self.get_balance()

        Label(self, text=f"Здравствуйте, {self.name}", font=("Calibri", 13)).pack(side=TOP,pady=10)

        Label(self, text=f"Ваш баланс: {self.diamonds}", font=("Calibri", 13)).pack(side=TOP)

        Button(self, text="Deposit", font=("Calibri", 12), width=15, command=self.deposit).pack(side=TOP, pady=10)

    def get_balance(self):
        with open(self.login, 'r') as f:
            f = f.read().split('\n')
            balance = f[3]
        return balance

    def deposit(self):
        UpdadeBalance(self.parent, self.name, self.login, self.password, self.diamonds)


