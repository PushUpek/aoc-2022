from .puzzle_1 import _split_by_elfs, _sum_by_elfs
from .puzzle_2 import _top_three_total
from .test_puzzle_1 import INPUT_DATA


def test_top_three_total():
    sum_by_elfs = _sum_by_elfs(_split_by_elfs(INPUT_DATA))
    result = _top_three_total(sum_by_elfs)

    assert isinstance(result, int)
    assert result == 45000
