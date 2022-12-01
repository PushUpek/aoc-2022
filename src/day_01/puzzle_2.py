from .puzzle_1 import (
    _most_calories,
    _read_input_data,
    _split_by_elfs,
    _sum_by_elfs,
)


def _top_three_total(data: dict[int, int]) -> int:
    sum_by_elfs = data.copy()

    top_3 = []
    for _ in range(3):
        elf, total = _most_calories(sum_by_elfs)
        top_3.append((elf, total))
        sum_by_elfs.pop(elf)

    return sum(map(lambda top: top[1], top_3))


def main() -> int:
    input_data = _read_input_data('./src/day_01/input_1.txt')
    sum_by_elfs = _sum_by_elfs(_split_by_elfs(input_data))
    total_top_3 = _top_three_total(sum_by_elfs)

    print(
        f'How many Calories are those Elves carrying in total? {total_top_3}'
    )

    return 0


if __name__ == '__main__':
    exit(main())
