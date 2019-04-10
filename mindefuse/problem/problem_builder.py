#!/usr/bin/env python3.7

from .problem import Problem
from .secret import SecretTypes
from .problem_default_config import ProblemDefaultConfig as Config


class ProblemBuilder:
    """
    Problem builder
    """

    """secret types that the builder is able to generate"""
    __available_types = (
        SecretTypes.NUMERIC,
        SecretTypes.LSTRING,
        SecretTypes.STRING,
    )

    """number of query rounds of the problem"""
    __rounds = int

    """secret type"""
    __secret_type = SecretTypes

    """secret sequence size"""
    __secret_size = int

    """secret sequence provided by the user"""
    __secret = str  # TODO review if it makes sense, later

    def __init__(self):
        """
        Initializes a builder with the Problem default values
        """
        self.__rounds = Config.ROUNDS
        self.__secret = Config.DEFAULT_SECRET
        self.__secret_type = Config.DEFAULT_TYPE
        self.__secret_size = Config.DEFAULT_SIZE

    def set_type(self, secret_type: SecretTypes):
        """
        Set secret type value
        :param secret_type: secret type to set
        :return: builder
        """
        if secret_type in self.__available_types:
            self.__secret_type = secret_type

        return self

    def set_rounds(self, rounds):
        """
        Set the number of problem rounds
        :param rounds: number of problem rounds to set
        :return: builder
        """
        self.__rounds = rounds
        return self

    def set_secret_size(self, size):
        """
        Set the size of the secret sequence
        :param size: size of the secret sequence to set
        :return: builder
        """
        self.__secret_size = size
        return self

    def set_secret(self, secret):
        """
        Set the secret sequence to use in the problem
        :param secret: secret to set
        :return: builder
        """
        if secret:
            self.set_secret_size(len(secret))
            self.__secret = secret
        return self

    def build(self) -> Problem:
        """
        Builds a Problem with the provided settings
        :return: Problem
        """
        return Problem(
            rounds=self.__rounds,
            secret_type=self.__secret_type,
            secret_size=self.__secret_size,
            secret=self.__secret
        )
