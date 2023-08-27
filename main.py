import tkinter as tk


def get_name():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty")


win = tk.Tk()
photo = tk.PhotoImage(file="img.png")
win.iconphoto(False, photo)
win.config(bg="#153023")
win.title("My first GUI")
win.geometry("500x600+500+10")

tk.Label(win, text="Name", bg="#153023").grid(row=0, column=0, stick='w')
name = tk.Entry(win, show="1")
tk.Button(win, text='Get', command=get_name).grid(row=1, column=0, stick='we')
tk.Button(win, text='Del', command=lambda: name.delete(0, tk.END)).grid(row=1, column=1, stick='we')
tk.Button(win, text='Insert "Hello!"', command=lambda: name.insert(0, "Hello!")).grid(row=2, columnspan=2, stick='we')

name.grid(row=0, column=1)

win.grid_columnconfigure(0, minsize=50)

if __name__ == "__main__":
    win.mainloop()