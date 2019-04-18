#!/usr/bin/env python3.7

from typing import List, Tuple
from collections import Counter


class Secret:
    """
    Representation of a secret sequence
    """

    """list of all possible elements for this type of Secret"""
    possible_elements = List[str]

    """number of elements in this secret"""
    elements = int

    """number of possible types of an element in the sequence"""
    types = int

    """secret sequence"""
    sequence = str

    def __init__(self, possible_elements, elements, types, sequence):
        self.possible_elements = possible_elements
        self.elements = elements
        self.types = types
        self.sequence = sequence

    @staticmethod
    def compare_sequences(sequence: str, proposal: str) -> Tuple[int, int]:
        """
        Compare the proposed sequence with the a sequence
        :param sequence: correct sequence
        :param proposal: sequence proposed as the correct sequence
        :return: tuple with number of whites and number of reds
        """
        assert isinstance(sequence, str) and isinstance(proposal, str) and len(sequence) == len(proposal)

        # convert string to list of chars
        aux_secret = list(sequence)
        aux_proposal = list(proposal)

        # count number of chars
        secret_count = Counter(aux_secret)
        proposal_count = Counter(aux_proposal)

        # count all reds
        reds = sum(secret_val == seq_val for secret_val, seq_val in zip(aux_secret, aux_proposal))

        # count all whites
        whites = sum(min(val, proposal_count.get(k, 0)) for k, val in secret_count.items()) - reds

        return whites, reds

    def compare(self, proposal: str) -> Tuple[int, int]:
        """
        Compare the proposed sequence with the secret sequence
        :param proposal: sequence proposed as the correct secret sequence
        :return: tuple with number of whites and number of reds
        """
        return self.compare_sequences(self.sequence, proposal)
