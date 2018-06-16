#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys
from decimal import getcontext, Decimal
from math import factorial, ceil


def genPi(places, quiet=False, maxK=None):
    """Generates pi to places decimal places, not counting the leading three.
    (genPi(5) returns 3.14159.)
    If quiet is False then it won't show progress reports."""
    getcontext().prec = places + 2
    subsum = 0
    # maxK is usually not set - it's only set when using test()
    if not maxK:
        # this is determined by a equation that was built using test()
        maxK = ceil(0.0714285714 * places + 0.0714285714)

    # these things are from Matt Parker's video where
    # he calculates pi by hand using the Chudnovsky Algorithm
    for k in range(maxK):
        top = factorial(6 * k) * (545140134 * k + 13591409)
        bottom = factorial(3 * k) * factorial(k)**3 * (-262537412640768000)**k
        subsum += Decimal(str(top)) / Decimal(str(bottom))

        # show progress for longer calculations
        # (but not every time and not when quiet)
        if (not quiet) and (places >= 10000) and (k % 50 == 0):
            print('%(k)s/%(maxK)s' % {'k': k, 'maxK': maxK})

    pie = Decimal('426880') * Decimal('10005').sqrt() / subsum
    pie = round(pie, places)
    return pie


def test(kvalues):
    """For testing. Prints how many decimal places kvalues are accurate to
    if kvalues were used for genPi()'s maxK. You must supply your own actualPi,
    which should be a string."""
    actualPi = open('actualPi.txt').read()

    for K in kvalues:
        # generates a pi that is the length of actualPi
        # and has a maxK of what maxK that is being tested
        generatedPi = str(genPi(len(actualPi) - 2, True, K))
        for c in range(1, len(actualPi) + 1):
            # when a digit in generatedPi is not equal to the same digit in
            # actualPi, it will print maxK and where the last accurate place is
            # then move on to the next test
            if generatedPi[c] != actualPi[c]:
                getcontext().prec = 10
                out = '%3s: %4s'
                print(out % (str(K), str(c - 2)))
                # a different output format i want to keep:
                # out = 'k: %3s; places: %4s; diff: % 9.1e; %%error: (% 9.1e)%%'
                # diff = Decimal(actualPi) - Decimal(generatedPi)
                # error = diff / Decimal(actualPi) * 100
                # print(out % (str(K), str(c - 2), diff, error))
                break


def main():
    """This will create a parser and then runs functions appropriately.
    If no arguments are given to the parser, the user will be prompted for the
    number of digits to generate, and a pi will be generated with that many
    decimal places."""
    # create the parser for passing it like a command
    parser = argparse.ArgumentParser(description='Generates pi to as many \
                                     digits as you want.')
    # everything is optional so it can be double clicked
    parser.add_argument('-d', '--digits', type=int, help='Number of digits \
                        (excluding the leading 3) to generate')
    parser.add_argument('-s', '--silent', action='store_true', help="Don't show \
                        progress reports (-d is required for this to work)")
    parser.add_argument('-t', '--test', type=int, action='append', help='Test \
                        the accuracy of maxK values.')
    args = parser.parse_args()

    if args.test:
        test(args.test)
    else:
        # if done as a command
        if args.digits:
            print(genPi(args.digits, args.silent))
        # if double clicked
        else:
            digits = int(input('Number of digits to generate: '))
            print(genPi(digits, args.silent))
            # pause the shell before exiting when not on MacOS (so you can
            # actually see the result)
            if sys.platform != 'darwin':
                input('press enter to exit')


if __name__ == '__main__':
    main()
