#!/usr/bin/env python
"""
info about project here
"""


import datetime

...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    today = datetime.datetime.now()                                 #datum van vandaag
    leeftijd = int(input("hoe oud ben je? "))
    geboortejaar = int(today.year) - leeftijd                       #voor een geboortejaar heb je geen uren etc nodig
    print("je bent geboren in het jaar " + str(geboortejaar))
    int50jaar = geboortejaar + 100
    print("je wordt 50 in het jaar " + str(int50jaar))


if __name__ == '__main__':  # code to execute if called from command-line
    main()
