import tkinter as tk
import utils


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.resizable(False, False)
        self.master.geometry("-100-100")
        self.master.attributes("-topmost", True)
        self.pack()
        self.create_buttons()

    def create_buttons(self):
        common_options = dict(
            borderwidth=0, background="#f4d7d7", activebackground="#e9afaf", anchor="w"
        )

        title_button = tk.Button(
            self, text="AbC", command=utils.title_converter, **common_options
        )
        after_period_capitalize_button = tk.Button(
            self,
            text="Ab.C",
            command=utils.capitalize_after_one_periodconverter,
            **common_options
        )
        uppercase_button = tk.Button(
            self, text="A", command=utils.upper_converter, **common_options
        )
        lowercase_button = tk.Button(
            self, text="a", command=utils.lower_converter, **common_options
        )
        capitalize_button = tk.Button(
            self, text="Ab", command=utils.capitalizer_converter, **common_options
        )

        uppercase_button.pack(fill="x")
        lowercase_button.pack(fill="x")
        capitalize_button.pack(fill="x")
        title_button.pack(fill="x")
        after_period_capitalize_button.pack(fill="x")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
