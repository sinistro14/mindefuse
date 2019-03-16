#!/usr/bin/env python3.7

from enum import Enum, unique, auto


@unique
class StrategyTypes(Enum):
    """
    Types of strategy available to solve a problem
    """
    NULL = auto()
    KNUTH = auto()
    GENETIC = auto()
    SWASZEK = auto()
