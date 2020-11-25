#!/usr/bin/env python
"""
info about project here
"""

import time

...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():

    starttijd = time.time()
    print(starttijd)
    input("druk enter om te stoppen")
    print("de stopwatch is gestopt")
    stoptijd = time.time()
    loopduur = stoptijd - starttijd
    print("je hebt gelopen voor "+str(loopduur)+" seconden")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
