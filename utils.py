"""
    Module for integrating clipboard management, text conversion and handling mouse events.

    Available functions: 
        get_selected_text
        is_selected_text_copied
        convert_clipoboard_content
        functions_caller
        concatenate_functions_calls
"""
import os
import subprocess
import collections
import logging
import functools
import pyperclip
import pyautogui
from typing import Callable

import textconverter

Size = collections.namedtuple("Size", "width height")
Point = collections.namedtuple("Point", "x y")

def get_cursor_position_to_set(app_wsize: Size, cursor_position: Point, distance_from_cursor: Point = Point(x=20,y=50)):
    x_required_distance = app_wsize.width + distance_from_cursor.x
    y_required_distance = app_wsize.height + distance_from_cursor.y

    x_position = cursor_position.x
    y_position = cursor_position.y

    if cursor_position.x + x_required_distance > pyautogui.size().width:
        x_position -= x_required_distance
    else:
        x_position += distance_from_cursor.x

    if  cursor_position.y - y_required_distance < 0:
        y_position += distance_from_cursor.y
    else:
        y_position -= distance_from_cursor.y

    return Point(x_position, y_position) 
    

def get_mouse_cursor_position():
    """Returns mouse cursor position"""
    return pyautogui.position()

def get_previous_selected_text():
    """Returns the previous selected text by the user"""
    global previous_selected_text
    return previous_selected_text

def get_selected_text():
    """Returns the output of xsel"""
    return subprocess.check_output("xsel", universal_newlines=True)

previous_selected_text = get_selected_text()

def is_selected_text_copied():
    """Returns True if the selected text by the user is currently at the clipboard"""
    current_content = get_selected_text()
    clipboard_content = pyperclip.paste()
    if current_content == clipboard_content:
        return True

def detect_selected_text_changed():
    """Returns True if the current selected text is different from the previous one"""
    previous_content = get_previous_selected_text()
    current_content = get_selected_text()
    if previous_content != current_content:
        global previous_selected_text
        previous_selected_text = current_content
        return True

def functions_caller(*functions):
    """Calls every function passed as argument"""
    for function in functions:
        try:
            function()
        except TypeError as e:
            logging.error(e)

def concatenate_functions_calls(*functions_calls):
    """Function with the only purpose of joining function calls
    
    Returns True if all return values are different from False or equivalent
    """
    return all(functions_calls)

def convert_clipboard_content(function: Callable, selected_text=True):
    """Retrieves clipboard content, converts it and updates it
    
    arguments:

        function: function to apply to clipboard's content

        selected_text: flag to copy or not from the selected text by the user
    """
    if selected_text:
        pyperclip.copy(get_selected_text())
    original_clipboard_content = pyperclip.paste()
    try:
        converted_clipboard_content = function(original_clipboard_content)
    except Exception as e:
        raise e
    pyperclip.copy(converted_clipboard_content)
    return True

def get_button_image_path(button_name):
    return f"{PHOTOS_FOLDER_PATH}{os.path.sep}{button_name}.png"

upper_converter = functools.partial(convert_clipboard_content, textconverter.to_uppercase)
lower_converter = functools.partial(convert_clipboard_content, textconverter.to_lowercase)
title_converter = functools.partial(convert_clipboard_content, textconverter.to_title_case)
capitalizer_converter = functools.partial(convert_clipboard_content, textconverter.capitalize)
capitalize_after_one_periodconverter = functools.partial(convert_clipboard_content, textconverter.capitalize_after_one_period)

PHOTOS_FOLDER = "design"
PHOTOS_FOLDER_PATH = f"{os.path.dirname(os.path.abspath(__file__))}{os.path.sep}{PHOTOS_FOLDER}"