import tkinter

FONT = ("Arial",16,"italic")
THEME_COLOR = "#375362"

class UI(tkinter.Tk):
    def __init__(self,quiz):
        super().__init__()
        self.quiz = quiz
        self.title("quiz")
        self.minsize(450,600)
        self.configure(background=THEME_COLOR)

        self.true_image = tkinter.PhotoImage(file="Images/true.png")
        self.false_image = tkinter.PhotoImage(file="Images/false.png")

        self.build_canvas()
        self.build_label()
        self.build_buttons()

    def build_canvas(self):
        self.canvas = tkinter.Canvas(self,bg="beige",height=300,width=350)
        self.canvas_text = self.canvas.create_text(175,100,text=self.quiz.questions[self.quiz.current_question_number].text,font=FONT,width=300)
        self.canvas.place(x=50,y=100)

    def build_label(self):
        self.label1 = tkinter.Label(self,text= f"Score: {self.quiz.score}/{len(self.quiz.questions)}",font=FONT,bg=THEME_COLOR,fg="white")
        self.label1.place(x=315, y=50)

    def build_buttons(self):
        self.true_button = tkinter.Button(self, image=self.true_image, command= lambda: self.check_answer("true"),highlightthickness=0)
        self.true_button.place(x=75, y=450)

        self.false_button = tkinter.Button(self, image=self.false_image, command= lambda: self.check_answer("false"),highlightthickness=0)
        self.false_button.place(x=275, y=450)

    def change_text(self):
        self.canvas.configure(bg="beige")
        self.true_button["state"] = "normal"
        self.false_button["state"] = "normal"
        if self.quiz.has_next():
            self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.questions[self.quiz.current_question_number].text)
        else:
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"

    def check_answer(self,state):
        color = self.quiz.check_answer(state)
        self.canvas.configure(bg=color)
        self.label1.config(text=f"Score: {self.quiz.score}/{len(self.quiz.questions)}")
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        self.after(5000, self.change_text)
