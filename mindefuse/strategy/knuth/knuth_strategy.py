#!/usr/bin/env python3.7

from ..strategy import Strategy
from ..strategy_types import StrategyTypes


class KnuthStrategy(Strategy):
    """
    Knuth strategy
    """

    _type = StrategyTypes.KNUTH

    def solve(self, problem):
        pass
