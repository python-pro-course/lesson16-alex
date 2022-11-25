from tkinter import *
from PIL import Image, ImageTk

class UpdadeBalance(Toplevel):
    def __init__(self, parent, user_name, user_login, user_password, user_diamonds):
        super().__init__(parent)
        self.parent = parent
        self.title("Please deposit 5 diamonds!")
        self.geometry("300x500-800+300")
        self.name = user_name
        self.login = user_login
        self.password = user_password
        self.diamonds = int(user_diamonds)
        self.amount = IntVar()
        img = Image.open("data/images/pickage.PNG").resize((170, 170))
        self.img = ImageTk.PhotoImage(img)

        Label(self, text=f"Текущий баланс: {self.diamonds}", font=("Calibri", 13)).pack(side=TOP, pady=10)
        Label(self, image=self.img).pack(side=TOP)

        Entry(self, textvariable=self.amount).pack(side=TOP)
        Button(self, text="Внести", font=("Calibri", 12), width=15, command=self.deposit).pack(side=TOP, pady=10)

        Entry(self, textvariable=self.amount).pack(side=TOP)
        Button(self, text="Снять", font=("Calibri", 12), width=15, command=self.withdraw).pack(side=TOP, pady=10)

    def deposit(self):
        amount = self.amount.get()
        self.amount.set(0)
        self.diamonds += amount

        with open(self.login, 'w') as f:
            f.write(f'{self.name}\n'
                    f'{self.login}\n'
                    f'{self.password}\n'
                    f'{self.diamonds}')

    def withdraw(self):
        amount = self.amount.get()
        self.amount.set(0)
        if self.diamonds >= amount:
            self.diamonds -= amount
        else:
            Label(self,fg="red", text=f"Не хватает средств", font=("Calibri", 13)).pack(side=TOP, pady=10)

        with open(self.login, 'w') as f:
            f.write(f'{self.name}\n'
                f'{self.login}\n'
                f'{self.password}\n'
                f'{self.diamonds}')
