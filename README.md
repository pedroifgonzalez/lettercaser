# ![Alt](https://github.com/pedroifgonzalez/lettercaser/blob/master/design/social_preview.png)

A simple widget app that provides some shortcuts of common letter cases:

- Uppercase
- Lowercase
- Capitalize
- Title
- Capitalize after every period.

Future improvements:

    - Add a tooltip for clarifying a button's letter case function.
    - Detect more accuractely when user selects or not a text.
    - Refactor code for better comprehension and usage of built-in components.

**For developers:**

Set work environment:

    - git clone https://github.com/pedroifgonzalez/lettercaser.git
    - virtualenv venv -p python3
    - source venv/bin/activate
    - pip install -r requirements.txt
    - pytest --doctest-modules

Run:

    python3 gui.py

1. Third-Party libraries used:
    - pyperclip
    - pyautogui

2. GUI library:
    - Tkinter
