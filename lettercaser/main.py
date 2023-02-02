import tkinter as tk

import lettercaser.gui as gui


if __name__ == "__main__":
    root = tk.Tk()
    app = gui.Application(master=root)
    app.mainloop()
