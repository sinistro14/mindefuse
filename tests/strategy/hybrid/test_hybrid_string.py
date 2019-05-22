#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


class TestKnuthLString:

    @pytest.mark.parametrize("rounds, secret, solved", [
        (30, "aBc", True),
    ])
    def test_numeric_hybrid(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.HYBRID, secret=secret)
        helper.assert_solved(problem, solved)
