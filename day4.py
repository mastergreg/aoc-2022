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


def day4_1(inpt):
    total = 0
    for elf_a, elf_b in inpt:
        if contained(elf_a, elf_b):
            total += 1
    return total


def day4_2(inpt):
    total = 0
    for elf_a, elf_b in inpt:
        if overlaps(elf_a, elf_b):
            total += 1
    return total


def a_contains_b(rng_a, rng_b):
    s_a, e_a = rng_a
    s_b, e_b = rng_b
    return s_b >= s_a and e_b <= e_a


def is_in(rng, sector):
    start, end = rng
    return sector >= start and sector <= end


def overlaps(rng_a, rng_b):
    s_a, e_a = rng_a
    s_b, e_b = rng_b
    return (
        is_in(rng_a, s_b) or is_in(rng_a, e_b) or is_in(rng_b, s_a) or is_in(rng_b, e_a)
    )


def contained(rng_1, rng_2):
    return a_contains_b(rng_1, rng_2) or a_contains_b(rng_2, rng_1)


def gen_range(elf_assignment):
    start, end = elf_assignment.split("-")
    return (int(start), int(end))


def parse_1(raw):
    inpt = []
    for line in raw:
        _elf_a, _elf_b = line.strip().split(",")
        elf_a = gen_range(_elf_a)
        elf_b = gen_range(_elf_b)
        inpt.append((elf_a, elf_b))
    return inpt


def main():
    with open("input_4.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day4_1(inpt)
        result_2 = day4_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
