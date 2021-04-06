"""import re

#pattern = r"gr.y"       #  dot matches any character, other than a new line.
pattern = r"^gr.y$"     #  ^ and $. These match the start and end of a string, respectively
if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")"""

"""import re

pattern = r"[aeiou]"     # Character classes provide a way to match only one of a specific set of characters.
if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rythm myths"):
    print("Match 3")"""

"""import re

pattern = r"[A-Z][A-Z][0-9]"     # Character classes provide a way to match only one of a specific set of characters.
if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "lab"):
    print("Match 3")"""

"""import re

pattern = r"^[A-Z]"     # Character classes provide a way to match only one of a specific set of characters.
if re.match(pattern, "this is all quiet"):
    print("Match 1")

if re.match(pattern, "AbCdEfG123"):
    print("Match 2")

if re.match(pattern, "THISISALLSHOUTING"):
    print("Match 3")"""

import re

pattern = r"egg(spam)*"     # * means "zero or more repetitions of the previous thing".
pattern = r"g+"              # + means "one or more repetitions"
pattern = r"ice(-)?"         #? means "zero or one repetitions".
pattern = r"9{1,3}$"
if re.match(pattern, "gg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")
if re.match(pattern, "ice-cream"):
    print("Match 4")
if re.match(pattern, "icecream"):
    print("Match 5")
if re.match(pattern, "9"):
    print("Match 6")
if re.match(pattern, "999"):
    print("Match 7")
# pattern = r"col(u)?r"     this will detect color or colour