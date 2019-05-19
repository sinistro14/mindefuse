#!/usr/bin/env python3.7

from typing import List, Tuple
from collections import Counter

from .secret_types import SecretTypes


class Secret:
    """
    Representation of a secret sequence
    """

    """list of all possible elements for this type of Secret"""
    possible_elements = List[str]

    """number of elements in this secret"""
    elements = int

    """type of secret"""
    type = str

    """number of possible types of an element in the sequence"""
    types = SecretTypes

    """secret sequence"""
    sequence = str

    """number of times that each element in the secret sequence appears"""
    __counted_elements = Counter

    def __init__(self, possible_elements, elements, secret_type, types, sequence):
        self.possible_elements = possible_elements
        self.elements = elements
        self.type = secret_type
        self.types = types
        self.sequence = sequence
        self.__counted = Counter(self.sequence)  # saves some computation when checking guesses

    @staticmethod
    def compare_sequences(sequence: str, proposal: str) -> Tuple[int, int]:
        """
        Compare the proposed sequence with the a sequence
        :param sequence: correct sequence
        :param proposal: sequence proposed as the correct sequence
        :return: tuple with number of whites and number of reds
        """
        assert isinstance(sequence, str) and isinstance(proposal, str) and len(sequence) == len(proposal)

        # count all reds
        reds = sum(secret_val == seq_val for secret_val, seq_val in zip(sequence, proposal))

        # count number of chars
        secret_count = Counter(sequence)
        proposal_count = Counter(proposal)

        # count all whites
        return sum(min(value, proposal_count.get(char, 0)) for char, value in secret_count.items()) - reds, reds

    def compare(self, proposal: str) -> Tuple[int, int]:
        """
        Compare the proposed sequence with the secret sequence
        :param proposal: sequence proposed as the correct secret sequence
        :return: tuple with number of whites and number of reds
        """

        assert isinstance(proposal, str) and self.elements == len(proposal)

        # count all reds
        reds = sum(secret_val == seq_val for secret_val, seq_val in zip(self.sequence, proposal))

        # count number of chars
        proposal_count = Counter(proposal)

        # count all whites
        return sum(min(value, proposal_count.get(char, 0)) for char, value in self.__counted.items()) - reds, reds
