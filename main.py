import tkinter as tk
import funcs

COUNT = 0


win = tk.Tk()
photo = tk.PhotoImage(file="img.png")
win.iconphoto(False, photo)
win.config(bg="#153023")
win.title("My first GUI")
win.geometry("500x600+500+10")

def new_label():
    label = tk.Label(win, text="Petuh",
                     bg="black",
                     fg='yellow',
                     font=("Arial", 15, "bold"),
                     relief=tk.RIDGE
                     )
    label.pack()

def counter():
    global COUNT
    COUNT += 1
    btn2["text"] = COUNT

def disabler():
    btn2['state'] = tk.DISABLED
    btn3["text"] = "Undisable"
    btn3["command"] = undisabler

def undisabler():
    btn2['state'] = tk.ACTIVE
    btn3["text"] = "Disable"
    btn3["command"] = disabler


btn1 = tk.Button(win, text="Make a new label!",
                 command=new_label)

btn2 = tk.Button(win, text="Count!",
                 command=counter,
                 bg="red",
                 activebackground="Blue",
                 state=tk.DISABLED)

btn3 = tk.Button(win, text='Undisable',
                 command=undisabler)

btn1.pack()
btn2.pack()
btn3.pack()

if __name__ == "__main__":
    win.mainloop()