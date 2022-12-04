import itertools
from typing import Iterable

from .puzzle_1 import Rucksack, _get_priority, _parse_input


def _split_into_groups(
    rucksacks: Iterable[Rucksack],
) -> Iterable[list[Rucksack]]:
    group_size = 3
    while item := list(itertools.islice(rucksacks, group_size)):
        yield item


def _get_badge_of_group(group: list[Rucksack]) -> str:
    items_1, items_2, items_3 = group

    badge = ''
    for item in items_1.all_items():
        if item not in items_2.all_items() or item not in items_3.all_items():
            continue

        badge = item

    return badge


def _sum_of_priorities_for_badge(data: str) -> int:
    rucksucks = _parse_input(data)

    sum_ = 0
    for group in _split_into_groups(rucksucks):
        badge = _get_badge_of_group(group)
        badge_priority = _get_priority(badge)
        sum_ += badge_priority
    return sum_


def _read_input_data(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def main() -> int:
    input_data = _read_input_data('./src/day_03/input_1.txt')
    sum_of_priorities = _sum_of_priorities_for_badge(input_data)
    print(
        f'The sum of the priorities of those item types: {sum_of_priorities}.'
    )

    return 0


if __name__ == '__main__':
    exit(main())
