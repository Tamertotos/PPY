import tkinter
import csv_utils

BG_COLOR ="#B1DDC6"

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg=BG_COLOR)
        self.title("Flashy")
        self.minsize(1000,800)

        self.image = {
            "front": tkinter.PhotoImage(file="Images/card_front.png"),
            "back": tkinter.PhotoImage(file="Images/card_back.png"),
            "right": tkinter.PhotoImage(file="Images/right.png"),
            "wrong": tkinter.PhotoImage(file="Images/wrong.png")
        }

        self.build_canvas()

    def build_canvas(self):
        self.canvas = tkinter.Canvas(self, width= 800, height=520, bg=BG_COLOR,highlightthickness=0)
        self.canvas_image = self.canvas.create_image(410,270, image=self.image["front"])
        self.canvas.place(x=100,y=50)
        self.text = self.canvas.create_text(410,120,text="", font=("Arial",40,"italic"))
        self.text2 = self.canvas.create_text(410,300,text="",font=("Arial",60,"bold"))

    def build_buttons(self,logic):
        self.button1 = tkinter.Button(self,image=self.image["right"], bg=BG_COLOR,relief="flat", command=logic.correct_button)
        self.button1.place(x=650,y=580)

        self.button2 = tkinter.Button(self,image=self.image["wrong"], bg=BG_COLOR,relief="flat",command=logic.wrong_button)
        self.button2.place(x=250,y=580)

    def change_front_back(self,state,language,color):
        self.canvas.itemconfig(self.canvas_image, image=self.image[state])
        self.canvas.itemconfig(self.text, text=language, fill=color)

    def change_text(self,word,color):
        self.canvas.itemconfig(self.text2, text=word,fill=color)

    def bind_canvas_click(self,handler):
        self.canvas.bind('<Button-1>', handler)

    def show_finished(self,message):
        self.canvas.itemconfig(self.text, text="")
        self.canvas.itemconfig(self.text2, text=message)
        self.button1["state"] = "disabled"
        self.button2["state"] = "disabled"
        self.canvas.unbind('<Button-1>')

class Logic:
    def __init__(self, flashcard_app, words):
        self.flashcard_app = flashcard_app
        self.state:str = "front"
        self.language:str = "Polish"
        self.flashcard_app.bind_canvas_click(self.change_canvas)
        self.count:int = 0
        self.mode = "Learning"
        self.color = "black"
        self.words_list = self.load_words(words)
        self.change_words()

    def load_words(self,words) -> list:
        try:
            result = csv_utils.read(csv_utils.REVIEW_FILE)
        except FileNotFoundError:
            result = words

        if len(result) > 0:
            self.mode = "Revising"
        else:
            self.mode = "Learning"

        return result if len(result) > 0 else words

    def change_canvas(self,event):
        if self.state == "front":
            self.state = "back"
            self.language = "English"
            self.color = "white"
            self.flashcard_app.change_text(self.words_list[self.count][1],self.color)
        elif self.state == "back":
            self.state = "front"
            self.language = "Polish"
            self.color = "black"
            self.flashcard_app.change_text(self.words_list[self.count][0], self.color)
        self.flashcard_app.change_front_back(self.state, self.language,self.color)

    def change_words(self):
        self.flashcard_app.change_front_back(self.state, self.language,"black" )
        self.flashcard_app.change_text(self.words_list[self.count][0], "black")

    def next_card(self):
        self.state = "front"
        self.language = "Polish"
        self.count += 1


        if self.count == len(self.words_list):
            self.finish()
        else:
            self.change_words()

    def wrong_button(self):
        if self.mode == "Learning":
            csv_utils.write_to_csv(self.words_list[self.count])
        self.next_card()

    def correct_button(self):
        if self.mode == "Learning":
            self.next_card()
        elif self.mode == "Revising":
            csv_utils.delete_from_csv(csv_utils.REVIEW_FILE,self.words_list[self.count])
            self.words_list.remove(self.words_list[self.count])
            self.count -= 1
            self.next_card()

    def finish(self):
        if self.mode == "Learning":
            message = "First pass done!"
        else:
            message = "All learnt!"
        self.flashcard_app.show_finished(message)
