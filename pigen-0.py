#!/usr/bin/env python3

# THIS IS NOT ACCURATE

import argparse
import decimal
from math import ceil, factorial

parser = argparse.ArgumentParser(description='Generate pi')
parser.add_argument('digits', type=int, help='number of digits (excluding the leading 3) to generate')
args = parser.parse_args()


def genPi(Digits):
    """Generate Digits digits (which excludes the leading 3)"""
    decimal.getcontext().prec = Digits + 1
    maxK = ceil(0.0705794 * Digits - 1.01985) + 1
    top, bottom, subsum = None, None, 0      # this may just be my js habits

    for k in range(maxK + 1):
        top = ((-1) ** k) * factorial(6 * k) * (545140134 * k + 13591409)
        bottom = factorial(3 * k) * (factorial(k) ** 3) * round(640320 ** (3 * k + decimal.Decimal('1.5')))
        subsum += decimal.Decimal(str(top)) / decimal.Decimal(str(bottom))
    return (subsum * 12) ** (-1)


print(genPi(args.digits))
