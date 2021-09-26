"""
    Module for integrating clipboard management and text conversion

    Available functions: 
        get_selected_text
        is_selected_text_copied
        convert_clipoboard_content
        functions_caller
        concatenate_functions_calls
"""
import subprocess
import logging
import functools
import pyperclip
from typing import Callable

import textconverter

def get_previous_selected_text():
    """Returns the previous selected text by the user"""
    pass

def get_selected_text():
    """Returns the output of xsel"""
    return subprocess.check_output("xsel", universal_newlines=True)

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

def convert_clipboard_content(function: Callable):
    """Retrieves clipboard content, converts it and updates it"""
    original_clipboard_content = pyperclip.paste()
    try:
        converted_clipboard_content = function(original_clipboard_content)
    except Exception as e:
        raise e
    pyperclip.copy(converted_clipboard_content)
    return True

upper_converter = functools.partial(convert_clipboard_content, textconverter.to_uppercase)
lower_converter = functools.partial(convert_clipboard_content, textconverter.to_lowercase)
title_converter = functools.partial(convert_clipboard_content, textconverter.to_title_case)
capitalizer_converter = functools.partial(convert_clipboard_content, textconverter.capitalize)
capitalize_after_one_periodconverter = functools.partial(convert_clipboard_content, textconverter.capitalize_after_one_period)