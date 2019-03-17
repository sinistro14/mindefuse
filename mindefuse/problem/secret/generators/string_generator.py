#!/usr/bin/env python3.7

import string
from ..secret_types import SecretTypes
from .secret_generator import SecretGenerator


class StringGenerator(SecretGenerator):
    """
    Generator of lower and upper case string sequences, e.g. aBcD
    """

    _type = SecretTypes.STRING

    _possible_elements = list(string.ascii_letters)
