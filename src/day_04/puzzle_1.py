from typing import Iterator


def _parse_input(data: str) -> Iterator[list[str]]:
    for line in data.split('\n'):
        if len(line) == 0:
            continue

        yield line.split(',')


def _build_ranges(ranges: list[str]) -> list[list[int]]:
    ranges_ = []
    for range_ in ranges:
        start, end = map(int, range_.split('-'))
        ranges_.append(list(range(start, end + 1)))
    return ranges_


def _is_range_contains(range1: list[int], range2: list[int]) -> bool:
    intersect = sorted(list(set(range1).intersection(range2)))
    if len(intersect) < 1:
        return False
    return range1 == intersect or range2 == intersect


def _how_many_pairs_contains(data: str) -> int:
    counter = 0
    for ranges in _parse_input(data):
        pairs = _build_ranges(ranges)
        if not _is_range_contains(*pairs):
            continue
        counter += 1
    return counter


def _read_input_data(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def main() -> int:
    input_data = _read_input_data('./src/day_04/input_1.txt')
    num = _how_many_pairs_contains(input_data)
    print(f'Assignment pairs that one range fully contain the other: {num}')

    return 0


if __name__ == '__main__':
    exit(main())
