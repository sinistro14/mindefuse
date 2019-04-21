#!/usr/bin/env python3.7

from .secret import SecretTypes


class ProblemDefaultConfig:
    """
    Default Problem values
    The values here defined match those of a classic Mastermind game,
    whilst considering numbers instead of colours
    """
    ROUNDS = 12
    DEFAULT_TYPE = SecretTypes.NUMERIC
    DEFAULT_SIZE = 4
    DEFAULT_COLOURS = 6
    DEFAULT_SECRET = ""
