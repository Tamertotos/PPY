import tkinter
import time


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro app")
        self.minsize(width=1000, height=1000)
        self.img = {
            "work": tkinter.PhotoImage(file="pomodoro_timer.png")
        }

        self.build_canvas()
        self.build_labels()

    def build_canvas(self):
        self.canvas = tkinter.Canvas(self, width=1001, height=1001, highlightthickness=0)
        self.canvas.create_image(500, 500, image=self.img["work"])
        self.canvas.pack()
        self.text = self.canvas.create_text(500, 650, text="25:00", fill="white", font=("Arial", 35, "bold"))

    def build_buttons(self, logic):
        self.button1 = tkinter.Button(self, text="START", command=logic.start, width=10, bg="Pink")
        self.button1.place(x=300, y=900)

        self.button2 = tkinter.Button(self, text="RESET", command=logic.reset, width=10, bg="Pink")
        self.button2.place(x=600, y=900)

    def build_labels(self):
        self.label1 = tkinter.Label(self, text="WORK TIME", fg="Green", bg="Pink", font=("Arial", 35, "bold"), width=10)
        self.label1.place(x=370, y=25)

        self.label2 = tkinter.Label(self, text='\N{check mark}', fg="Green", bg="Pink", font=("Arial", 20, "bold"))
        self.label2.place(x=440, y=900)

    def set_timer(self, text):
        self.canvas.itemconfig(self.text, text=text)

    def set_label(self, text):
        self.label1.config(text=text)


class Logic:
    def __init__(self, app):
        self.pomodoro = app
        self.text = '\N{check mark}'
        self.minute: int = 00
        self.seconds: int = 7
        self.state = "work"

    def reset(self):
        self.minute = 25
        self.seconds = 00
        # self.pomodoro.label2.config(text=self.text)
        self.pomodoro.set_timer(f"{self.minute:02d}:{self.seconds:02d}")

    def start(self):
        def counter():
            self.pomodoro.set_timer(f"{self.minute:02d}:{self.seconds:02d}")

            if self.minute == 0 and self.seconds == 0:
                if self.state == "work":
                    self.minute, self.seconds = 5, 0
                    self.state = "break"
                    self.pomodoro.set_label("BREAK TIME")
                elif self.state == "break":
                    self.minute, self.seconds = 25, 0
                    self.state = "work"
                    self.pomodoro.set_label("WORK TIME")

            if self.seconds == 0:
                self.minute -= 1
                self.seconds = 59
            else:
                self.seconds -= 1

            self.pomodoro.update()
            self.pomodoro.after(1000, counter)

        counter()


