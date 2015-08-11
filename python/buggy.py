#!/usr/bin/env python
import sys

def foo():
    a = 1
    b = 2
    c = 1+b
    d = 4-c
    e = 1 - d/0.25
    f = 13.23 / (e + 3)
    g = f / 34
    r = g + 2 + 4 + + 100
    sys.stdout.write("And the answer is {}\n".format(r))

try:
    foo()
except:
    sys.stdout.write("*** Uh uh, this script failed, and the reason is hidden by this try/except ***\n")
