from heuristics.greedy_coin import greedy_coin


def test_coin():
    result = greedy_coin(99)
    assert result[25] == 3