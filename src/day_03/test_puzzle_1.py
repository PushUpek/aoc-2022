import pytest

from src.day_03.puzzle_1 import (
    Rucksack,
    _find_error,
    _get_priority,
    _parse_input,
    _prioritize_items_rearrangment,
    _split_into_comparmtnets,
    _sum_of_priorities,
)

INPUT_DATA = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('abbd', Rucksack('ab', 'bd')),
        ('abcbd', Rucksack('ab', 'cbd')),
        ('a', Rucksack('', 'a')),
    ],
)
def test_split_into_compartment(test_input, expected):
    assert _split_into_comparmtnets(test_input) == expected


def test_find_errors():
    expected_errors = ['p', 'L', 'P', 'v', 't', 's']

    for idx, rucksack in enumerate(_parse_input(INPUT_DATA)):
        error = _find_error(rucksack.compartment_1, rucksack.compartment_2)
        assert error == expected_errors[idx]


@pytest.mark.parametrize(
    'char,expected_priority',
    [
        ('a', 1),
        ('z', 26),
        ('A', 27),
        ('Z', 52),
    ],
)
def test_priority(char, expected_priority):
    assert _get_priority(char) == expected_priority


@pytest.mark.parametrize(
    'error,expected',
    [
        ('p', ('p', 16)),
        ('L', ('L', 38)),
        ('P', ('P', 42)),
        ('v', ('v', 22)),
        ('t', ('t', 20)),
        ('s', ('s', 19)),
    ],
)
def test_prioritize_items_rearrangment(error, expected):
    assert _prioritize_items_rearrangment(error) == expected


def test_sum_of_priorities():
    expected_sum = 157
    assert _sum_of_priorities(INPUT_DATA) == expected_sum
