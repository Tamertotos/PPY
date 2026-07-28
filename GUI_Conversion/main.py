import tkinter
from tkinter import ttk

CONVERSION: list[str] = ["Mile","Km","Meter","Foot","Centimeter"]
TO_BASE_VALUE = {
    "Mile": 1609.34,
    "Foot": 0.3048,
    "Km": 1000,
    "Centimeter" : 0.01,
    "Meter" : 1,
}

def convert(value:float,from_unit:str, to_unit:str) -> float:
    base_value = value * TO_BASE_VALUE[from_unit]
    return base_value / TO_BASE_VALUE[to_unit]

def calculate():
    try:
        value = float(entry1.get())
        from_unit = combo1.get()
        to_unit = combo2.get()


        if from_unit and to_unit:
            result = convert(value,from_unit,to_unit)
            label2.config(text=f"is equal to {result:.2f}")
        else:
            label2.config(text="Pick both units!")

    except ValueError:
            label2.config(text="Enter a valid number!")

def combobox_used(event):
    calculate()

def create_entry(window,x,y) -> tkinter.Entry:
    entry = tkinter.Entry(window)
    entry.grid(row=x,column=y)
    return entry

def create_label(window,x,y,text) -> tkinter.Label:
    label = tkinter.Label(window,text=text)
    label.grid(row=x,column=y)
    return label

def create_combobox(window,x,y) -> ttk.Combobox:
    combo = ttk.Combobox(window, values=CONVERSION)
    combo.grid(row=x,column=y)
    return combo

def create_button(window,x,y,text,color,to_do) -> tkinter.Button:
    button = tkinter.Button(window,text=text, fg=color, command=to_do)
    button.place(x=x,y=y)
    button.config(padx=10,pady=10)
    return button

def create_window() -> tkinter.Tk:
    window = tkinter.Tk()
    window.title("Converter")
    window.minsize(width=200,height=150)
    window.config(padx=30,pady=30)
    return window

if __name__ == "__main__":
    frame = create_window()
    combo1 = create_combobox(frame,0,3)
    combo2 = create_combobox(frame,1,3)
    label1 = create_label(frame,1,1,"to")
    label2 = create_label(frame,1,5,"is equal to = 0")
    button1 = create_button(frame,100,50,"QUIT","red",frame.quit)
    button2 = create_button(frame,170,50,"Calculate","black",calculate)
    entry1 = create_entry(frame,0,1)
    combo1.bind("<<ComboboxSelected>>",combobox_used)
    combo2.bind("<<ComboboxSelected>>",combobox_used)

    frame.mainloop()


