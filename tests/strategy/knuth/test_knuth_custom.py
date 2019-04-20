#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


@pytest.mark.custom
class TestKnuthNumeric:

    @pytest.mark.parametrize("rounds, secret, solved", [
        (5, "456", True),
    ])
    def test_numeric_knuth(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.KNUTH, secret=secret)
        helper.assert_solved(problem, solved)
