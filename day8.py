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


def is_visible(grid, point):
    x, y = point

    return (
        all(grid[y][i] < grid[y][x] for i in range(x))
        or all(grid[y][i] < grid[y][x] for i in range(x + 1, len(grid[y])))
        or all(grid[j][x] < grid[y][x] for j in range(y))
        or all(grid[j][x] < grid[y][x] for j in range(y + 1, len(grid)))
    )


def visibility_right(grid, point):
    x, y = point
    total = 0
    height = grid[y][x]
    for i in range(x + 1, len(grid[y])):
        total += 1
        if grid[y][i] >= height:
            break
    return total


def visibility_left(grid, point):
    x, y = point
    total = 0
    height = grid[y][x]
    for i in range(x - 1, -1, -1):
        total += 1
        if grid[y][i] >= height:
            break
    return total


def visibility_up(grid, point):
    x, y = point
    total = 0
    height = grid[y][x]
    for j in range(y - 1, -1, -1):
        total += 1
        if grid[j][x] >= height:
            break
    return total


def visibility_down(grid, point):
    x, y = point
    total = 0
    height = grid[y][x]
    for j in range(y + 1, len(grid)):
        total += 1
        if grid[j][x] >= height:
            break
    return total


def visibility(grid, point):
    return (
        visibility_left(grid, point)
        * visibility_right(grid, point)
        * visibility_up(grid, point)
        * visibility_down(grid, point)
    )


def day8_1(inpt):
    total = 0
    for y in range(len(inpt)):
        for x in range(len(inpt[y])):
            if is_visible(inpt, (x, y)):
                total += 1

    return total


def day8_2(inpt):
    visibilities = []
    for i in range(len(inpt)):
        for j in range(len(inpt[0])):
            visibilities.append(visibility(inpt, (i, j)))
    return max(visibilities)


def parse_1(raw):
    return [list(map(int, line.strip())) for line in raw]


def main():
    with open("input_8.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day8_1(inpt)
        result_2 = day8_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
