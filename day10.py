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
import logging


def execute_instruction(register, cycle, inst, arg=None):
    match inst:
        case "noop":
            execute_noop(register, cycle)
            return cycle + 1
        case "addx":
            execute_addx(register, cycle, arg)
            return cycle + 2
        case _:
            logging.critical(f"This is bad: {inst}")


def execute_noop(register, cycle):
    x = register[cycle]
    cycle += 1
    register[cycle] = x


# TODO Rename this here and in `execute_instruction`
def execute_addx(register, cycle, arg):
    x = register[cycle]
    cycle += 1
    register[cycle] = x
    x += arg
    cycle += 1
    register[cycle] = x


def day10_1(inpt):
    register = {1: 1}
    cycle = 1
    for instruction, arg in inpt:
        cycle = execute_instruction(register, cycle, instruction, arg)
    keys = [20, 60, 100, 140, 180, 220]
    return sum(key * register[key] for key in keys)


def place_sprite(sprite_pos):
    return ["."] * (sprite_pos - 1) + ["#", "#", "#"] + ["."] * (40 - sprite_pos - 2)


def day10_2(inpt):
    register = {1: 1}
    cycle = 1
    screen = [40 * ["."] for _ in range(6)]
    for instruction, arg in inpt:
        cycle = execute_instruction(register, cycle, instruction, arg)
    for cycle in range(240):
        sprite_pos = register[cycle + 1] % 40
        sprite_mask = place_sprite(sprite_pos)

        row, pos = divmod(cycle, 40)
        screen[row][pos] = sprite_mask[pos]
    return "\n".join(("".join(row)) for row in screen)


def parse_1(raw):
    inpt = []
    for line in raw:
        try:
            instruction, arg_s = line.split()
            arg = int(arg_s)
        except ValueError:
            instruction = line.split()[0]
            arg = None
        inpt.append((instruction, arg))
    return inpt


def main():
    logging.basicConfig(level=logging.INFO)

    with open("input_10.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day10_1(inpt)
        result_2 = day10_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
