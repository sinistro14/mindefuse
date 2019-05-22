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
        peg_possibilities_list = [p for p in itertools.product(peg_space, repeat=problem.secret_size())]
        
        agent_list = [
            AgentRandom(),
            AgentSamePos(0),
            AgentNextPos()
        ]

        best_problem = problem
        last_proposal = None

        while True:
            best_proposal = None

            agent_problem_to_copy = copy.deepcopy(best_problem)

            for agent in agent_list:

                if best_problem and best_problem.finished():
                    best_problem.generate_response((last_proposal.whites,last_proposal.reds))
                    return best_problem

                agent_problem = copy.deepcopy(agent_problem_to_copy)
                agent_choice = ''.join(agent.agent_choice(peg_possibilities_list))
                proposal = agent_problem.check_proposal(self.create_proposal(agent_choice), respond=False)

                if best_problem.finished() or proposal.reds == 4:
                    best_problem = agent_problem
                    best_problem.generate_response((proposal.whites,proposal.reds))
                    return best_problem

                if proposal and (not best_proposal or self.better_proposal(proposal, best_proposal)):
                    last_proposal = proposal
                    best_proposal = proposal
                    best_problem = agent_problem

            if not best_problem.finished():
                best_problem.generate_response((best_proposal.whites,best_proposal.reds))

            peg_possibilities_list = self.prune_guesses(
                peg_possibilities_list,
                best_proposal.sequence,
                best_proposal.reds,
                best_proposal.whites
            )

        return best_problem

    @staticmethod
    def better_proposal(proposal1, proposal2):
        prop1 = proposal1.reds + proposal1.whites
        prop2 = proposal2.reds + proposal2.whites
        return (prop1 > prop2) or (prop1 == prop2 and proposal1.whites > proposal2.whites)

    @staticmethod
    def prune_guesses(possibilities, current_guess, red, white):
        new_possibilities = []

        for possibility in possibilities:
            possib = ''.join(possibility)
            if (possib != current_guess) and (Problem.compare_sequences(possib, current_guess) == (white, red)):
                new_possibilities.append(possibility)
        return new_possibilities

    @staticmethod
    def get_num_matching_vals(list1, list2):
        return len([e1 for e1, e2 in zip(list1, list2) if e1 == e2])
