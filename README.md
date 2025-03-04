# password-manager-py

A simple password manager that can generate a password with various options and length.

## Options include:

- Any combinations of what's below. Default is **all**.
- lowercase letters (l).
- Uppercase letters (u).
- Numbers (n).
- Special characters (s).

## Length:

- Default length is **8** but can be set to whatever you want.

## Usage:

```powershell
py create_password.py # Default options. Generates a password with lower and upper-case letters, numbers, and special characters.

py create_password.py lns 20 # Generates a password with lowercase letters, numbers, and special characters.

py create_password.py 15 # Generates a password with all options and a length of 15.
```

## Upcoming features:

- A password finder/searcher where user can quickly find their password.
  - _Create a password if one is not found if user wants to._
