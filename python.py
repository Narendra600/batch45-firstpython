import tkinter as tk
from time import strftime

clock = tk.Tk()
clock.title("Clock")

label = tk.Label(clock, font=("Arial", 48), padx=20, pady=10)
label.pack()

def update_clock():
    label.config(text=strftime("%H:%M:%S"))
    clock.after(1000, update_clock)

update_clock()
clock.mainloop()