import tkinter
import string
import secrets
from tkinter import messagebox as mb
import json

PASSWORD =  list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.minsize(width=600,height=500)
        self.img = tkinter.PhotoImage(file="MyPass.png")

        self.build_canvas()
        self.build_labels()
        self.build_entries()

    def build_canvas(self):
        self.canvas = tkinter.Canvas(self,width=600,height=300)
        self.canvas.create_image(300,150,image=self.img)
        self.canvas.pack()

    def build_labels(self):
        self.label1 = tkinter.Label(self,text="Website:", font=("Ariel",12,"bold"))
        self.label1.place(x=130,y=300)

        self.label2 = tkinter.Label(self,text="Email/Username:", font=("Ariel",12,"bold"))
        self.label2.place(x=100,y=350)

        self.label3 = tkinter.Label(self, text="Password:", font=("Ariel", 12, "bold"))
        self.label3.place(x=130, y=400)

    def build_entries(self):
        self.entry1 = tkinter.Entry(self,width=30)
        self.entry1.place(x=250,y=300)
        self.entry1.focus()

        self.entry2 = tkinter.Entry(self, width=45)
        self.entry2.place(x=250, y=350)

        self.entry3 = tkinter.Entry(self, width=25,show="*")
        self.entry3.place(x=250, y=400)

    def build_buttons(self,logic):
        self.button1 = tkinter.Button(self,text="Generate Password",command=logic.generate_pass)
        self.button1.place(x=420,y=395)

        self.button2 = tkinter.Button(self,text="Add",width=40, command=logic.add)
        self.button2.place(x=245,y = 435)

        self.button3 = tkinter.Button(self, text="Search",width=11, command=logic.search)
        self.button3.place(x=440 ,y=295)

    def show_error(self,text):
        mb.showerror(title="Oops",message=text)

    def show_user_pass(self,username,password):
        mb.showinfo(title=f"{self.entry1.get()}",message=f"Email: {username}\nPassword: {password}")

    def dialog_answer(self) -> bool|None:
        if mb.askyesno(title=f"{self.entry1.get()}",message=f"These are the details entered:\nEmail: {self.entry2.get()}\nPassword: {self.entry3.get()}\nIs it okay to save?"):

            return True
        else:
            mb.showinfo("Cancel","File creation is cancelled")

class Logic:
    def __init__(self,password_app):
        self.password_manager = password_app

    def add(self):
        if self.check_entries():
            website = self.password_manager.entry1.get()
            user = self.password_manager.entry2.get()
            password = self.password_manager.entry3.get()
            new_data = {
                website: {
                    "email/user": user,
                    "password": password,
                }
            }

            if self.password_manager.dialog_answer():
                self.password_manager.entry3.delete(0, tkinter.END)
                self.password_manager.entry1.delete(0, tkinter.END)
                try:
                    with open("C:\\Users\\savac\\OneDrive\\Masaüstü\\data.json", "r") as f:
                        data = json.load(f)
                except FileNotFoundError:
                    data = {}

                data.update(new_data)

                try:
                    with open("C:\\Users\\savac\\OneDrive\\Masaüstü\\data.json", "w") as f:
                        json.dump(data, f, indent=4)
                except FileNotFoundError:
                    print("Given path could not be found!")
                else:
                    print("Success")
        else:
            self.password_manager.show_error("Please don't leave the required entry/entries empty!")

    def search(self):
        if self.check_first_entry():
            try:
                with open("C:\\Users\\savac\\OneDrive\\Masaüstü\\data.json", "r") as f:
                    data = json.load(f)
                    website = self.password_manager.entry1.get()
                    if website in data:
                        self.password_manager.show_user_pass(data[website]["email/user"],data[website]["password"])
                    else:
                        self.password_manager.show_user_pass("NAN","NAN")
            except FileNotFoundError:
                self.password_manager.show_error("You have to add before searching/Check the file path")
            else:
                print("Success")

    def check_first_entry(self) -> bool:
        return bool(self.password_manager.entry1.get())

    def check_entries(self) -> bool:
        return bool(self.password_manager.entry1.get() and self.password_manager.entry2.get() and self.password_manager.entry3.get())

    def generate_pass(self):
        self.password_manager.entry3.delete(0,tkinter.END)
        password = "".join(secrets.choice(PASSWORD) for _ in range(20))
        self.password_manager.entry3.insert(0,password)
