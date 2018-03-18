#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from decimal import getcontext, Decimal
from math import factorial, ceil


def genPi(places):
    """Generates pi to places decimal places, not counting the leading three.
    (genPi(5) returns 3.14159.)"""
    getcontext().prec = places + 2
    subsum = 0
    # this is determined by a equation that was built using test()
    # plus one for good measure
    maxK = ceil(0.0704225352 * places + 0.126760563) + 1

    # these things are from Matt Parker's video where
    # he calculates pi by hand using the Chudnovsky Algorithm
    for k in range(maxK):
        top = factorial(6 * k) * (545140134 * k + 13591409)
        bottom = factorial(3 * k) * factorial(k)**3 * (-262537412640768000)**k
        subsum += Decimal(str(top)) / Decimal(str(bottom))
    pie = Decimal('426880') * Decimal('10005').sqrt() / subsum
    pie = round(pie, places)
    return pie


def main():
    """This will prompt the user for the number of digits to generate,
    then generate pi with that number of decimal places."""
    digits = int(input('Number of digits to generate: '))
    print(genPi(digits))
    # pause before exiting when not on MacOS
    if sys.platform != 'darwin':
        input('press enter to exit')


if __name__ == '__main__':
    main()
