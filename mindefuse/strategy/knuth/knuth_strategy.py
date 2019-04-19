#!/usr/bin/env python3.7

from itertools import product
from collections import defaultdict
from itertools import tee
from multiprocessing import Pool

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
        all_combinations = list(all_combinations)
        solutions = list(solutions)
        guesses1, guesses2 = tee(guesses)

        for guess in guesses1:
            if guess in solutions:
                return guess

        for guess in guesses2:
            if guess in all_combinations:
                return guess

    def _remove_guess(self, guesses, guess_to_remove):  # TODO review
        return (guess for guess in guesses if guess != guess_to_remove)

    def prune_guesses(self, problem, guesses, current_guess, answer):
        return (guess for guess in guesses if problem.compare_sequences(guess, current_guess) == answer)

    def _mini_max(self, problem, all_combinations, solutions):

        best_score = {}

        all_combinations, aux_solutions = tee(all_combinations)
        solutions, solutions_final = tee(solutions)

        for el in all_combinations:

            score_count = defaultdict(int)
            solutions, solutions_aux = tee(solutions)

            for opt in solutions_aux:
                score = problem.compare_sequences(el, opt)
                score = score[0] + score[1]
                score_count[score] += 1

            max_score = max(score_count, key=score_count.get)
            max_score = score_count[max_score]
            best_score[el] = max_score

        min_score = best_score[min(best_score, key=best_score.get)]

        next_guesses = (k for k, v in sorted(best_score.items()) if v == min_score)

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
        while True:

            turn += 1

            all_combinations = self._remove_guess(all_combinations, current_guess)
            solutions = self._remove_guess(solutions, current_guess)

            proposal = self.create_proposal(current_guess)

            answer = problem.check_proposal(proposal)
            if answer.reds == secret_size:
                print("The game is won!")
                print("Sequence: " + str(current_guess))
                break
            else:
                print("Round " + str(turn))
                print("Sequence: " + str(current_guess))
                print("Points: ({}, {})".format(answer.whites, answer.reds))

            # Remove from solutions any code that would not give the same response if it was the code
            solutions = self.prune_guesses(problem, solutions, current_guess, (answer.whites, answer.reds))

            all_combinations, all_combinations_aux = tee(all_combinations)
            solutions, solutions_aux = tee(solutions)

            next_guesses = self._mini_max(problem, all_combinations_aux, solutions_aux)

            all_combinations, all_combinations_aux = tee(all_combinations)
            solutions, solutions_aux = tee(solutions)
            current_guess = self._get_next_guess(next_guesses, all_combinations_aux, solutions_aux)

        return problem
