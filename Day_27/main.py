from tkinter import *


def button_clicked():
    miles = float(user_input.get())
    km = round(miles * 1.60,2)
    km_output.config(text=f"{km}")


window = Tk()
window.title("MIle to Km Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=("Arial", 24))
km_label = Label(text="Km", font=("Arial", 24))
km_output = Label(text="", font=("Arial", 24))
is_equal_label = Label(text="Is equal to", font=("Arial", 24))

miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
km_output.grid(column=1, row=1)
is_equal_label.grid(column=0, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

user_input = Entry(width=7)
user_input.grid(column=1, row=0)

window.mainloop()
