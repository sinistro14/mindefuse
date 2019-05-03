#!/usr/bin/env python3.7

from abc import ABC, abstractmethod
from collections import defaultdict

from mindefuse.problem import Problem


class ScoreCount(ABC):

    @staticmethod
    def _count_score(combination, solutions):
        """
        Sets in scores the score of the provided combination.
        The score of a combination is the maximum size of the solution space, in the worst case,
        if the said combination was the secret sequence.
        :param combination: combination being tested
        :param solutions: solution space
        """
        score_count = defaultdict(int)

        for solution in solutions:
            score = sum(Problem.compare_sequences(combination, solution))  # sum the two elements of the array
            score_count[score] += 1

        return combination, score_count[max(score_count, key=score_count.get)]

    @staticmethod
    @abstractmethod
    def run(combinations, solutions):
        pass
