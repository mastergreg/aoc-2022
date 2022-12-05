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
import functools
from tkinter import W


def priority(item):
    asci = ord(item)
    if asci >= 97:
        return asci - ord("a") + 1
    return asci - ord("A") + 27


def rucksack_split(inpt):
    return (inpt[: len(inpt) // 2], inpt[len(inpt) // 2 :])


def common(l_a, l_b):
    return set(l_a).intersection(set(l_b))


def day3_1(inpt):
    total = 0
    common_item_sets = (common(l_a, l_b) for l_a, l_b in inpt)
    for common_item_set in common_item_sets:
        for common_item in common_item_set:
            total += priority(common_item)
    return total


def group_in_3(inpt):
    for i in range(0, len(inpt), 3):
        yield inpt[i : i + 3]


def day3_2(inpt):
    total = 0
    triplets = list(group_in_3(inpt))
    for t_1, t_2, t_3 in triplets:
        badge = common(common(t_1, t_2), t_3)
        total += priority(list(badge)[0])
    return total


def parse_1(raw):
    return [rucksack_split(inpt) for inpt in raw]


def parse_2(raw):
    return [line.strip() for line in raw]


def main():
    with open("input_3.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day3_1(inpt)
    with open("input_3.txt") as raw:
        inpt = parse_2(raw)
        result_2 = day3_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
