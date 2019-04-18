#!/usr/bin/env python3.7

from typing import List, Tuple


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
        assert len(sequence) == len(proposal)

        blank = '@'

        whites = 0
        reds = 0

        aux_proposal = proposal.split()
        aux_secret = sequence.split()

        # count all reds
        for i in range(0, len(aux_secret)):

            if aux_secret == aux_proposal[i]:
                reds += 1
                aux_proposal[i] = blank
                aux_secret[i] = blank

        for i in range(0, len(aux_secret)):

            if aux_secret[i] != blank:

                for e in range(len(aux_proposal)):

                    if aux_proposal[e] == aux_secret[i]:
                        whites += 1
                        aux_proposal[e] = blank
                        break

        return whites, reds

    def compare(self, proposal: str) -> Tuple[int, int]:
        """
        Compare the proposed sequence with the secret sequence
        :param proposal: sequence proposed as the correct secret sequence
        :return: tuple with number of whites and number of reds
        """
        return self.compare_sequences(self.sequence, proposal)
