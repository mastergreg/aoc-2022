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


class WrongStateException(Exception):
    pass


def integer_distance(point_a, point_b):
    """Will be 0 if the points are identical, 1 if they are next to each other
    or 2 if they are further appart.
    """
    if point_a == point_b:
        return 0
    ax, ay = point_a
    bx, by = point_b
    return 2 if abs(ax - bx) > 1 or abs(ay - by) > 1 else 1


def calculate_move(point, instruction):
    moves = []
    command, repeats = instruction
    for _ in range(repeats):
        x, y = point
        match command:
            case "R":
                point = (x + 1, y)
                moves.append(point)
            case "L":
                point = (x - 1, y)
                moves.append(point)
            case "U":
                point = (x, y + 1)
                moves.append(point)
            case "D":
                point = (x, y - 1)
                moves.append(point)
    return moves


def follow_move(tail, moves):
    follows = [tuple(tail)]
    for head in moves:
        ax, ay = tail
        bx, by = head
        difference = (abs(bx - ax), abs(by - ay))
        match difference:
            case (0, 0):
                pass
            case (0, 1):
                pass
            case (0, 2):
                ay = by - 1 if by > ay else by + 1
            case (1, 0):
                pass
            case (1, 1):
                pass
            case (1, 2):
                ay = by - 1 if by > ay else by + 1
                ax = bx
            case (2, 0):
                ax = bx - 1 if bx > ax else bx + 1
            case (2, 1):
                ax = bx - 1 if bx > ax else bx + 1
                ay = by
            case (2, 2):
                ax = bx - 1 if bx > ax else bx + 1
                ay = by - 1 if by > ay else by + 1
            case _:
                logging.critical(f"Ummm? {difference}")
        tail = (ax, ay)
        follows.append(tail)
    return follows


def day9_1(inpt):
    total_moves = []
    head = (0, 0)
    tail = (0, 0)
    for instruction in inpt:
        moves = calculate_move(head, instruction)
        total_moves.extend(moves)
        head = moves[-1]
    follows = follow_move(tail, total_moves)
    return len(set(follows))


def day9_2(inpt):
    head = (0, 0)
    tail = (0, 0)
    length = 10
    head_moves = []
    for instruction in inpt:
        moves = calculate_move(head, instruction)
        head_moves.extend(moves)
        head = moves[-1]
    current_moves = head_moves
    for _ in range(9):
        follows = follow_move(tail, current_moves)
        current_moves = list(follows)
    return len(set(follows))


def parse_1(raw):
    inpt = []
    for line in raw:
        command, repeats_s = line.split()
        repeats = int(repeats_s)
        inpt.append((command, repeats))
    return inpt


def main():
    logging.basicConfig(level=logging.INFO)

    with open("input_9.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day9_1(inpt)
        result_2 = day9_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
