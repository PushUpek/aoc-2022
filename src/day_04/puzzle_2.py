from src.day_04.puzzle_1 import _build_ranges, _parse_input


def _is_range_overlap(range1: list[int], range2: list[int]) -> bool:
    intersect = set(range1).intersection(range2)
    if len(intersect) < 1:
        return False
    return True


def _how_many_pairs_overlap(data: str) -> int:
    counter = 0
    for ranges in _parse_input(data):
        pairs = _build_ranges(ranges)
        if not _is_range_overlap(*pairs):
            continue
        counter += 1
    return counter


def _read_input_data(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def main() -> int:
    input_data = _read_input_data('./src/day_04/input_1.txt')
    num = _how_many_pairs_overlap(input_data)
    print(f'Assignment pairs that one range overlap the other: {num}')

    return 0


if __name__ == '__main__':
    exit(main())
