import tkinter as tk


win = tk.Tk()
photo = tk.PhotoImage(file="img.png")
win.iconphoto(False, photo)
win.config(bg="#153023")
win.title("My first GUI")
win.geometry("500x600+500+10")

label_1 = tk.Label(win, text="Pidor",
                   bg="black",
                   fg='yellow',
                   font=("Arial", 15, "bold"),
                   padx=20,
                   pady=20,
                   width=20,
                   height=10,
                   anchor='se',
                   relief=tk.RIDGE,
                   bd=10,
                   justify=tk.CENTER)
label_1.pack()


win.mainloop()