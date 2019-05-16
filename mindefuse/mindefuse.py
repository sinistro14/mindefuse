#!/usr/bin/env python3.7

from typing import Dict

from .problem import ProblemBuilder, Problem
from .strategy import NullStrategy, KnuthStrategy, GeneticStrategy, SwaszekStrategy
from .strategy import Strategy, StrategyTypes


class Mindefuse:
    """
    Mastermind style problems solver.
    Given a problem, where a certain sequence is secret, it is able
    to query the adversary with a set of proposals, trying to uncover
    the secret information.
    In each round, the adversary replies with the number of correctly
    guessed elements and the number of misplaced guesses.
    """

    """Holds all the available strategies"""
    __strategies = Dict[StrategyTypes, Strategy]

    def __init__(self):

        self.__strategies = {}

        self.__default_strategy = NullStrategy().register(self)

        # available strategies are added here
        for strategy in (
            KnuthStrategy(),
            GeneticStrategy(),
            SwaszekStrategy()
        ):
            strategy.register(self)

    def register(self, strategy_type, strategy):
        """
        Register a strategy of a given type
        :param strategy_type: type of the strategy to register
        :param strategy: strategy to register
        """
        self.__strategies[strategy_type] = strategy

    def get_strategy(self, strategy_type):
        """
        Provides the requested strategy
        :return: requested strategy type, or NullStrategy otherwise
        """
        return self.__strategies.get(strategy_type, self.__default_strategy)

    @staticmethod
    def generate_problem(rounds, secret_type=None, secret_size=None, secret=None):
        """
        Generates a problem based on the provided specification.
        If secret is defined no random sequence is generated, thus,
        both secret_type and secret_size are overridden
        :param rounds: number of rounds of the problem
        :param secret_type: type of the secret
        :param secret_size: size of the secret sequence
        :param secret: final secret sequence
        :return: built problem
        """
        return ProblemBuilder()\
            .set_rounds(rounds)\
            .set_type(secret_type)\
            .set_secret_size(secret_size)\
            .set_secret(secret)\
            .build()

    def solve_problem(self, rounds, algorithm=None, secret_type=None, secret_size=None, secret=None) -> Problem:
        """
        Tries to solve a problem, using the requested strategy, in the specified number of rounds
        If no secret is defined, a new one is randomly generated with the provided specs
        :param rounds: number of rounds of the problem
        :param algorithm: algorithm used to solve the problem
        :param secret_type: type of secret to generate
        :param secret_size: size of secret to generate
        :param secret: secret proposed by the user
        :return:
        """
        problem = self.generate_problem(rounds=rounds, secret_type=secret_type, secret_size=secret_size, secret=secret)
        problem = self.get_strategy(algorithm).solve_problem(problem)
        problem.print_history()
        return problem
