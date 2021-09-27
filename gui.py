#!/usr/bin/env python3
"""
    App GUI module 
"""
import threading
import time
import tkinter as tk
import utils


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.clicked_button = None
        self.conversion_status = False
        self.status = True
        self.master.resizable(False, False)
        self.master.attributes("-topmost", True)
        self.master.wm_withdraw()
        self.master.overrideredirect(True)
        self.master.bind("<Enter>", lambda *ignore: self.set_status(True))
        self.master.bind("<Leave>", lambda *ignore: self.set_status(False))
        self.pack()
        self.create_buttons()
        self.start_notification_thread()
        self.start_selected_text_thread()
        self.start_hide_gui_thread()

    def set_status(self, status: bool):
        self.status = status

    def start_notification_thread(self):
        def notificate_conversion_success():
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
        thread = threading.Thread(target=notificate_conversion_success, daemon=True)
        thread.start()
    
    def start_selected_text_thread(self):
        def thread_selected_text_function():
            while True:
                if utils.detect_selected_text_changed():
                    cursor_position = utils.get_mouse_cursor_position()
                    app_wsize = utils.Size(250, 35)
                    x, y = utils.get_cursor_position_to_set(app_wsize, cursor_position)
                    self.master.geometry(f"+{x}+{y}")
                    self.master.wm_deiconify()

        thread = threading.Thread(target=thread_selected_text_function, daemon=True)
        thread.start()
    
    def start_hide_gui_thread(self):
        def hide_gui_thread():
            while True:
                status = self.status
                time.sleep(3)
                if status is False:
                    self.master.wm_withdraw()
        thread = threading.Thread(target=hide_gui_thread, daemon=True)
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
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.title_converter), 
                self.set_clicked_button("title_button")),
            **common_options
        )
        self.after_period_capitalize_button = tk.Button(
            self,
            text="Ab.C",
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.capitalize_after_one_periodconverter),
                self.set_clicked_button("after_period_capitalize_button")),
            **common_options
        )
        self.uppercase_button = tk.Button(
            self,
            text="A",
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.upper_converter), 
                self.set_clicked_button("uppercase_button")),
            **common_options
        )
        self.lowercase_button = tk.Button(
            self,
            text="a",
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.lower_converter),
                self.set_clicked_button("lowercase_button")),
            **common_options
        )
        self.capitalize_button = tk.Button(
            self,
            text="Ab",
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.capitalizer_converter),
                self.set_clicked_button("capitalize_button")),
            **common_options
        )
        
        self.after_period_capitalize_button.pack(side="right")
        self.title_button.pack(side="right")
        self.capitalize_button.pack(side="right")
        self.lowercase_button.pack(side="right")
        self.uppercase_button.pack(side="right")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
