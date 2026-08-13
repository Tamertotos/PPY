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
        self.text = self.canvas.create_text(410,120,text="Polish", font=("Arial",40,"italic"))
        self.text2 = self.canvas.create_text(410,300,text="AAAA",font=("Arial",60,"bold"))

    def build_buttons(self,logic):
        self.button1 = tkinter.Button(self,image=self.image["right"], bg=BG_COLOR,relief="flat", command=logic.next_card)
        self.button1.place(x=650,y=580)

        self.button2 = tkinter.Button(self,image=self.image["wrong"], bg=BG_COLOR,relief="flat",command=logic.wrong_button)
        self.button2.place(x=250,y=580)

    def change_front_back(self,state,language):
        self.canvas.itemconfig(self.canvas_image, image=self.image[state])
        self.canvas.itemconfig(self.text, text=language)

    def change_text(self,word):
        self.canvas.itemconfig(self.text2, text=word)

    def bind_canvas_click(self,handler):
        self.canvas.bind('<Button-1>', handler)

class Logic:
    def __init__(self, flashcard_app, words):
        self.flashcard_app = flashcard_app
        self.state = "front"
        self.language = "Polish"
        self.flashcard_app.bind_canvas_click(self.change_canvas)
        self.count = 0
        self.words_list = self.load_words(words)
        self.change_words()

    def load_words(self,words):
        try:
            result = csv_utils.read(csv_utils.REVIEW_FILE)
        except FileNotFoundError:
            result = words

        return result if len(result) > 0 else words

    def change_canvas(self,event):
        if self.state == "front":
            self.state = "back"
            self.language = "English"
            self.flashcard_app.change_text(self.words_list[self.count][1])
        elif self.state == "back":
            self.state = "front"
            self.language = "Polish"
            self.flashcard_app.change_text(self.words_list[self.count][0])
        self.flashcard_app.change_front_back(self.state, self.language)

    def change_words(self):
        self.flashcard_app.change_front_back(self.state, self.language)
        self.flashcard_app.change_text(self.words_list[self.count][0])

    def next_card(self):
        self.state = "front"
        self.language = "Polish"
        self.count += 1
        if self.count > len(self.words_list) - 1:
            self.flashcard_app.destroy()
            return
        self.change_words()

    def wrong_button(self):
        csv_utils.write_to_csv(self.words_list[self.count])
        self.next_card()




