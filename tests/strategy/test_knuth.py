#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


class TestKnuth:

    @pytest.mark.skip(reason="still not outputting a testable value")
    @pytest.mark.parametrize("rounds, secret, expected", [
        (
            12, "456",
            (
                "456",
            )
        ),
    ])
    def test_knuth(self, helper, mindefuse, rounds, secret, expected):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.KNUTH, secret=secret)
        helper.assert_knuth(problem.history, expected)
