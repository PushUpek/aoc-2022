from .puzzle_1 import _most_calories, _split_by_elfs, _sum_by_elfs

INPUT_DATA = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_should_split_by_elfs():
    result = _split_by_elfs(INPUT_DATA)

    assert isinstance(result, dict)
    assert result[1] == [1000, 2000, 3000]
    assert result[2] == [4000]
    assert result[3] == [5000, 6000]
    assert result[4] == [7000, 8000, 9000]
    assert result[5] == [10000]


def test_sum():
    caloreis_by_elfs = _split_by_elfs(INPUT_DATA)
    result = _sum_by_elfs(caloreis_by_elfs)

    assert isinstance(result, dict)
    assert result[1] == 6000
    assert result[2] == 4000
    assert result[3] == 11000
    assert result[4] == 24000
    assert result[5] == 10000


def test_pick_most_calories():
    sum_by_elfs = _sum_by_elfs(_split_by_elfs(INPUT_DATA))
    result = _most_calories(sum_by_elfs)

    assert isinstance(result, tuple)
    assert result == (4, 24000)
