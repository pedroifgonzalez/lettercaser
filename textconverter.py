#!usr/bin/python3    
"""Module for transformings text to different formats using str built-in methods
"""

def to_uppercase(text: str)-> str:
    """Converts to uppercase"""
    return text.upper()

def to_lowercase(text: str)-> str:
    """Converts to lowercase"""
    return text.lower()

def to_title_case(text: str)-> str:
    """Converts to title case"""
    return text.title()

def capitalize(text: str)-> str:
    """Capitalize text"""
    return text.capitalize()

def capitalize_after_one_period(text: str)-> str:
    """Capitalize text after every one period
    
    This function will remove any leading and trailing whitespace except for sentences between 
    three periods (...)
    """
    three_period_separated_sentences = text.split("...")
    all_sentences = []
    for three_period_sentence in three_period_separated_sentences:
        sentences = three_period_sentence.split(".")
        capitalized_sentences = [sentence.strip().capitalize() for sentence in sentences]
        all_sentences.append(". ".join(capitalized_sentences).rstrip())

    return "...".join(all_sentences)