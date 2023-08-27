import tkinter as tk


LEVELS = {
    1: "Easy",
    2: "Middle",
    3: "Hard"
}

RASES = ['Orcs', "People", "Elfs"]


def select_level():
    level = level_var.get()
    level_text.set(f"You chose level {level}")
    print(LEVELS[level])


def select_rase():
    rase = rase_var.get()
    rase_text.set(f"You chose {rase}!")
    print(rase)


win = tk.Tk()
photo = tk.PhotoImage(file="img.png")
win.iconphoto(False, photo)
win.config(bg="#153023")
win.title("My first GUI")
win.geometry("500x600+500+10")

level_var = tk.IntVar()
level_text = tk.StringVar()
rase_var = tk.StringVar()
rase_var.set("People")
rase_text = tk.StringVar()


tk.Label(win, text="Choose difficulty!").pack()
for level in sorted(LEVELS):
    tk.Radiobutton(win, text=LEVELS[level], variable=level_var, value=level, command=select_level).pack()
tk.Label(win, textvariable=level_text).pack()

tk.Label(win, text="Choose rase!").pack()
for rase in RASES:
    tk.Radiobutton(win, text=rase, variable=rase_var, value=rase, command=select_rase).pack()
tk.Label(win, textvariable=rase_text).pack()

if __name__ == "__main__":
    win.mainloop()