
import random

from .agent import Agent
#from agent_types import AgentTypes

class AgentRandom(Agent):

     #_type = AgentTypes.RANDOM

    def __init__(self):
        self.previous = None

    def agentChoice(self, possibilities):
        """
        Randomly pick a choice from the possibilities list,
        if the choice is the same as the previous pick a new one
        """
        choice = random.choice(possibilities)
        while(choice == self.previous):
            choice = random.choice(possibilities)
        return choice
