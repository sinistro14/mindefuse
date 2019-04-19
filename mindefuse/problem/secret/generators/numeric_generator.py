#!/usr/bin/env python3.7

from ..secret_types import SecretTypes
from .secret_generator import SecretGenerator


class NumericGenerator(SecretGenerator):
    """
    Generator of numeric sequences, e.g. 1234
    """

    _type = SecretTypes.NUMERIC

    _possible_elements = [str(n) for n in range(0, 10)]
