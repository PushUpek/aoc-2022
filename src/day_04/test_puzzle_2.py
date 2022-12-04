import pytest

from src.day_04.puzzle_2 import _how_many_pairs_overlap, _is_range_overlap

from .test_puzzle_1 import INPUT_DATA


@pytest.mark.parametrize(
    'ranges,expected',
    [
        ([[2, 3, 4], [6, 7, 8]], False),
        ([[2, 3], [4, 5]], False),
        ([[5, 6, 7], [7, 8, 9]], True),
        ([[2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]], True),
        ([[6], [4, 5, 6]], True),
        ([[2, 3, 4, 5, 6], [4, 5, 6, 7, 8]], True),
    ],
)
def test_is_range_overlap(ranges, expected):
    assert _is_range_overlap(*ranges) == expected


def test_how_many_pairs_overlap():
    expected_num = 4
    assert _how_many_pairs_overlap(INPUT_DATA) == expected_num
