#!/usr/bin/env python3.7

import itertools
import copy

from ..strategy import Strategy
from ..strategy_types import StrategyTypes
from .agent import AgentNextPos, AgentSamePos, AgentRandom
from mindefuse.problem import Problem


class SwaszekStrategy(Strategy):
    """
    Swaszek strategy
    """

    _type = StrategyTypes.SWASZEK

    def solve_problem(self, problem):
        peg_space = problem.possible_elements()
        num_it = 0
        peg_possibilities_list = [p for p in itertools.product(peg_space, repeat=problem.secret_size())]
        
        agent_list = [
            AgentRandom(),
            AgentSamePos(0),
            AgentNextPos()
        ]

        answer_not_found = True

        previous_choices = []

        best_problem = problem

        while answer_not_found:
            best_proposal = None

            for a in agent_list:
                agent_problem = copy.deepcopy(best_problem)
                agent_choice = ''.join(a.agent_choice(peg_possibilities_list))
                proposal = agent_problem.check_proposal(self.create_proposal(agent_choice))

                if best_problem.finished() or proposal.reds == 4:
                    answer_not_found = False
                    best_proposal = proposal
                    best_problem = agent_problem
                    return best_problem

                if proposal is not None:
                    if best_proposal is None or self.better_proposal(proposal, best_proposal):
                        best_proposal = proposal
                        best_problem = agent_problem

            peg_possibilities_list = self.prune_guesses(
                peg_possibilities_list,
                best_proposal.sequence,
                best_proposal.reds,
                best_proposal.whites
            )

        return best_problem

    @staticmethod
    def better_proposal(proposal1, proposal2):
        if proposal1.reds + proposal1.whites > proposal2.reds + proposal2.whites:
            return True
        elif proposal1.reds + proposal1.whites == proposal2.reds + proposal2.whites:
            if proposal1.whites > proposal2.whites:
                return True
        return False

    @staticmethod
    def prune_guesses(possibilities, current_guess, red, white):
        new_possibilities = []

        for possibility in possibilities:
            possib = ''.join(possibility)
            if possib != current_guess:
                answer = Problem.compare_sequences(possib, current_guess)
                if answer == (white, red):
                    new_possibilities.append(possibility)

        return new_possibilities

    @staticmethod
    def get_num_matching_vals(list1, list2):
        total = 0
        for i in range(0, len(list1)):
            if list1[i] == list2[i]:
                total += 1
        return total
