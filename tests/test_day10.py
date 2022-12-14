import day10


def test_small_1():
    with open("input_10_small.txt") as raw:
        inpt = day10.parse_1(raw)
        assert day10.day10_1(inpt) == 13140


def test_place_sprite():
    assert day10.place_sprite(1) == "###....................................."
    assert day10.place_sprite(16) == "...............###......................"
    assert day10.place_sprite(5) == "....###................................."
    assert day10.place_sprite(11) == "..........###..........................."
    assert day10.place_sprite(8) == ".......###.............................."


def test_small_2():
    with open("input_10_small.txt") as raw:
        inpt = day10.parse_1(raw)
        assert (
            day10.day10_2(inpt)
            == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
        )
