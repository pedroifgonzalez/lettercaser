#!/usr/bin/env python3
"""
    App GUI module 
"""
import threading
import time
import tkinter as tk
from utils import (concatenate_functions_calls, upper_converter, lower_converter, capitalizer_converter,
                    capitalize_after_one_periodconverter, title_converter)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.clicked_button = None
        self.conversion_status = False
        self.master.resizable(False, False)
        self.master.geometry("-100-100")
        self.master.attributes("-topmost", True)
        self.pack()
        self.create_buttons()
        self.start_thread()
    
    def start_thread(self):
        thread = threading.Thread(target=self.notificate_conversion_success, daemon=True)
        thread.start()
    
    def set_clicked_button(self, button_name):
        self.clicked_button = getattr(self, button_name)
    
    def check_conversion_status(self, converter_function):
        if converter_function():
            self.conversion_status = True

    def create_buttons(self):
        common_options = dict(
            borderwidth=0, background="#f4d7d7", activebackground="#e9afaf", anchor="w"
        )

        self.title_button = tk.Button(
            self,
            text="AbC",
            command=lambda: concatenate_functions_calls(self.check_conversion_status(title_converter), 
                self.set_clicked_button("title_button")),
            **common_options
        )
        self.after_period_capitalize_button = tk.Button(
            self,
            text="Ab.C",
            command=lambda: concatenate_functions_calls(self.check_conversion_status(capitalize_after_one_periodconverter),
                self.set_clicked_button("after_period_capitalize_button")),
            **common_options
        )
        self.uppercase_button = tk.Button(
            self,
            text="A",
            command=lambda: concatenate_functions_calls(self.check_conversion_status(upper_converter), 
                self.set_clicked_button("uppercase_button")),
            **common_options
        )
        self.lowercase_button = tk.Button(
            self,
            text="a",
            command=lambda: concatenate_functions_calls(self.check_conversion_status(lower_converter),
                self.set_clicked_button("lowercase_button")),
            **common_options
        )
        self.capitalize_button = tk.Button(
            self,
            text="Ab",
            command=lambda: concatenate_functions_calls(self.check_conversion_status(capitalizer_converter),
                self.set_clicked_button("capitalize_button")),
            **common_options
        )

        self.uppercase_button.pack(fill="x")
        self.lowercase_button.pack(fill="x")
        self.capitalize_button.pack(fill="x")
        self.title_button.pack(fill="x")
        self.after_period_capitalize_button.pack(fill="x")

    def notificate_conversion_success(self):
        while True:
            
            clicked_button = self.clicked_button
            conversion_status = self.conversion_status

            if clicked_button and conversion_status:
                original_text = clicked_button['text']
                clicked_button['text'] = "OK"
                time.sleep(1)
                clicked_button['text'] = original_text
                self.clicked_button = None
                self.conversion_status = False

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
