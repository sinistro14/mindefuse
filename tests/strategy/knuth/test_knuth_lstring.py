#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


class TestKnuthLString:

    @pytest.mark.parametrize("rounds, secret, solved", [
        (
            16, "abc", True
        ),
    ])
    def test_numeric_knuth(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.KNUTH, secret=secret)
        helper.assert_solved(problem, solved)
