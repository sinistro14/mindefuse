#!/usr/bin/env python3.7

from ..strategy import Strategy
from ..strategy_types import StrategyTypes


class NullStrategy(Strategy):
    """
    Null strategy
    Used only as a default, as to avoid unnecessarily specific error handling
    """

    _type = StrategyTypes.NULL

    def solve_problem(self, problem):
        pass
