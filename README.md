# pigen
Generates pi to as many digits as you want.

Uses the equation from the beginning of [this video](https://youtu.be/LhlqCJjbEa0), where mathematician Matt Parker calculates pi by hand for Pi Day 2018. The equation used is a variant of the Chudnovsky algorithm. For some reason this variant works better than other variants of the same algorithm that I tried (probably because the square root bit is outside the summation).

## Installation
Just download or clone this repository. You will need Python 3.

## Usage
This only applies to MacOS and probably other Unix-based systems (tested only on Raspbian though).

Double-click `pigen` or `superpigen` to run it. Terminal (or your platform's equivalent) will be opened, and you will be prompted for the number of digits to generate. `superpigen` will show progress reports when generating greater than or equal to 10,000 digits, but is probably slower than `pigen`.

`superpigen` has a parser, so it will also accept arguments when run in the command line. `-d digits` or `--digits digits` will skip the prompt and generate `digits` decimal places. `-s` or `--silent` will skip printing progress reports. `-t kvalue` or `--test kvalue` will test how many digits of pi generated using `kvalue` as the upper bound of the summation used in the algorithm is. You will need to hard code a true pi in the script (put it in the empty string on line 9 of scripts/superpigen.py).
