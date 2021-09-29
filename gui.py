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
        self.xposition = None
        self.yposition = None
        self.uppercase_button_image = tk.PhotoImage(file=utils.get_button_image_path('uppercase_button_image'))
        self.lowercase_button_image = tk.PhotoImage(file=utils.get_button_image_path('lowercase_button_image'))
        self.title_button_image = tk.PhotoImage(file=utils.get_button_image_path('title_button_image'))
        self.capitalize_button_image = tk.PhotoImage(file=utils.get_button_image_path('capitalize_button_image'))
        self.after_period_capitalize_button_image = tk.PhotoImage(file=utils.get_button_image_path('after_period_capitalize_button_image'))
        self.master.resizable(False, False)
        self.master.attributes("-topmost", True)
        self.master.wm_withdraw()
        self.master.overrideredirect(True)
        self.master.bind("<Motion>", lambda *ignore: self.set_status(True))
        self.master.bind("<Leave>", lambda *ignore: self.set_status(False))
        self.create_buttons()
        self.start_thread()
        self.pack()

    def set_status(self, status: bool):
        self.status = status

    def start_thread(self):
        def to_check():
            while True:
                # to hide the app
                status = self.status
                if status is False:
                    time.sleep(1)
                    if status == self.status:
                        self.master.wm_withdraw()
                        self.xposition = None
                        self.yposition = None
                        self.status = True
                
                if self.xposition and self.yposition:
                    cursor_position = utils.get_mouse_cursor_position()
                    xdifference = abs(cursor_position.x - self.xposition)
                    ydifference = abs(cursor_position.y - self.yposition)
                    if xdifference > 300 or ydifference > 250:
                        self.master.wm_withdraw()
                        self.xposition = None
                        self.yposition = None
                        self.status = True
                
                # detect change of selected text
                if utils.detect_selected_text_changed():
                    cursor_position = utils.get_mouse_cursor_position()
                    app_wsize = utils.Size(250, 35)
                    x, y = utils.get_cursor_position_to_set(app_wsize, cursor_position)
                    self.master.geometry(f"+{x}+{y}")
                    self.xposition = x
                    self.yposition = y
                    self.master.wm_deiconify()

                # show success
                clicked_button = self.clicked_button
                conversion_status = self.conversion_status

                if clicked_button and conversion_status:
                    original_text = clicked_button['text']
                    clicked_button['text'] = "OK"
                    time.sleep(1)
                    clicked_button['text'] = original_text
                    self.clicked_button = None
                    self.conversion_status = False

        thread = threading.Thread(target=to_check, daemon=True)
        thread.start()

    def set_clicked_button(self, button_name):
        self.clicked_button = getattr(self, button_name)
    
    def check_conversion_status(self, converter_function):
        if converter_function():
            self.conversion_status = True

    def create_buttons(self):
        common_options = dict(
            borderwidth=0, 
            anchor="w"
        )

        self.title_button = tk.Button(
            self,
            image=self.title_button_image,
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.title_converter), 
                self.set_clicked_button("title_button")),
            **common_options
        )
        self.after_period_capitalize_button = tk.Button(
            self,
            image=self.after_period_capitalize_button_image,
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.capitalize_after_one_periodconverter),
                self.set_clicked_button("after_period_capitalize_button")),
            **common_options
        )
        self.uppercase_button = tk.Button(
            self,
            image=self.uppercase_button_image,
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.upper_converter), 
                self.set_clicked_button("uppercase_button")),
            **common_options
        )
        self.lowercase_button = tk.Button(
            self,
            image=self.lowercase_button_image,
            command=lambda: utils.concatenate_functions_calls(self.check_conversion_status(utils.lower_converter),
                self.set_clicked_button("lowercase_button")),
            **common_options
        )
        self.capitalize_button = tk.Button(
            self,
            image=self.capitalize_button_image,
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
