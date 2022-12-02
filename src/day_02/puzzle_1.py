from enum import IntEnum, StrEnum, unique
from typing import Iterator, Optional


@unique
class Shape(StrEnum):
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'


@unique
class GameState(StrEnum):
    win = 'win'
    draw = 'draw'
    lose = 'lose'


@unique
class OpponentShape(StrEnum):
    rock = 'A'
    paper = 'B'
    scissors = 'C'


@unique
class MyShape(StrEnum):
    rock = 'X'
    paper = 'Y'
    scissors = 'Z'


@unique
class ShapePoints(IntEnum):
    rock = 1
    paper = 2
    scissors = 3


@unique
class GameStatePoints(IntEnum):
    lose = 0
    draw = 3
    win = 6


GAME_WINNER: dict[tuple[Shape, Shape], Shape] = {
    (Shape.rock, Shape.scissors): Shape.rock,
    (Shape.scissors, Shape.rock): Shape.rock,
    (Shape.scissors, Shape.paper): Shape.scissors,
    (Shape.paper, Shape.scissors): Shape.scissors,
    (Shape.paper, Shape.rock): Shape.paper,
    (Shape.rock, Shape.paper): Shape.paper,
}


def _check_game_winner(s1: Shape, s2: Shape) -> Optional[Shape]:
    if s1 == s2:
        return None

    return GAME_WINNER[(s1, s2)]


def _calculate_points(shape: Shape, state: GameState) -> int:
    return ShapePoints[shape] + GameStatePoints[state]


def _get_game_state(winner_shape: Optional[Shape], me: Shape) -> GameState:
    if winner_shape is None:
        return GameState.draw
    elif me == winner_shape:
        return GameState.win

    return GameState.lose


def _parse_input(data: str) -> Iterator[tuple[Shape, Shape, int]]:
    round = 0
    for line in data.split('\n'):
        if len(line) == 0:
            continue

        opponent, me = line.split(' ')

        opponent_shape = OpponentShape(opponent)
        my_shape = MyShape(me)

        yield Shape[opponent_shape.name], Shape[my_shape.name], round

        round += 1


def _play_round(opponent: Shape, me: Shape) -> int:
    winner_shape = _check_game_winner(opponent, me)
    game_state = _get_game_state(winner_shape, me)
    return _calculate_points(me, game_state)


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
