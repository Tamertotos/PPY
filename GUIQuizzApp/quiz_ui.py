import tkinter

FONT = ("Courier",20,"bold")

class UI(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("quiz")
        self.minsize(450,600)
        self.configure(background="blue")
        self.build_labels()

    def build_labels(self):
        self.label1 = tkinter.Label(self,text= "", font=FONT, width=22, height=10)
        self.label1.place(x=50,y=100)

