import day3


def test_priority():
    assert day3.priority("a") == 1
    assert day3.priority("A") == 27
    assert day3.priority("p") == 16
    assert day3.priority("L") == 38


def test_rucksack_split():
    assert day3.rucksack_split("vJrwpWtwJgWrhcsFMMfFFhFp") == (
        "vJrwpWtwJgWr",
        "hcsFMMfFFhFp",
    )
    assert day3.rucksack_split("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == (
        "jqHRNqRjqzjGDLGL",
        "rsFMfFZSrLrFZsSL",
    )


def test_common():
    assert day3.common("vJrwpWtwJgWr", "hcsFMMfFFhFp") == {"p"}
    assert day3.common("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL") == {"L"}


def test_parse():
    assert day3.parse_1(
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
    ) == [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrV", "vPwwTWBwg"),
        ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"),
        ("ttgJtRGJ", "QctTZtZT"),
        ("CrZsJsPPZsGz", "wwsLwLmpwMDw"),
    ]


def test_day3_1():
    assert (
        day3.day3_1(
            [
                ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
                ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
                ("PmmdzqPrV", "vPwwTWBwg"),
                ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"),
                ("ttgJtRGJ", "QctTZtZT"),
                ("CrZsJsPPZsGz", "wwsLwLmpwMDw"),
            ]
        )
        == 157
    )
