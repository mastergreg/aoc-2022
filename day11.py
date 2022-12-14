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


class Monkey:
    def __init__(self, lines):
        lines = lines.split("\n")
        self.id = int(lines[0].split(":")[0].split()[1])
        self.items = list(map(int, lines[1].split(":")[1].split(",")))
        self.operation = compile(lines[2].split(":")[1].strip(), "<string>", "exec")

        self.test = int(lines[3].split()[-1])
        self.if_true = int(lines[4].split()[-1])
        self.if_false = int(lines[5].split()[-1])
        self.inspections = 0

    def _execute(self, worry):
        self.inspections += 1
        context = {"new": 0, "old": worry}
        exec(self.operation, context)
        worry = context["new"]
        #        worry //= 3
        return worry

    def _test(self, worry):
        return worry % self.test == 0

    def _throw(self, item):
        return self.if_true if self._test(item) else self.if_false

    def round(self, chinese_modulo=None):
        intent = []
        for item in self.items:
            if chinese_modulo is None:
                new_worry = self._execute(item)
            else:
                new_worry = self._execute(item) % chinese_modulo
            intent.append((new_worry, self._throw(new_worry)))
        self.items = []
        return intent

    def receive(self, item):
        self.items.append(item)

    def __repr__(self) -> str:
        return f"ID: {self.id} #items: {len(self.items)}"


class Game:
    def __init__(self, monkeys):
        self.monkeys = monkeys

    def round(self, chinese_modulo=None):
        intent = []
        for monkey in self.monkeys:
            print(monkey)
            intent = monkey.round(chinese_modulo=chinese_modulo)
            for item, recipient in intent:
                self.monkeys[recipient].receive(item)
        inspections = sorted(
            [monkey.inspections for monkey in self.monkeys], reverse=True
        )
        print(f"Top 2 {inspections[0]} * {inspections[1]}")
        return inspections[0] * inspections[1]


def day10_1(inpt):
    game = Game(monkeys=inpt)
    for r in range(20):
        print(f"Round {r}")
        inspections = game.round()
    return inspections


def day10_2(inpt):
    game = Game(monkeys=inpt)
    chinese_modulo = 1
    for monkey in inpt:
        chinese_modulo *= monkey.test
    for r in range(10000):
        print(f"Round {r}")
        inspections = game.round(chinese_modulo=chinese_modulo)
    return inspections


def parse_1(raw):
    inpt = []
    lines = raw.readlines()
    for index in range(0, len(lines), 7):
        monkey_inpt = "".join(lines[index : index + 7])
        monkey = Monkey(monkey_inpt)
        inpt.append(monkey)
    return inpt


def main():
    logging.basicConfig(level=logging.INFO)

    with open("input_11.txt") as raw:
        inpt = parse_1(raw)
        result_1 = day10_1(inpt)
    with open("input_11.txt") as raw:
        inpt = parse_1(raw)
        result_2 = day10_2(inpt)
    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
