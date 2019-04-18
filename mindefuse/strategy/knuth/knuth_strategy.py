#!/usr/bin/env python3.7

from itertools import product

from ..strategy import Strategy
from ..strategy_types import StrategyTypes


class KnuthStrategy(Strategy):
    """
    Knuth strategy

    TODO write algorithm
    """

    _type = StrategyTypes.KNUTH

    def _initial_guess(self, problem):
        # TODO complete
        return "1122"

    def _generate_combinations(self, possible_elements, secret_size):
        return product(possible_elements, repeat=secret_size)

    def _get_next_guess(self, guesses):
        for guess in guesses:
            return guess

    def _remove_guess(self, guesses, guess_to_remove):  # TODO review
        return (guess for guess in guesses if guess is not guess_to_remove)

    def prune_guesses(self, problem, guesses, current_guess, answer):
        return (guess for guess in guesses if problem.compare_sequences(guess, current_guess) == answer)

    def _mini_max(self, problem, all_combinations, solutions):

        best_score = {}

        for el in all_combinations:

            score_count = {}

            for opt in solutions:
                score = problem.compare_sequences(el, opt)
                score = score[0] + score[1]
                if score_count.get(score):
                    score_count[score] += 1
                else:
                    score_count[score] = 1

            max_score = max(score_count, key=score_count.get)
            max_score = score_count[max_score]
            best_score[el] = max_score

        min_score = min(best_score, key=best_score.get)
        min_score = best_score[min_score]

        next_guesses = (v for k, v in best_score.items() if v == min_score)

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

            self._remove_guess(all_combinations, current_guess)
            self._remove_guess(solutions, current_guess)

            proposal = self.create_proposal(current_guess)

            answer = problem.check_proposal(proposal)

            if answer.reds == secret_size:
                print("The game is won!")
                break

            # Remove from solutions, any code that would not give the same response if it were the code
            self.prune_guesses(problem, solutions, current_guess, (answer.whites, answer.reds))

            next_guesses = self._mini_max(problem, all_combinations, solutions)

            current_guess = self._get_next_guess(next_guesses)
            turn += 1

        return
