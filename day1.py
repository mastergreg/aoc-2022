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


def day1_1(inpt):
    return max(map(sum, inpt))


def day1_2(inpt):
    s_inpt = sorted(map(sum, inpt), reverse=True)
    return sum(s_inpt[:3])


def parse(raw):
    elflist = []
    current_list = []
    for line in raw:
        try:
            current_list.append(int(line))
        except ValueError:
            elflist.append(current_list)
            current_list = []
    return elflist


def main():
    with open("input_1.txt") as raw:
        inpt = parse(raw)
        result_1 = day1_1(inpt)
        result_2 = day1_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
