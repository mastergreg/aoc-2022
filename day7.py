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


def day7_1(inpt):
    total = 0
    files, directories = inpt
    for fname, size, path in files:
        for i in range(1, len(path) + 1):
            directories["/".join(path[:i])] += int(size)
    for directory_size in directories.values():
        if directory_size <= 100000:
            total += directory_size
    return total


def day7_2(inpt):
    total = 0
    files, directories = inpt
    fssize = 70000000
    update_size = 30000000
    sizes = sorted(directories.values())
    free_space = fssize - sizes[-1]
    required_cleanup = update_size - free_space
    for size in sizes:
        if size >= required_cleanup:
            total = size
            break

    return total


def parse_1(raw):
    files = []
    directories = {}
    path = []
    for line in raw:
        match line[:4]:
            case "$ ls":
                # skip the ls command
                continue
            case "$ cd":
                folder = line.split()[-1]
                if folder == "..":
                    path.pop()
                else:
                    path.append(folder)
                    directories["/".join(path)] = 0
            case "dir ":
                continue
            case _:
                size, fname = line.split()
                files.append((fname, size, list(path)))
    return files, directories


def main():
    with open("input_7.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day7_1(inpt)
        result_2 = day7_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
