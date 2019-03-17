#!/usr/bin/env python3.7

import secrets
from typing import List


class SequenceGenerator:
    """
    Sequence generator
    """

    @staticmethod
    def generate(sequence_size: int, possible_elements: List) -> str:
        """
        Given the intended sequence size and possible elements, generates a sequence
        :param sequence_size: size of the sequence
        :param possible_elements: possible elements
        :return: requested string sequence
        """
        possible_elements = [str(i) for i in possible_elements]
        return "".join(secrets.choice(possible_elements) for _ in range(sequence_size))
