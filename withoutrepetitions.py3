#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/173'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
    if not line:
        continue
    charlast=False
    out=''
    for char in line:
        if char != charlast:
            out += char
        charlast = char
    print(out)
