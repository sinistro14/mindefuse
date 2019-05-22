#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


@pytest.mark.lite
class TestKnuthNumeric:

    @pytest.mark.parametrize("rounds, secret, solved", [
        (12, "5", True),
        (12, "9", True),
        (12, "12", True),
        (12, "37", True),
        (12, "99", True),
        (12, "111", True),
        (12, "456", True),
        (12, "555", True),
        (12, "989", True),
        (12, "999", True),
        (12, "5555", True),
        (12, "9999", True),
    ])
    def test_numeric_hybrid(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.HYBRID, secret=secret)
        helper.assert_solved(problem, solved)
