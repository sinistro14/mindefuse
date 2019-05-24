#!/usr/bin/env python3.7

from typing import Iterable

from ..score_count import ScoreCount


class SimpleScore(ScoreCount):
    """
    Iterative score counter
    """

    @staticmethod
    def run(combinations: Iterable, solutions: Iterable):

        solutions = list(solutions)

        return {
            combination: score for combination, score in
            [ScoreCount.count_score(combination, solutions) for combination in combinations]
        }
