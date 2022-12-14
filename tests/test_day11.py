import day11


def test_monkey_execute():
    lines = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
"""
    monkey = day11.Monkey(lines)
    assert monkey.round() == [(500, 3), (620, 3)]

    lines = """Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0
"""
    monkey = day11.Monkey(lines)
    assert monkey.round() == [(20, 0), (23, 0), (27, 0), (26, 0)]
