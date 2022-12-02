from src.day_02.puzzle_1 import GameState, Shape
from src.day_02.puzzle_2 import (
    _get_my_shape,
    _parse_input,
    _play_game,
    _play_round,
)

from .test_puzzle_1 import INPUT_DATA


def test_get_my_shape():
    assert _get_my_shape(Shape.rock, GameState.win) == Shape.paper
    assert _get_my_shape(Shape.scissors, GameState.win) == Shape.rock
    assert _get_my_shape(Shape.paper, GameState.win) == Shape.scissors
    assert _get_my_shape(Shape.rock, GameState.lose) == Shape.scissors
    assert _get_my_shape(Shape.scissors, GameState.lose) == Shape.paper
    assert _get_my_shape(Shape.paper, GameState.lose) == Shape.rock


def test_play_round():
    my_scores = [4, 1, 7]
    for opponent_shape, expected_state, round in _parse_input(INPUT_DATA):
        assert _play_round(opponent_shape, expected_state) == my_scores[round]


def test_play_game():
    expected_total_score = 12

    assert _play_game(INPUT_DATA) == expected_total_score
