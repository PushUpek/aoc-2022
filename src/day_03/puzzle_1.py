import string
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Rucksack:
    compartment_1: str
    compartment_2: str

    def all_items(self) -> str:
        return self.compartment_1 + self.compartment_2


def _split_into_comparmtnets(line: str) -> Rucksack:
    split_point = len(line) // 2
    compartment_1, compartment_2 = line[:split_point], line[split_point:]
    return Rucksack(compartment_1, compartment_2)


def _parse_input(data: str) -> Iterator[Rucksack]:
    for line in data.split('\n'):
        if len(line) == 0:
            continue

        yield _split_into_comparmtnets(line)


def _find_error(compartment_1: str, compartment_2: str) -> str:
    errors = [item for item in compartment_2 if item in compartment_1]
    return errors.pop()


def _get_priority(char: str) -> int:
    offset = 1
    if char.islower():
        return string.ascii_lowercase.index(char) + offset
    else:
        offset += len(string.ascii_lowercase)
        return string.ascii_uppercase.index(char) + offset


def _prioritize_items_rearrangment(error: str) -> tuple[str, int]:
    return error, _get_priority(error)


def _sum_of_priorities(data: str) -> int:
    sum_ = 0
    for rucksuck in _parse_input(data):
        error = _find_error(rucksuck.compartment_1, rucksuck.compartment_2)
        priority = _get_priority(error)
        sum_ += priority
    return sum_


def _read_input_data(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def main() -> int:
    input_data = _read_input_data('./src/day_03/input_1.txt')
    sum_of_priorities = _sum_of_priorities(input_data)
    print(
        f'The sum of the priorities of those item types: {sum_of_priorities}.'
    )

    return 0


if __name__ == '__main__':
    exit(main())
