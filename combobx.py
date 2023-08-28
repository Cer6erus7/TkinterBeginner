import tkinter as tk
from tkinter import ttk


WEEKDAYS = ("Monday", "Tuesday", 'Wednesday', "Thursday", "Friday", "Saturday", "Sunday")
LIST_INT = [1, 2, 3, 4, 5, 6, 7]


def show_day():
    combo_var = combo.get()
    print(combo_var, combo_int.get())
    day_var.set(combo_var)


def set_day():
    combo.set(WEEKDAYS[5])


win = tk.Tk()
photo = tk.PhotoImage(file="img.png")
win.iconphoto(False, photo)
win.config(bg="#153023")
win.title("My first GUI")
win.geometry("500x600+500+10")

day_var = tk.StringVar()

combo = ttk.Combobox(win, values=WEEKDAYS)
combo.current(1)
combo_int = ttk.Combobox(win, values=LIST_INT)
combo_int.current(4)
ttk.Button(win, text="Show day", command=show_day).pack()
ttk.Button(win, text='Set day', command=set_day).pack()
ttk.Label(win, textvariable=day_var).pack()


combo.pack()
combo_int.pack()

if __name__ == "__main__":
    win.mainloop()