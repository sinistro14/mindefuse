#!/usr/bin/env python3.7

from enum import IntEnum
from ..secret_types import SecretTypes
from .secret_generator import SecretGenerator


class Color(IntEnum):
    BLUE = 1
    GREEN = 2
    ORANGE = 3
    PURPLE = 4
    RED = 5
    YELLOW = 6


class ColorGenerator(SecretGenerator):
    """
    Generator of original Mastermind color sequences, as numbers from 1 to 6, e.g. 2456
    """

    _type = SecretTypes.COLOR

    _possible_elements = range(len(Color))
