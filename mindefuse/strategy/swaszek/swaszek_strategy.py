#!/usr/bin/env python3.7

from ..strategy import Strategy
from ..strategy_types import StrategyTypes
from .agent import AgentNextPos, AgentSamePos, AgentRandom

import itertools
from collections import OrderedDict
from collections import Counter

from ..strategy import Strategy
from ..strategy_types import StrategyTypes
from .agent import AgentNextPos, AgentSamePos, AgentRandom


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
        #answer = None

        previous_choices = []

        while answer_not_found:
            peg_possibilities_list_next = peg_possibilities_list

            it = 0
            if it < len(peg_possibilities_list):
                #for a in agent_list:
                    a = agent_list[0]
                    it += 1
                    agent_choice = a.agent_choice(peg_possibilities_list)
                    if not (agent_choice == 0 or agent_choice is None):
                        a_choice = ''.join(agent_choice)
                        if a_choice not in previous_choices:
                            proposal = problem.check_proposal(self.create_proposal(a_choice))
                            if(problem.finished()):
                                #answer = proposal
                                answer_not_found = False
                                break

                            peg_possibilities_list = self.eliminate_possibilities(peg_possibilities_list, a_choice, proposal.reds, proposal.whites)
                            previous_choices.append(a_choice)
            else:
                a_choice = ''.join(agent_list[0].agent_choice(peg_possibilities_list))
                print(a_choice)
                proposal = problem.check_proposal(self.create_proposal(a_choice))
                if(problem.finished()):
                    #answer = proposal
                    answer_not_found = False
                    break

                peg_possibilities_list = self.eliminate_possibilities(peg_possibilities_list, a_choice, proposal.reds, proposal.whites)

            num_it += 1

        return problem

    @staticmethod
    def get_answer_V2(peg_solution, peg_guess):
        sol = list(peg_solution)
        guess = list(peg_guess)
        in_guess = list(OrderedDict.fromkeys(peg_guess))
        
        checked = []
        red = 0
        white = 0
        
        for i in range(0, len(guess)):
            if guess[i] == sol[i]:
                red += 1
                checked.append(i)
                
        for j in in_guess:
            for k in range(0, len(sol)):
                if k not in checked and sol[k] == j:
                    white += 1
        
        return red, white

    @staticmethod
    def eliminate_possibilities(possibilities, current_guess, red, white):
        new_possibilities = []

        cntr = 0
        for possibility in possibilities:
            #res = possibility - current_guess
            res = len(list((Counter(possibility) - Counter(current_guess)).elements()))
            """print("possibility: ")
            print(possibility)
            print("res: ")
            print(res)"""
            if res <= len(current_guess)-(red + white):
                if SwaszekStrategy.get_num_matching_vals(possibility, current_guess) >= red:
                    cntr += 1
                    new_possibilities.append(possibility)
            
        return new_possibilities

    @staticmethod
    def get_num_matching_vals(list1, list2):
        total = 0
        for i in range(0, len(list1)):
            if list1[i] == list2[i]:
                total += 1
        return total
