"""
This file will be to used to find a password from the desktop file that is created
or updated during create_password.py execution.

Notes:
    - Need to figure out how to search through file quickly.
        - Regex?
    - Needs to prompt user if password not found if they would like to create one.
        - Will need to figure out how to import create_password.py into here and make
        sure everything works.
"""
import os
import re


def main():
    find_passwords("netflix")


def find_passwords(service_or_account_name):
    path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    name = "password_vault.txt"
    filename = os.path.join(path, name)

    with open(filename, "r") as file:
        content = file.read()
        print(content)

        # Regex to find password for user specified service
        pattern = re.compile(
            fr'(?i)^{re.escape(service_or_account_name)}:\s+(.+)$', re.MULTILINE)
        print(pattern)

        matches = pattern.findall(content)
        print(matches)
        file.close()

        if matches:
            return matches
        else:
            return "No password found... Create one?"


if __name__ == "__main__":
    main()
