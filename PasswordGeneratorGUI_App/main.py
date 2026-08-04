from app import App,Logic


def main():
    password_app = App()
    logic = Logic(password_app)


    password_app.build_buttons(logic)
    password_app.mainloop()

if __name__ == "__main__":
    main()