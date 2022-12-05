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


INDEX_MAP = {
    "ROCK": 0,
    "PAPER": 1,
    "SCISSORS": 2,
}

VALUE_MAP = [1, 2, 3]

TRANSLATION_MAP = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

B_WIN_MATRIX = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3],
]

RESULT_MAP = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

ENC_MATRIX = [
    {
        0: 3,
        3: 1,
        6: 2,
    },
    {
        0: 1,
        3: 2,
        6: 3,
    },
    {
        0: 2,
        3: 3,
        6: 1,
    },
]


def calc_score_1(a, b):
    return VALUE_MAP[b] + B_WIN_MATRIX[a][b]


def calc_score_2(a, r):
    return r + ENC_MATRIX[a][r]


def day2_2(inpt):
    return sum(
        calc_score_2(
            TRANSLATION_MAP[_a],
            RESULT_MAP[_b],
        )
        for _a, _b in inpt
    )


def day2_1(inpt):
    return sum(
        calc_score_1(
            TRANSLATION_MAP[_a],
            TRANSLATION_MAP[_b],
        )
        for _a, _b in inpt
    )


def parse(raw):
    return [line.split() for line in raw]


def main():
    with open("input_2.txt") as raw:
        inpt = parse(raw)
        result_1 = day2_1(inpt)
        result_2 = day2_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
