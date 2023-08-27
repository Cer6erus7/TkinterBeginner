import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():
    print("Flag 18", over_18_value.get())
    print("Commercial", commercial_value.get())


win = tk.Tk()
photo = tk.PhotoImage(file="img.png")
win.iconphoto(False, photo)
win.config(bg="#153023")
win.title("My first GUI")
win.geometry("500x600+500+10")

over_18_value = tk.StringVar()
over_18_value.set("No!")
commercial_value = tk.IntVar()

over_18 = tk.Checkbutton(win, text='Are you over 18?',
                         variable=over_18_value,
                         onvalue="Yes!",
                         offvalue="No!")
commercial = tk.Checkbutton(win, text="Do you want to take ad?",
                            variable=commercial_value,
                            onvalue=1,
                            offvalue=0)
follow = tk.Checkbutton(win, text="Do you want to follow the chanel?", indicatoron=False)

over_18.pack()
commercial.pack()
follow.pack()

btn = tk.Button(win, text="Select all!", command=select_all)
btn.pack()
btn1 = tk.Button(win, text="Deselect all!", command=deselect_all)
btn1.pack()
btn2 = tk.Button(win, text="Switch all!", command=switch_all)
btn2.pack()
btn3 = tk.Button(win, text="Show", command=show)
btn3.pack()

win.grid_columnconfigure(0, minsize=50)

if __name__ == "__main__":
    win.mainloop()