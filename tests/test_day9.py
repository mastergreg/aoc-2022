import day9
from io import StringIO


def test_parse_1():
    raw = StringIO("""R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2""")
    inpt = [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2),
    ]
    assert day9.parse_1(raw) == inpt


def test_day9_1():
    inpt = [
        ("R", "4"),
        ("U", "4"),
        ("L", "3"),
        ("D", "1"),
        ("R", "4"),
        ("D", "1"),
        ("L", "5"),
        ("R", "2"),
    ]
    assert day9.day9_1(inpt) == 13


def test_integer_distance():
    assert day9.integer_distance((1, 1), (1, 1)) == 0
    assert day9.integer_distance((0, 1), (1, 1)) == 1
    assert day9.integer_distance((1, 0), (1, 1)) == 1
    assert day9.integer_distance((0, 0), (1, 1)) == 1
    assert day9.integer_distance((2, 1), (1, 1)) == 1
    assert day9.integer_distance((1, 2), (1, 1)) == 1
    assert day9.integer_distance((2, 2), (1, 1)) == 1
    assert day9.integer_distance((0, 0), (2, 2)) == 0


def test_calculate_move():
    assert day9.calculate_move((0, 0), ("R", 4)) == [(1, 0), (2, 0), (3, 0), (4, 0)]
    assert day9.calculate_move((4, 1), ("L", 4)) == [(3, 1), (2, 1), (1, 1), (0, 1)]
    assert day9.calculate_move((4, 1), ("U", 3)) == [(4, 2), (4, 3), (4, 4)]
    assert day9.calculate_move((3, 7), ("D", 3)) == [(3, 6), (3, 5), (3, 4)]


def test_follow_move():
    tail = (0, 0)
    moves = [(1, 0), (2, 0), (3, 0), (4, 0)]
    assert day9.follow_move(tail, moves) == [(0, 0), (1, 0), (2, 0), (3, 0)]
    tail = (5, 1)
    moves = [(3, 1), (2, 1), (1, 1), (0, 1)]
    assert day9.follow_move(tail, moves) == [(5, 1), (4, 1), (3, 1), (2, 1), (1, 1)]


def test_small_1():
    with open("input_9_small.txt") as raw:
        inpt = day9.parse_1(raw)
        assert day9.day9_1(inpt) == 13


def test_small_2():
    with open("input_9_2_small.txt") as raw:
        inpt = day9.parse_1(raw)
        assert day9.day9_2(inpt) == 36
