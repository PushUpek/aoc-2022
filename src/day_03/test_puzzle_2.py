import pytest

from src.day_03.puzzle_1 import Rucksack, _parse_input
from src.day_03.puzzle_2 import (
    _get_badge_of_group,
    _split_into_groups,
    _sum_of_priorities_for_badge,
)

from .test_puzzle_1 import INPUT_DATA


def test_split_into_groups():
    data = iter(
        [
            Rucksack('ab1', 'ba1'),
            Rucksack('ab2', 'ba2'),
            Rucksack('ab3', 'ba3'),
            Rucksack('cd1', 'dc1'),
            Rucksack('cd2', 'dc2'),
            Rucksack('cd3', 'dc3'),
        ]
    )

    expected_groups = [
        [
            Rucksack('ab1', 'ba1'),
            Rucksack('ab2', 'ba2'),
            Rucksack('ab3', 'ba3'),
        ],
        [
            Rucksack('cd1', 'dc1'),
            Rucksack('cd2', 'dc2'),
            Rucksack('cd3', 'dc3'),
        ],
    ]

    for idx, group in enumerate(_split_into_groups(data)):
        assert group == expected_groups[idx]


@pytest.mark.parametrize(
    'group,expected_badge',
    [
        (
            [
                Rucksack('ac1', 'ba4'),
                Rucksack('ac2', 'ba5'),
                Rucksack('ac3', 'ba6'),
            ],
            'a',
        ),
        (
            [
                Rucksack('ce1', 'dc4'),
                Rucksack('ce2', 'dc5'),
                Rucksack('ce3', 'dc6'),
            ],
            'c',
        ),
    ],
)
def test_get_badge_of_group(group, expected_badge):
    assert _get_badge_of_group(group) == expected_badge


def test_sum_priorities_for_badge():
    expected_sum = 70
    assert _sum_of_priorities_for_badge(INPUT_DATA) == expected_sum
