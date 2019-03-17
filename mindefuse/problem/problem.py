#!/usr/bin/env python3.7

from .secret import Secret
from .secret import SecretTypes
from .secret import SecretFactory


class Problem:
    """
    Representation of a Mastermind style problem
    """

    """number of query rounds of the problem"""
    __rounds = int

    """secret to be uncovered"""
    __secret = Secret

    def __init__(self, rounds: int, secret_type: SecretTypes, secret_size: int, secret=None):
        """
        Creates a Mastermind style problem
        :param rounds: number of problem rounds
        :param secret_type: secret type
        :param secret_size: secret sequence size
        :param secret: secret sequence provided the user TODO review if needed, later
        """
        self.__rounds = rounds
        self.__secret = self.__generate_secret(secret_type=secret_type, secret_size=secret_size, secret=secret)

    @staticmethod
    def __generate_secret(secret_type: SecretTypes, secret_size: int, secret=None):
        """
        Generates a secret sequence for the problem
        Should only be called once, upon Problem construction
        :param secret_type: type of the secret
        :param secret_size: size of the secret sequence
        :param secret: user defined secret TODO review if needed, later
        :return: generated secret sequence
        """
        return SecretFactory.generate_secret(secret_type=secret_type, size=secret_size)

    def check_secret(self):  # TODO test only, delete later
        """
        Provides the generated secret sequence
        :return: secret sequence
        """
        return self.__secret.sequence
