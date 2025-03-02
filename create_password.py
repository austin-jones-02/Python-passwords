"""
Holds the functions to create password

Note:
    Not sure what all will be needed... probably should have options for password to include:
        - Lowercase
        - Uppercase
        - Numbers
        - Randomized symbols aka special chars    
"""

import string
import random

lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
nums = string.digits
special_chars = string.punctuation


def create_password(options="all", length="8"):
    char_pool = ""

    match options.lower():
        case "l":
            char_pool += lower_chars
        case "all":
            char_pool += lower_chars + upper_chars + nums + special_chars

    return char_pool


if __name__ == '__main__':
    print(create_password())
