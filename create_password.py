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


def create_password_random(options="all", length=8):
    # Initialize character pool (What the password will pick from for creation)
    char_pool = ""

    if "l" in options or options.lower() == "all":
        char_pool += lower_chars
    if "u" in options or options.lower() == "all":
        char_pool += upper_chars
    if "n" in options or options.lower() == "all":
        char_pool += nums
    if "s" in options or options.lower() == "all":
        char_pool += special_chars

    password = "".join([random.choice(char_pool) for _ in range(length + 1)])

    return password


if __name__ == '__main__':
    print(create_password_random('l', 10))
    print(create_password_random('lu', 10))
    print(create_password_random('lun', 10))
    print(create_password_random('all', 10))  # also could do "luns"
