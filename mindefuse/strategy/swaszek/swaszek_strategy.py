#!/usr/bin/env python3.7

from ..strategy import Strategy
from ..strategy_types import StrategyTypes


class SwaszekStrategy(Strategy):
    """
    Swaszek strategy
    """

    _type = StrategyTypes.SWASZEK

    def solve(self, problem):
        pass
