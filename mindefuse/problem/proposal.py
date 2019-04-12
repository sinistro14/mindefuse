#!/usr/bin/env python3.7


class Proposal:
    """
    Sequence proposed by the player while trying to guess the secret
    The problem will add hint information, by setting the value of whites and reds
    """

    """proposed secret sequence"""
    sequence = str

    """number of right colours in a wrong position"""
    whites = int

    """number of right colours in the correct position"""
    reds = int

    def __init__(self, sequence):
        """
        Create a proposal
        :param sequence: secret sequence proposed by the player
        """
        self.sequence = sequence
