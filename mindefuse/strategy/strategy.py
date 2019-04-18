#!/usr/bin/env python3.7

from abc import ABC, abstractmethod
from mindefuse.problem import Problem, Proposal


class Strategy(ABC):
    """
    Strategy used to solve a problem
    """

    @property
    @abstractmethod
    def _type(self):
        """Strategy type identifier"""
        pass

    def __init__(self):
        pass

    def register(self, context):
        """
        Register the strategy to a given context
        :param context: context to which the strategy belongs
        """
        context.register(self._type, self)

    @abstractmethod
    def solve(self, problem: Problem):
        """
        Solves a Mastermind problem using a specific algorithm
        :param problem: problem to be solved
        """
        pass

    @staticmethod
    def create_proposal(sequence) -> Proposal:
        """
        Creates a proposal with the guess sequence
        :param sequence: string of the proposed sequence
        :return: proposal
        """
        return Proposal(sequence)
