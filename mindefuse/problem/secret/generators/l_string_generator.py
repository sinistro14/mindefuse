#!/usr/bin/env python3.7

import string
from ..secret_types import SecretTypes
from .secret_generator import SecretGenerator


class LStringGenerator(SecretGenerator):
    """
    Generator of lower case string sequences, e.g. abcd
    """

    _type = SecretTypes.LSTRING

    _possible_elements = list(string.ascii_lowercase)
