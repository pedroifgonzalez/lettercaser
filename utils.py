"""
    Module for integrate clipboard management and text conversion

    Available function: convert_clipoboard_content
"""
import pyperclip
import functools
from typing import Callable

import textconverter

def functions_caller(*functions):
    for function in functions:
        function()

def concatenate_functions_calls(*functions_calls):
    """Function with the only purpose of joining function calls
    
    Returns True if all return values are different from False or equivalent
    """
    return all(functions_calls)

def convert_clipoboard_content(function: Callable):
    """Retrieves clipboard content, converts it and updates it"""
    original_clipboard_content = pyperclip.paste()
    try:
        converted_clipboard_content = function(original_clipboard_content)
    except Exception as e:
        raise e
    pyperclip.copy(converted_clipboard_content)
    return True

upper_converter = functools.partial(convert_clipoboard_content, textconverter.to_uppercase)
lower_converter = functools.partial(convert_clipoboard_content, textconverter.to_lowercase)
title_converter = functools.partial(convert_clipoboard_content, textconverter.to_title_case)
capitalizer_converter = functools.partial(convert_clipoboard_content, textconverter.capitalize)
capitalize_after_one_periodconverter = functools.partial(convert_clipoboard_content, textconverter.capitalize_after_one_period)