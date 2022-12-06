# vim: ft=python
#!/usr/bin/env python
# -*- coding: utf-8
#
# * -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : solve.py
# Creation Date : 20-12-2008
# Last Modified : Mon 05 Dec 2022 10:55:57 GMT
# Created By : Greg Lyras <greglyras@gmail.com>
# _._._._._._._._._._._._._._._._._._._._._.*/


def uniq(characters):
    return len(characters) == len(set(characters))


def find_marker(datastream, length=4):
    return next(
        (i for i in range(length, len(datastream)) if uniq(datastream[i - length : i])),
        -1,
    )


def day6_1(inpt):
    return sum(find_marker(datastream) for datastream in inpt)


def day6_2(inpt):
    return sum(find_marker(datastream, length=14) for datastream in inpt)


def parse_1(raw):
    return [line.strip() for line in raw]


def main():
    with open("input_6.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day6_1(inpt)
        result_2 = day6_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
