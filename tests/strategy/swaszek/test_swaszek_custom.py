#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


@pytest.mark.custom
class TestSwaszekNumeric:

    @pytest.mark.parametrize("rounds, secret, solved", [
        (12, "456", True),
    ])
    def test_custom_swaszek(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.SWASZEK, secret=secret)
        helper.assert_solved(problem, solved)
