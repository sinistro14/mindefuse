#!/usr/bin/env python3.7

import random

from .agent import Agent


class AgentRandom(Agent):

    #def __init__(self):
        #self.previous = None

    def agent_choice(self, possibilities):
        """
        Randomly pick a choice from the possibilities list,
        if the choice is the same as the previous pick a new one
        """
        if(len(possibilities) > 0):
            return random.choice(possibilities)
        return None
