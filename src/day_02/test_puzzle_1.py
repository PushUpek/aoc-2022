from src.day_02.puzzle_1 import (
    GameState,
    Shape,
    _calculate_points,
    _check_game_winner,
    _get_game_state,
    _parse_input,
    _play_game,
    _play_round,
)

INPUT_DATA = """
A Y
B X
C Z
"""


def test_game_rules_rock_wins():
    assert _check_game_winner(Shape.rock, Shape.scissors) == Shape.rock
    assert _check_game_winner(Shape.scissors, Shape.rock) == Shape.rock


def test_game_rules_scissors_wins():
    assert _check_game_winner(Shape.paper, Shape.scissors) == Shape.scissors
    assert _check_game_winner(Shape.scissors, Shape.paper) == Shape.scissors


def test_game_rules_paper_wins():
    assert _check_game_winner(Shape.paper, Shape.rock) == Shape.paper
    assert _check_game_winner(Shape.rock, Shape.paper) == Shape.paper


def test_game_rules_draw():
    assert _check_game_winner(Shape.rock, Shape.rock) is None
    assert _check_game_winner(Shape.scissors, Shape.scissors) is None
    assert _check_game_winner(Shape.paper, Shape.paper) is None


def test_calculate_points():
    assert _calculate_points(Shape.rock, GameState.win) == 7
    assert _calculate_points(Shape.rock, GameState.draw) == 4
    assert _calculate_points(Shape.rock, GameState.lose) == 1
    assert _calculate_points(Shape.scissors, GameState.win) == 9
    assert _calculate_points(Shape.scissors, GameState.draw) == 6
    assert _calculate_points(Shape.scissors, GameState.lose) == 3
    assert _calculate_points(Shape.paper, GameState.win) == 8
    assert _calculate_points(Shape.paper, GameState.draw) == 5
    assert _calculate_points(Shape.paper, GameState.lose) == 2


def test_get_game_state():
    assert _get_game_state(None, Shape.rock) == GameState.draw
    assert _get_game_state(None, Shape.scissors) == GameState.draw
    assert _get_game_state(None, Shape.paper) == GameState.draw
    assert _get_game_state(Shape.paper, Shape.rock) == GameState.lose
    assert _get_game_state(Shape.paper, Shape.scissors) == GameState.lose
    assert _get_game_state(Shape.rock, Shape.paper) == GameState.lose
    assert _get_game_state(Shape.rock, Shape.scissors) == GameState.lose
    assert _get_game_state(Shape.paper, Shape.rock) == GameState.lose
    assert _get_game_state(Shape.paper, Shape.scissors) == GameState.lose
    assert _get_game_state(Shape.rock, Shape.rock) == GameState.win
    assert _get_game_state(Shape.scissors, Shape.scissors) == GameState.win
    assert _get_game_state(Shape.paper, Shape.paper) == GameState.win


def test_play_round():
    my_scores = [8, 1, 6]
    for opponent_shape, my_shape, round in _parse_input(INPUT_DATA):
        assert _play_round(opponent_shape, my_shape) == my_scores[round]


def test_play_game():
    expected_total_score = 15

    assert _play_game(INPUT_DATA) == expected_total_score
