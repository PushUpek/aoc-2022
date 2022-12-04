import pytest

from src.day_04.puzzle_1 import (
    _build_ranges,
    _how_many_pairs_contains,
    _is_range_contains,
)

INPUT_DATA = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@pytest.mark.parametrize(
    'ranges,expected',
    [
        (['2-4', '6-8'], [[2, 3, 4], [6, 7, 8]]),
        (['2-3', '4-5'], [[2, 3], [4, 5]]),
        (['5-7', '7-9'], [[5, 6, 7], [7, 8, 9]]),
        (['2-8', '3-7'], [[2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]]),
        (['6-6', '4-6'], [[6], [4, 5, 6]]),
        (['2-6', '4-8'], [[2, 3, 4, 5, 6], [4, 5, 6, 7, 8]]),
    ],
)
def test_build_ranges(ranges, expected):
    assert _build_ranges(ranges) == expected


@pytest.mark.parametrize(
    'ranges,expected',
    [
        ([[2, 3, 4], [6, 7, 8]], False),
        ([[2, 3], [4, 5]], False),
        ([[5, 6, 7], [7, 8, 9]], False),
        ([[2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]], True),
        ([[6], [4, 5, 6]], True),
        ([[2, 3, 4, 5, 6], [4, 5, 6, 7, 8]], False),
        (
            [
                [
                    40,
                    41,
                    42,
                    43,
                    44,
                    45,
                    46,
                    47,
                    48,
                    49,
                    50,
                    51,
                    52,
                    53,
                    54,
                    55,
                    56,
                    57,
                    58,
                    59,
                    60,
                    61,
                    62,
                    63,
                    64,
                    65,
                    66,
                    67,
                    68,
                    69,
                    70,
                    71,
                    72,
                    73,
                    74,
                    75,
                    76,
                    77,
                    78,
                ],
                [
                    58,
                    59,
                    60,
                    61,
                    62,
                    63,
                    64,
                    65,
                    66,
                    67,
                    68,
                    69,
                    70,
                    71,
                    72,
                    73,
                    74,
                ],
            ],
            True,
        ),
    ],
)
def test_is_range_contains(ranges, expected):
    assert _is_range_contains(*ranges) is expected


def test_how_many_pairs_contains():
    expected_result = 2
    assert _how_many_pairs_contains(INPUT_DATA) == expected_result
