#! usr/bin/env python3.7

import pytest
from mindefuse.strategy import StrategyTypes


class TestGeneticNumeric:

    @pytest.mark.parametrize("rounds, secret, solved", [
        (12, "456", True),
    ])
    def test_numeric_genetic(self, helper, mindefuse, rounds, secret, solved):
        problem = mindefuse.solve_problem(rounds=rounds, algorithm=StrategyTypes.GENETIC, secret=secret)
        helper.assert_solved(problem, solved)
