#!/usr/bin/env python3.7

from typing import Union, List
from timeit import default_timer as time
from random import choice
from math import floor

from .secret import Secret
from .secret import SecretTypes
from .secret import SecretFactory
from .proposal import Proposal
from .history import History
from .responses import Responses


class Problem(Responses):
    """
    Representation of a Mastermind style problem
    """

    """whether the problem is solved"""
    __solved = bool

    """whether the problem is finished"""
    __finished = bool

    """number of query rounds of the problem"""
    __rounds = int

    """number of rounds elapsed, also corresponds to the number of guesses"""
    elapsed_rounds = int

    """time at which the first guess was submitted"""
    __start_time = float

    """secret to be uncovered"""
    __secret = Secret

    """metric to establish the complexity of the problem, the size of the solution space"""
    complexity = int

    """history of guesses and answers of the game"""
    history = History

    def __init__(self, rounds: int, secret_type: SecretTypes, secret_size: int, secret=None):
        """
        Creates a Mastermind style problem
        If provided, the secret overrides all other definitions, except the number of rounds
        :param rounds: number of available rounds
        :param secret_type: secret type
        :param secret_size: secret sequence size
        :param secret: secret sequence provided by the user
        """
        self.__solved = False
        self.__finished = False
        self.__rounds = rounds
        self.__secret = self.__generate_secret(secret_type=secret_type, secret_size=secret_size, secret=secret)
        self.elapsed_rounds = rounds
        self.history = History()
        self.complexity = self.__estimate_complexity()
        self.__start_time = None

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

    def __estimate_complexity(self):
        """
        Estimates the complexity of the problem
        :return: complexity metric
        """
        return pow(len(self.__secret.possible_elements), self.secret_size())

    def __time_passed(self):
        """
        Provides the time passed since the first time it was requested
        :return: microseconds passed
        """
        now = time()
        self.__start_time = self.__start_time or now
        return now - self.__start_time

    def __current_round(self) -> int:
        """
        Provides the current round value
        :return: current round
        """
        return self.__rounds - self.elapsed_rounds

    def __generate_response(self, answer):
        """
        Evaluates captor's mood after a guess and prints a response. This mood is given by (2R + W) / 2S, where R and W
        are the number red and white pegs, respectively, and S is the secret size. The actual response is chosen
        randomly based on the mood.
        :param answer: current round's answer
        """
        score = floor(4 * (2 * answer[1] + answer[0]) / (2 * self.secret_size()))
        print('Negotiation round {} -> Captor: {}'.format(self.__current_round(),
                                                          choice(Responses.MOODS.get(score))), flush=True)

    def check_proposal(self, proposal: Proposal) -> Union[Proposal, None]:
        """
        Verify how many whites and reds correspond to the proposed sequence
        Represents a played turn, therefore, it elapses a round
        :param proposal: Proposal submitted by the player
        :return: tuple with number of whites and reds if the game is not over, None otherwise
        """
        if not self.__finished:
            self.elapsed_rounds -= 1

            answer = proposal.reds = self.__secret.compare(proposal.sequence)
            proposal.whites, proposal.reds = answer

            if proposal.reds == self.__secret.elements:     # the correct secret was proposed
                self.__solved = True
                self.__finished = True

            if not self.elapsed_rounds:                     # the maximum number of rounds has passed
                self.__finished = True

            self.history.add_entry(                         # update history
                self.__current_round(),
                self.__secret.sequence,
                proposal.sequence,
                answer,
                self.__time_passed()
            )
            self.__generate_response(answer)
            return proposal
        return None

    def secret_type(self) -> SecretTypes:
        """
        Provides the type fo secret
        :return: type of secret
        """
        return self.__secret.type

    def secret_size(self) -> int:
        """
        Provides the size of the secret sequence
        :return: size of the secret sequence
        """
        return self.__secret.elements

    def possible_elements(self) -> List[str]:
        """
        Provides a list with the possible colours of the sequence
        :return: list of strings
        """
        return self.__secret.possible_elements

    @staticmethod
    def compare_sequences(sequence1, sequence2):
        """
        Compares two sequences, assuming the first one to be the correct
        :param sequence1: first sequence
        :param sequence2: second sequence
        :return: a tuple with number of whites and reds
        """
        return Secret.compare_sequences(sequence1, sequence2)

    def solved(self):
        """
        States whether the problem was solved
        :return: True if the problem was solved, False otherwise
        """
        return self.__solved

    def finished(self):
        """
        State whether the problem is finished
        The problem may be finished if the maximum number of rounds passed or if was solved
        :return: True if the problem is finished, False otherwise
        """
        return self.__finished

    def time_to_solve(self):
        """
        Provides the time, in seconds, take to solve the problem
        :return: time taken to solve the problem
        """
        return self.history.duration()

    def print_secret(self):
        """
        Prints the generated secret sequence
        :return: secret sequence
        """
        print(self.__secret.sequence)

    def print_history(self):
        """
        Prints the history of the problem
        """
        history = "{}\n".format(self.history)
        if self.__solved:
            history += "The game was won!!!\n"
        else:
            history = 'Negotiation Round _ -> Captor: {}\n' \
                      '*BANG*\n' \
                      '{}' \
                      'The game was lost.\n'.format(choice(Responses.FAILURE), history)
        print(history)
