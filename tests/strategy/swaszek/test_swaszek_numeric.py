#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


class TestSwaszekNumeric:

    @pytest.mark.repeat(10)
    @pytest.mark.parametrize("rounds, secret, solved", [
        (12, "456", True),
    ])
    def test_swaszek_consistency(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.SWASZEK, secret=secret)
        helper.assert_solved(problem, solved)

    @pytest.mark.parametrize("rounds, secret, solved", [
        (12, "12", True),
        (12, "37", True),
        (12, "99", True),
        (12, "111", True),
        (12, "456", True),
        (12, "555", True),
        (12, "989", True),
        (12, "999", True),
    ])
    def test_numeric_swaszek(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.SWASZEK, secret=secret)
        helper.assert_solved(problem, solved)
