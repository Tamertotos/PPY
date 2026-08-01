import tkinter


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro app")
        self.minsize(width=1000,height=1000)
        self.img = {
            "work" : tkinter.PhotoImage(file="pomodoro_timer.png")
        }


    def build_canvas(self):
        self.canvas = tkinter.Canvas(self, width=1001, height=1001, highlightthickness=0)
        self.canvas.create_image(500, 500, image=self.img["work"])
        self.canvas.pack()
        self.text = self.canvas.create_text(500,650,text="00:00",fill="white",font=("Arial",35,"bold"))

    def build_buttons(self,logic):
        self.button1 = tkinter.Button(self,text="START",command=logic.start)
        self.button1.pack()


    def set_timer(self):
        self.canvas.itemconfig(self.text,text="AAAA")

class Logic:
    def __init__(self,app):
        self.pomodoro = app

    def start(self):
        self.pomodoro.set_timer()
