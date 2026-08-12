from reader import Reader
from app import App, Logic

def main():
    read = Reader("PolishEnglishTranslation.csv")
    flashcard_app = App()
    button_logic = Logic(flashcard_app,read.words)
    flashcard_app.build_buttons(button_logic)
    flashcard_app.mainloop()

if __name__ == "__main__":
    main()