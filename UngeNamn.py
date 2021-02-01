för = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "å",
    "ä",
    "ö"
]

efter = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "å",
    "ä",
    "ö"
]

import random
förnamn = ""
efternamn = ""
for i in range(0, 5):
  förval = random.randint(0, len(för)-1)
  förnamn += för[förval]
  efterval = random.randint(0, len(efter)-1)
  efternamn += efter[efterval]

print(förnamn, efternamn)