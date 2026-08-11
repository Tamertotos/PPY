from reader import Reader
from app import App

def main():
    read = Reader("PolishEnglishTranslation.csv")
    flashcard_app = App()
    print(read.words)

    flashcard_app.mainloop()

if __name__ == "__main__":
    main()