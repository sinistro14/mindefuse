#!/usr/bin/env python3.7

from ..strategy import Strategy
from ..strategy_types import StrategyTypes


class NullStrategy(Strategy):

    _type = StrategyTypes.NULL
