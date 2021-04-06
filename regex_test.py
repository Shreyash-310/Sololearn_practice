"""You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not."""

import re

n = int(input())
pattern = r"\A(1|8|9)\d{7}$"

match = re.match(pattern, str(n))
if match:
    print("Valid")
else:
    print("Invalid")
