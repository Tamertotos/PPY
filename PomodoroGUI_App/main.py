import app

if __name__ == "__main__":
    pomodoro = app.App()
    logic = app.Logic(pomodoro)


    pomodoro.build_buttons(logic)


    pomodoro.mainloop()

