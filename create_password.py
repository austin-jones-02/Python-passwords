import os
import sys
import string
import random
import argparse

lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
nums = string.digits
special_chars = string.punctuation


def main():
    parser = argparse.ArgumentParser(
        description="""Generate a password and save to a txt file on desktop.
                    options are l (lowercase), u (uppercase), n (numbers), s (special characters), or all."""
    )
    parser.add_argument(
        "options_or_length",
        nargs='?',
        default="all",
        help="Either options (l/u/n/s/all) or just the length as a number."
    )
    parser.add_argument(
        "length",
        nargs='?',
        default=None,
        type=int,
        help="Length of password to be generated."
    )

    args = parser.parse_args()

    # Check if first argument is a number (length)
    try:
        length = int(args.options_or_length)
        options = "all"  # Use default options
    except ValueError:
        # First argument is options
        options = args.options_or_length
        length = args.length if args.length is not None else 8

    password = create_password_random(options, length)
    print(f"Password: {password}\nOptions: {options}\nLength: {length}")

    save_to_file = input("Save this password to file? [Y/N]: ")

    if save_to_file.lower() == "n":
        sys.exit("Password not saved to file...")
    elif save_to_file.lower() == "y":
        try:
            path = os.path.join(os.path.join(
                os.environ["USERPROFILE"]), "Desktop")
            name = "password_vault.txt"

            use_for_password = input(
                "The name or thing that the password is for: ")

            file = open(os.path.join(path, name), "a")
            file.write(f"{use_for_password}: {password}\n")
            file.close()

            file = open(os.path.join(path, name), "r")
            print(file.read())
            file.close()

        except KeyError:
            raise KeyError("Error occurred trying to access desktop path.")
    else:
        sys.exit("Invalid response to question... Exiting program")


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

    password = "".join([random.choice(char_pool) for _ in range(length)])

    return password


if __name__ == "__main__":
    main()
