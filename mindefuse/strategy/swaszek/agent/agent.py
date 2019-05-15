from abc import ABC, abstractmethod

class Agent(ABC):

    @property
    @abstractmethod
    def _type(self):
        """Agent type identifier"""
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def agentChoice(self, possibilities):
        """
        Returns the choice of the specific agent
        :param possibilities: list of all possible solutions of wich the agent will pick one
        """"
        pass