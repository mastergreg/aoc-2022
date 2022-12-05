import day2


def test_solve_1():
    inpt = [
        ["A", "Y"],
        ["B", "X"],
        ["C", "Z"],
    ]
    assert day2.day2_1(inpt) == 15


def test_solve_2():
    inpt = [
        ["A", "Y"],
        ["B", "X"],
        ["C", "Z"],
    ]
    assert day2.day2_2(inpt) == 12
