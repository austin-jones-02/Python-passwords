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
import time

lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
nums = string.digits
special_chars = string.punctuation


def create_password_random_before(options="all", length=8):
    start = time.perf_counter()

    # Initialize character pool (What the password will pick from for creation)
    char_pool = ""

    if "l" in options or options.lower() == "all":
        char_pool += "".join([random.choice(lower_chars)
                             for _ in range(len(lower_chars) + 1)])
    if "u" in options or options.lower() == "all":
        char_pool += "".join([random.choice(upper_chars)
                             for _ in range(len(upper_chars) + 1)])
    if "n" in options or options.lower() == "all":
        char_pool += "".join([random.choice(nums)
                             for _ in range(len(nums) + 1)])
    if "s" in options or options.lower() == "all":
        char_pool += "".join([random.choice(special_chars)
                             for _ in range(len(special_chars) + 1)])

    char_pool = "".join([random.choice(char_pool)
                        for _ in range(len(char_pool) + 1)])
    print(f"Character pool used for password: {char_pool}")

    password = "".join([random.choice(char_pool) for _ in range(length + 1)])

    end = time.perf_counter()
    print(f"Random generation BEFORE runtime: {end - start:.6f}")
    return password


def create_password_random_after(options="all", length=8):
    start = time.perf_counter()

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

    print(f"Character pool used for password: {char_pool}")
    password = "".join([random.choice(char_pool) for _ in range(length + 1)])

    end = time.perf_counter()
    print(f"Random generation AFTER runtime: {end - start:.6f}")
    return password


if __name__ == '__main__':
    print(
        f"\nPassword with lower and upper and nums: {create_password_random_before("luns", 10)}")
    print(
        f"\nPassword with lower and upper and nums: {create_password_random_after("luns", 10)}")
