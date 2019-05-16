#!/usr/bin/env python3.7

from ..strategy import Strategy
from ..strategy_types import StrategyTypes
from .agent import AgentNextPos, AgentSamePos, AgentRandom

import itertools

from collections import OrderedDict
from collections import Counter

class SwaszekStrategy(Strategy):
    """
    Swaszek strategy
    """

    _type = StrategyTypes.SWASZEK

    def solve_problem(self, problem):
        #self.swaszek(problem.__secret.possible_elements(), problem.__secret.possible_elements)

    #def swaszek(pegSolution, pegSpace):
        pegSpace = problem.possible_elements()
        numIt = 0
        pegPossibilitiesList = [p for p in itertools.product(pegSpace, repeat=problem.secret_size())]
        
        agentList = []
        agentList.append(AgentRandom())
        agentList.append(AgentSamePos(0))
        agentList.append(AgentNextPos())
        
        while(len(pegPossibilitiesList) > 1):
            #choice = pegPossibilitiesList[0]
            pegPossibilitiesListNext = pegPossibilitiesList
            #print(len(pegPossibilitiesList))
            
            it = 0
            if(it < len(pegPossibilitiesList)):
                for a in agentList:
                    it += 1
                    aChoice = a.agentChoice(pegPossibilitiesList)
                    if not(aChoice == 0 or aChoice == None):
                        print(aChoice)
                        #redPegs, whitePegs = getAnswerV2(pegSolution, aChoice)
                        proposal = problem.check_proposal(self.create_proposal(aChoice))
                        pegPossibilitiesListNext = eliminatePossibilities(pegPossibilitiesListNext, aChoice, proposal.reds, proposal.whites)
            else:
                aChoice = agentList[0].agentChoice(pegPossibilitiesList)
                print(aChoice)
                #redPegs, whitePegs = getAnswerV2(pegSolution, aChoice)
                proposal = problem.check_proposal(self.create_proposal(aChoice))
                pegPossibilitiesListNext = eliminatePossibilities(pegPossibilitiesListNext, aChoice, proposal.reds, proposal.whites)
                print(len(pegPossibilitiesListNext))
            
            #print(len(pegPossibilitiesListNext))  
            pegPossibilitiesList = pegPossibilitiesListNext
            #print(len(pegPossibilitiesList))
            #print("-------------------------")
            numIt += 1

        print(pegPossibilitiesList[0])
        print(str(numIt) + " attempts")

    """class AgentSamePos:
        def __init__(self, pos):
            self.pos = pos
            self.previous = None
        
        def agentChoice(self, possibilities):
            if not (self.previous == possibilities[self.pos]):
                self.previous = possibilities[self.pos]
                return self.previous
            return None
        
    class AgentRandom:
        def __init__(self):
            self.previous = None
            
        def agentChoice(self, possibilities):
            choice = random.choice(possibilities)
            while(choice == self.previous):
                choice = random.choice(possibilities)
            return choice
        
    class AgentNextPos:
        def __init__(self):
            self.pos = 0
        
        def agentChoice(self, possibilities):
            if(self.pos < len(possibilities)):
                self.pos += 1
                return possibilities[self.pos-1]
            else:
                self.pos = 1
                return possibilities[self.pos-1]"""

    def getAnswerV2(pegSolution, pegGuess):
        sol = list(pegSolution)
        guess = list(pegGuess)
        inGuess = list(OrderedDict.fromkeys(pegGuess))
        
        checked = []
        red = 0
        white = 0
        
        for i in range(0,len(guess)):
            if(guess[i] == sol[i]):
                red += 1
                checked.append(i)
                
        for j in inGuess:
            for k in range(0, len(sol)):
                if(k not in checked and sol[k] == j):
                    white += 1
        
        return red, white

    def eliminatePossibilities(possibilities, currentGuess, red, white):
        new_possibilities = []
        
        for possibility in possibilities:
            #res = possibility - currentGuess
            res = len(list((Counter(possibility) - Counter(currentGuess)).elements()))
            """print("possibility: ")
            print(possibility)
            print("res: ")
            print(res)"""
            if(res <= len(currentGuess)-(red + white)):
                if(getNumMatchingVals(possibility, currentGuess) >= red):
                    new_possibilities.append(possibility)
            
        return new_possibilities


    def getNumMatchingVals(list1, list2):
        total = 0
        for i in range(0, len(list1)):
            if(list1[i] == list2[i]):
                total += 1
        return total
