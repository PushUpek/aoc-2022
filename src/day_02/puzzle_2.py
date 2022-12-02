from enum import StrEnum, unique
from typing import Iterator

from .puzzle_1 import (
    GAME_WINNER,
    GameState,
    OpponentShape,
    Shape,
    _calculate_points,
)


@unique
class ExpectedState(StrEnum):
    lose = 'X'
    draw = 'Y'
    win = 'Z'


def _parse_input(data: str) -> Iterator[tuple[Shape, GameState, int]]:
    round = 0
    for line in data.split('\n'):
        if len(line) == 0:
            continue

        opponent, state = line.split(' ')

        opponent_shape = OpponentShape(opponent)
        state = ExpectedState(state)

        yield Shape[opponent_shape.name], GameState[state.name], round

        round += 1


def _get_my_shape(opponent: Shape, expected_state: GameState) -> Shape:
    if expected_state == GameState.draw:
        return opponent

    if expected_state == GameState.lose:
        combinations = [k for k, v in GAME_WINNER.items() if v == opponent]
    else:
        combinations = [
            k
            for k, v in GAME_WINNER.items()
            if v != opponent and opponent in k
        ]

    candidate_shapes = set()
    for shapes in combinations:
        s1, s2 = shapes
        candidate_shapes.add(s1)
        candidate_shapes.add(s2)
    candidate_shapes.remove(opponent)

    return candidate_shapes.pop()


def _play_round(opponent: Shape, expected_state: GameState) -> int:
    my_shape = _get_my_shape(opponent, expected_state)
    return _calculate_points(my_shape, expected_state)


def _play_game(input_data: str) -> int:
    total_score = 0
    for oponent_shape, my_shape, _ in _parse_input(input_data):
        total_score += _play_round(oponent_shape, my_shape)
    return total_score


def _read_input_data(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def main() -> int:
    input_data = _read_input_data('./src/day_02/input_1.txt')
    total_score = _play_game(input_data)
    print(f'Your total score is {total_score}.')

    return 0


if __name__ == '__main__':
    exit(main())
