#!/usr/bin/env python3.7

from multiprocessing import Pool, Manager, cpu_count
from itertools import product, tee
from collections import defaultdict
from functools import partial

from .knuth_config import KnuthConfig as Config
from ..strategy import Strategy
from ..strategy_types import StrategyTypes


class KnuthStrategy(Strategy):
    """
    Knuth strategy

    TODO write algorithm
    """

    _type = StrategyTypes.KNUTH

    def _initial_guess(self, problem):
        # TODO review if there is a better way to generate the initial guess
        times = 1
        final = ""
        secret_size = problem.secret_size()

        for el in problem.possible_elements():
            final += times * el
            times += 1

            if len(final) >= secret_size:
                break

        return final[:secret_size]

    def _generate_combinations(self, possible_elements, secret_size):
        return map(''.join, product(possible_elements, repeat=secret_size))

    def _get_next_guess(self, guesses, all_combinations, solutions):

        solutions = set(solutions)

        guesses1, guesses2 = tee(guesses)

        for guess in guesses1:
            if guess in solutions:
                return guess

        all_combinations = set((comb for comb in all_combinations if comb not in solutions))

        for guess in guesses2:
            if guess in all_combinations:
                return guess

    def _remove_guess(self, guesses, guess_to_remove):  # TODO review
        return (guess for guess in guesses if guess != guess_to_remove)

    def prune_guesses(self, problem, guesses, current_guess, answer):
        return (guess for guess in guesses if problem.compare_sequences(guess, current_guess) == answer)

    def _count_score(self, combination, problem, solutions, best_score):

        score_count = defaultdict(int)

        for opt in solutions:
            score = sum(problem.compare_sequences(combination, opt))  # sum the two elements of the array
            score_count[score] += 1

        best_score[combination] = score_count[max(score_count, key=score_count.get)]

    def _mini_max(self, problem, all_combinations, solutions):

        manager = Manager()

        best_score = manager.dict()

        pool = Pool(Config.POOL_SIZE)

        pool.map(  # blocking call
            partial(self._count_score, problem=problem, solutions=list(solutions), best_score=best_score),
            iterable=list(all_combinations),
            chunksize=problem.complexity // Config.POOL_SIZE
        )

        pool.close()

        min_score = best_score[min(best_score, key=best_score.get)]

        next_guesses = (k for k, v in sorted(best_score.items()) if v == min_score)

        manager.shutdown()

        return next_guesses

    def solve(self, problem):
        secret_size = problem.secret_size()
        possible_elements = problem.possible_elements()

        initial_guess = self._initial_guess(problem)

        current_guess = initial_guess

        all_combinations = self._generate_combinations(possible_elements, secret_size)
        solutions = self._generate_combinations(possible_elements, secret_size)
        turn = 0

        # TODO create correct loop here
        while not problem.finished():

            turn += 1

            proposal = self.create_proposal(current_guess)

            answer = problem.check_proposal(proposal)

            if problem.finished():
                break

            # remove guess from pools
            solutions = self._remove_guess(solutions, current_guess)
            all_combinations = self._remove_guess(all_combinations, current_guess)

            # remove from solutions any code that would not give the same response if it was the secret sequence
            solutions = self.prune_guesses(problem, solutions, current_guess, (answer.whites, answer.reds))

            solutions, solutions_aux = tee(solutions)
            all_combinations, all_combinations_aux = tee(all_combinations)
            next_guesses = self._mini_max(problem, all_combinations_aux, solutions_aux)

            solutions, solutions_aux = tee(solutions)
            all_combinations, all_combinations_aux = tee(all_combinations)
            current_guess = self._get_next_guess(next_guesses, all_combinations_aux, solutions_aux)

        problem.print_history()
        return problem
