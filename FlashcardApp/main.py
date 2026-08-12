import csv_utils
from app import App, Logic

def main():
    words = csv_utils.read("PolishEnglishTranslation.csv")
    flashcard_app = App()
    button_logic = Logic(flashcard_app,words)
    flashcard_app.build_buttons(button_logic)
    flashcard_app.mainloop()

if __name__ == "__main__":
    main()