import tkinter

FONT = ("Courier",12,"normal")

class UI(tkinter.Tk):
    def __init__(self,quiz):
        super().__init__()
        self.quiz = quiz
        self.title("quiz")
        self.minsize(450,600)
        self.configure(background="blue")

        self.true_image = tkinter.PhotoImage(file="Images/true.png")
        self.false_image = tkinter.PhotoImage(file="Images/false.png")

        self.build_canvas()
        self.build_buttons()

    def build_canvas(self):
        self.canvas = tkinter.Canvas(self,bg="beige",height=300,width=350)
        self.canvas_text = self.canvas.create_text(175,100,text=self.quiz.questions[self.quiz.current_question_number].text,font=FONT,width=300)
        self.canvas.place(x=50,y=100)

    def build_label(self):
        self.label = tkinter.Label(self,)

    def build_buttons(self):
        self.button1 = tkinter.Button(self, image=self.true_image, command= lambda: self.button_clicked("true"))
        self.button1.place(x=75,y=450)

        self.button2 = tkinter.Button(self, image=self.false_image, command= lambda: self.button_clicked("false"))
        self.button2.place(x=275,y=450)

    def button_clicked(self,state):
        if self.quiz.has_next():
            self.quiz.next_question(state)
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.questions[self.quiz.current_question_number].text)