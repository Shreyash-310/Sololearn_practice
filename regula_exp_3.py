import re

"""pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, 'abcdefghijklmnop')
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))"""

"""pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, 'abcdefghi')
if match:
    print(match.group("first"))
    print(match.groups())"""

"""pattern = r"gr(e|a)y"
match = re.match(pattern, "gray")
if match:
    print("match 1")
match = re.match(pattern, "grey")
if match:
    print("match 2")"""

"""pattern = r"(.+)\1"
match = re.match(pattern, "word word word")
if match:
    print("match 1")
match = re.match(pattern, "?! ?!")
if match:
    print("match 2")
match = re.match(pattern, "abc cde")
if match:
    print("match 3")"""

"""pattern = r"(\D+\d)"        #  matches one or more non-digits followed by a digit.
match = re.match(pattern, "Hi 999!")
if match:
    print("match 1")
match = re.match(pattern, "A, 23, 456!")
if match:
    print("match 2")
match = re.match(pattern, " ! $?")
if match:
    print("match 3")"""

"""pattern = r"\AS...\b.\Z"
match = re.match(pattern, "SPAM!")
if match:
    print("match 1")"""

# email extraction  [\w\.-]+ matches one or more word character, dot or dash.
"""pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"
match = re.search(pattern, str)
if match:
    print(match.group())"""
pattern = r"[01]+0$"
str = '011101'
match = re.match(pattern, str)
if match:
    print("match 1")
else:
    print("match 0")