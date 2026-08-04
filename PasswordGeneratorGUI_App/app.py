import tkinter
import string
import secrets
from tkinter import messagebox as mb

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

        self.label3 = tkinter.Label(self, text="Password", font=("Ariel", 12, "bold"))
        self.label3.place(x=130, y=400)

    def build_entries(self):
        self.entry1 = tkinter.Entry(self,width=40)
        self.entry1.place(x=250,y=300)

        self.entry2 = tkinter.Entry(self, width=40)
        self.entry2.place(x=250, y=350)

        self.entry3 = tkinter.Entry(self, width=25,show="*")
        self.entry3.place(x=250, y=400)

    def build_buttons(self,logic):
        self.button1 = tkinter.Button(self,text="Generate Password",command=logic.generate_pass)
        self.button1.place(x=410,y=395)

        self.button2 = tkinter.Button(self,text="Add",width=40, command=logic.add)
        self.button2.place(x=245,y = 435)

    def show_error(self):
        mb.showerror("Ooops","Please don't leave any files empty!")

    def dialog_answer(self) -> bool:
        if mb.askyesno(f"{self.entry1.get()}",f"Email: {self.entry2.get()}\nPassword: {self.entry3.get()}\nIs this okay?"):
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

            if self.password_manager.dialog_answer():
                with open("C:\\Users\\savac\\OneDrive\\Masaüstü\\my_file.txt", "a") as f:
                    f.write(f"{website} | {user} | {password}\n")

        else:
            self.password_manager.show_error()


    def check_entries(self) -> bool:
        return bool(self.password_manager.entry1.get() and self.password_manager.entry2.get() and self.password_manager.entry3.get())

    def generate_pass(self):
        self.password_manager.entry3.delete(0,tkinter.END)
        password = "".join(secrets.choice(PASSWORD) for _ in range(20))
        self.password_manager.entry3.insert(0,password)
