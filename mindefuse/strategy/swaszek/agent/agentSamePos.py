from agent import Agent
from agent_types import AgentTypes

class AgentSamePos(Agent):

     _type = AgentTypes.SAMEPOS

    def __init__(self, pos):
        self.pos = pos
        self.previous = None

    def agentChoice(self, possibilities):
        if not (self.previous == possibilities[self.pos]):
            self.previous = possibilities[self.pos]
            return self.previous
        return None