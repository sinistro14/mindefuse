#!/usr/bin/env python3.7

from typing import Union, Tuple
from .secret import Secret
from .secret import SecretTypes
from .secret import SecretFactory
from .proposal import Proposal


class Problem:
    """
    Representation of a Mastermind style problem
    """

    """number of query rounds of the problem"""
    __rounds = int

    elapsed_rounds = int

    """secret to be uncovered"""
    __secret = Secret

    def __init__(self, rounds: int, secret_type: SecretTypes, secret_size: int, secret=None):
        """
        Creates a Mastermind style problem
        If provided, the secret overrides all other definitions, except the number of rounds
        :param rounds: number of available rounds
        :param secret_type: secret type
        :param secret_size: secret sequence size
        :param secret: secret sequence provided by the user
        """
        self.__rounds = rounds
        self.elapsed_rounds = rounds
        self.__secret = self.__generate_secret(secret_type=secret_type, secret_size=secret_size, secret=secret)

    @staticmethod
    def __generate_secret(secret_type: SecretTypes, secret_size: int, secret=None):
        """
        Generates a secret sequence for the problem
        Should only be called once, upon Problem construction
        :param secret_type: type of the secret
        :param secret_size: size of the secret sequence
        :param secret: user defined secret
        :return: generated secret sequence
        """
        return SecretFactory.generate_secret(secret_type=secret_type, size=secret_size, secret=secret)

    def check_secret(self):  # TODO test only, delete later
        """
        Provides the generated secret sequence
        :return: secret sequence
        """
        return self.__secret.sequence

    def check_proposal(self, proposal: Proposal) -> Union[Proposal, None]:
        """
        Verify how many whites and reds correspond to the proposed sequence
        Represents a played turn, therefore, it elapses a round
        :param proposal: Proposal submitted by the player
        :return: tuple with number of whites and reds if the max number of rounds was not reached, None otherwise
        """
        if self.elapsed_rounds:
            self.elapsed_rounds -= 1
            proposal.whites, proposal.reds = self.__secret.compare(proposal.sequence)
            return proposal
        return None

    def secret_size(self):
        """
        Provides the size of the secret sequence
        :return: size of the secret sequence
        """
        return self.__secret.elements

    def possible_elements(self):
        """
        Provides a list with the possible colours of the sequence
        :return: list of strings
        """
        return self.__secret.possible_elements

    def compare_sequences(self, sequence1, sequence2):
        """
        Compares two sequences, assuming the first one to be the correct
        :param sequence1: first sequence
        :param sequence2: second sequence
        :return: a tuple with number of whites and reds
        """
        return self.__secret.compare_sequences(sequence1, sequence2)
