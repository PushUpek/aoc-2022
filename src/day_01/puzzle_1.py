def _read_input_data(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def _split_by_elfs(input_data: str) -> dict[int, list[int]]:
    elfs = {}

    for idx, calories in enumerate(input_data.split('\n\n'), start=1):
        elfs[idx] = [
            int(calorie)
            for calorie in calories.split('\n')
            if len(calorie) > 0
        ]

    return elfs


def _sum_by_elfs(data: dict[int, list[int]]) -> dict[int, int]:
    return {num: sum(calories) for num, calories in data.items()}


def _most_calories(data: dict[int, int]) -> tuple[int, int]:
    elf, max_ = 0, 0
    for num, calories in data.items():
        if max_ < calories:
            max_ = calories
            elf = num

    return elf, max_


def main() -> int:
    input_data = _read_input_data('./src/day_01/input_1.txt')
    sum_by_elfs = _sum_by_elfs(_split_by_elfs(input_data))
    _, most_calories = _most_calories(sum_by_elfs)
    print(f'How many total Calories is that Elf carrying? {most_calories}')

    return 0


if __name__ == '__main__':
    exit(main())
