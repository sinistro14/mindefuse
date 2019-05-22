#!/usr/bin/env python3.7

from mindefuse.problem import Problem, SecretTypes
from ..strategy import Strategy
from ..strategy_types import StrategyTypes
from ..knuth import KnuthStrategy
from ..genetic import GeneticStrategy
from ..swaszek import SwaszekStrategy


class HybridStrategy(Strategy):
    """
    Hybrid strategy.
    Based on the results obtained from the performed set of evaluation tests
    some threshold values have been defined as to choose the best algorithm
    to solve each problem.

    The set of defined rules is:
        - secrets of size 1 are solved with Swaszek
        - secrets of size 2, of types numeric and lstring are solved with Knuth
        - secrets of size 3 are solved with Swaszek
        - secrets of size 4 are solved with Swaszek, unless numeric, which is solved with Genetic
        - secrets of size > 4 are solved with Genetic
    """

    """strategy identification type"""
    _type = StrategyTypes.HYBRID

    """strategies which the selector has access to"""
    __strategies = {
        StrategyTypes.KNUTH: KnuthStrategy(),
        StrategyTypes.GENETIC: GeneticStrategy(),
        StrategyTypes.SWASZEK: SwaszekStrategy(),
    }

    def solve_problem(self, problem: Problem):

        solver = StrategyTypes.GENETIC

        secret_type = problem.secret_type()
        secret_size = problem.secret_size()

        if secret_size == 1 or secret_size == 3:
            solver = StrategyTypes.SWASZEK

        elif secret_type == SecretTypes.NUMERIC:
            if secret_size == 2:
                solver = StrategyTypes.KNUTH
            elif secret_size > 3:
                solver = StrategyTypes.GENETIC

        elif secret_size == SecretTypes.LSTRING:
            if secret_size == 2:
                solver = StrategyTypes.KNUTH
            elif secret_size < 5:
                solver = StrategyTypes.SWASZEK
            else:
                solver = StrategyTypes.GENETIC

        elif secret_type == SecretTypes.STRING:
            if secret_size < 5:
                solver = StrategyTypes.SWASZEK
            else:
                solver = StrategyTypes.GENETIC

        return self.__strategies[solver].solve_problem(problem)
