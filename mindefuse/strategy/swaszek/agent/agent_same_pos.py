#!/usr/bin/env python3.7

from .agent import Agent


class AgentSamePos(Agent):

    def __init__(self, pos):
        self.pos = pos

    def agent_choice(self, possibilities):
        if(self.pos > len(possibilities)-1):
            return possibilities[len(possibilities)-1]
        return possibilities[self.pos]
