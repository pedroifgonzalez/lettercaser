#!usr/bin/python3    
"""Module for transformings text to different formats using str built-in methods
"""

def to_uppercase(text: str)-> str:
    """Converts to uppercase
    
    >>> to_uppercase("word")
    'WORD'
    """
    return text.upper()

def to_lowercase(text: str)-> str:
    """Converts to lowercase
    
    >>> to_lowercase("All Words WERE converted to lower")
    'all words were converted to lower'
    """
    return text.lower()

def to_title_case(text: str)-> str:
    """Converts to title case
    
    >>> to_title_case("you got a title case")
    'You Got A Title Case'
    """
    return text.title()

def capitalize(text: str)-> str:
    """Capitalize text
    
    >>> capitalize("initial letter is written in uppercase")
    'Initial letter is written in uppercase'
    """
    return text.capitalize()

def capitalize_after_one_period(text: str)-> str:
    """Capitalize text after every one period
    
    This function will remove any leading and trailing whitespace except for sentences between 
    three periods (...)

    >>> capitalize_after_one_period("initial letter is written in uppercase after a period too. remember that...")
    'Initial letter is written in uppercase after a period too. Remember that...'
    """
    three_period_separated_sentences = text.split("...")
    all_sentences = []
    for three_period_sentence in three_period_separated_sentences:
        sentences = three_period_sentence.split(".")
        if len(sentences)>1:
            capitalized_sentences = []
            capitalized_sentences.append(sentences[0])
            for sentence in sentences[1:]:
                capitalized_sentences.append(sentence.strip().capitalize())
            all_sentences.append(". ".join(capitalized_sentences).rstrip())
        else:
            all_sentences.append(sentences[0])

    return "...".join(all_sentences)

if __name__ == "__main__":
    import doctest
    doctest.testmod()