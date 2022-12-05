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


def day5_1(inpt):
    crane_map, instructions = inpt
    for instruction in instructions:
        move(crane_map, instruction)
    answer = [stack[-1] for stack in crane_map]
    return "".join(answer)


def day5_2(inpt):
    crane_map, instructions = inpt
    for instruction in instructions:
        move_advanced(crane_map, instruction)
    answer = [stack[-1] for stack in crane_map]
    return "".join(answer)


def parse_crane_map(raw):
    crane_map = [[] for _ in range(9)]
    for line in raw:
        for index in range(1, len(line), 4):
            if line[index].isalpha():
                crane_map[index // 4].append(line[index])
            elif line[index].isnumeric():
                for i in range(9):
                    crane_map[i].reverse()
                return crane_map


def move_advanced(crane_map, instruction):
    rep, a, b = instruction
    stack = crane_map[a - 1]
    destination = b - 1
    movable_slice = stack[len(stack) - rep :]
    crane_map[a - 1] = stack[: len(stack) - rep]
    crane_map[b - 1].extend(movable_slice)


def move(crane_map, instruction):
    a, b = instruction
    t = crane_map[a - 1].pop()
    crane_map[b - 1].append(t)


def parse_instructions_simple(raw):
    instructions = []
    for line in raw:
        _, repeat, _, src, _, dst = line.split()
        instructions.extend((int(src), int(dst)) for _ in range(int(repeat)))
    return instructions


def parse_instructions_advanced(raw):
    instructions = []
    for line in raw:
        _, repeat, _, src, _, dst = line.split()
        instructions.append((int(repeat), int(src), int(dst)))
    return instructions


def parse_1(raw):
    crane_map = parse_crane_map(raw)
    # skip the empty line
    raw.readline()
    instructions = parse_instructions_simple(raw)
    return crane_map, instructions


def parse_2(raw):
    crane_map = parse_crane_map(raw)
    # skip the empty line
    raw.readline()
    instructions = parse_instructions_advanced(raw)
    return crane_map, instructions


def main():
    with open("input_5.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day5_1(inpt)
    print(result_1)
    with open("input_5.txt") as raw:
        inpt = parse_2(raw)
        result_2 = day5_2(inpt)
    print(result_2)


if __name__ == "__main__":
    main()
