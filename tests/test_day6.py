import day6


def test_uniq():
    assert day6.uniq("bvwb") == False
    assert day6.uniq("vwbj") == True


def test_find_marker():
    assert day6.find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert day6.find_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert day6.find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert day6.find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_find_message_marker():
    assert day6.find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert day6.find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert day6.find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
