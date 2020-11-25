#!/usr/bin/env python
"""
info about project here
"""


...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    getal1 = int(input("geef een natuurlijk getal"))
    getal2 = int(input("nu nog een alstublieft"))
    operator = input("wil je optellen(+) aftrekken(-) delen(/) of vermenigvuldigen(*)")
    if operator == '+':
        print(getal1 + getal2)

    elif operator == '-':
        print(getal1 - getal2)

    elif operator == '*':
        print(getal1 * getal2)

    elif operator == '/':
        print(getal1 / getal2)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
