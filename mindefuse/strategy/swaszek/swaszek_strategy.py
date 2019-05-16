#!/usr/bin/env python3.7

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
        #self.swaszek(problem.__secret.possible_elements(), problem.__secret.possible_elements)

    #def swaszek(peg_solution, peg_space):
        peg_space = problem.possible_elements()
        num_it = 0
        peg_possibilities_list = [p for p in itertools.product(peg_space, repeat=problem.secret_size())]
        
        agent_list = [
            AgentRandom(),
            AgentSamePos(0),
            AgentNextPos()
        ]
        
        while len(peg_possibilities_list) > 1:
            #choice = peg_possibilities_list[0]
            peg_possibilities_list_next = peg_possibilities_list
            #print(len(peg_possibilities_list))
            
            it = 0
            if it < len(peg_possibilities_list):
                for a in agent_list:
                    it += 1
                    a_choice = a.agent_choice(peg_possibilities_list)
                    if not (a_choice == 0 or a_choice is None):
                        print(a_choice)
                        #red_pegs, white_pegs = getAnswerV2(peg_solution, a_choice)
                        proposal = problem.check_proposal(self.create_proposal(a_choice))
                        peg_possibilities_list_next = self.eliminate_possibilities(peg_possibilities_list_next, a_choice, proposal.reds, proposal.whites)
            else:
                a_choice = agent_list[0].agent_choice(peg_possibilities_list)
                print(a_choice)
                #redPegs, whitePegs = getAnswerV2(peg_solution, a_choice)
                proposal = problem.check_proposal(self.create_proposal(a_choice))
                peg_possibilities_list_next = self.eliminate_possibilities(peg_possibilities_list_next, a_choice, proposal.reds, proposal.whites)
                print(len(peg_possibilities_list_next))
            
            #print(len(peg_possibilities_list_next))
            peg_possibilities_list = peg_possibilities_list_next
            #print(len(peg_possibilities_list))
            #print("-------------------------")
            num_it += 1

        print(peg_possibilities_list[0])
        print(str(num_it) + " attempts")

    """class AgentSamePos:
        def __init__(self, pos):
            self.pos = pos
            self.previous = None
        
        def agent_choice(self, possibilities):
            if not (self.previous == possibilities[self.pos]):
                self.previous = possibilities[self.pos]
                return self.previous
            return None
        
    class AgentRandom:
        def __init__(self):
            self.previous = None
            
        def agent_choice(self, possibilities):
            choice = random.choice(possibilities)
            while(choice == self.previous):
                choice = random.choice(possibilities)
            return choice
        
    class AgentNextPos:
        def __init__(self):
            self.pos = 0
        
        def agent_choice(self, possibilities):
            if(self.pos < len(possibilities)):
                self.pos += 1
                return possibilities[self.pos-1]
            else:
                self.pos = 1
                return possibilities[self.pos-1]"""

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
        
        for possibility in possibilities:
            #res = possibility - current_guess
            res = len(list((Counter(possibility) - Counter(current_guess)).elements()))
            """print("possibility: ")
            print(possibility)
            print("res: ")
            print(res)"""
            if res <= len(current_guess)-(red + white):
                if SwaszekStrategy.get_num_matching_vals(possibility, current_guess) >= red:
                    new_possibilities.append(possibility)
            
        return new_possibilities

    @staticmethod
    def get_num_matching_vals(list1, list2):
        total = 0
        for i in range(0, len(list1)):
            if list1[i] == list2[i]:
                total += 1
        return total
