#!/usr/bin/env python3.7

from .agent import Agent
from .agent_types import AgentTypes


class AgentNextPos(Agent):

    _type = AgentTypes.SAMEPOS

    def __init__(self):
        self.pos = 0

    def agent_choice(self, possibilities):
        if self.pos < len(possibilities):
            self.pos += 1
            return possibilities[self.pos - 1]
        else:
            self.pos = 1
            return possibilities[self.pos - 1]
