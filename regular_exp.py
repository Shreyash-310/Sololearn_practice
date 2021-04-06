import re

"""pattern = r"spam"

#re.match function can be used to determine whether it matches at the beginning of a string.
if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

# The function re.search finds a match of a pattern anywhere in the string.
if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")
# function re.findall returns a list of all substrings that match a pattern."""

"""patt = r"pam"
match = re.search(patt, "eggspamsausagespam")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())"""

str = "My name is shree, Hi shree!"
pattern = r"shree"
newstr = re.sub(pattern, 'vicky', str)
print(newstr)
