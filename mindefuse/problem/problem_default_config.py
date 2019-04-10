#!/usr/bin/env python3.7

from .secret import SecretTypes


class ProblemDefaultConfig:
    """
    Default Problem values
    The values here defined match those of a classic Mastermind game,
    whilst considering numbers instead of colours
    """

    ROUNDS = 12                         # TODO review value
    DEFAULT_TYPE = SecretTypes.COLOR    # TODO review value
    DEFAULT_SIZE = 4                    # TODO review value
    DEFAULT_COLOURS = 6                 # TODO review value
    DEFAULT_SECRET = ""                 # TODO review value
