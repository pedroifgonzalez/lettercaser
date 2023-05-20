import tkinter as tk

from lettercaser import gui


if __name__ == "__main__":
    root = tk.Tk()
    app = gui.Application(master=root)
    app.mainloop()
