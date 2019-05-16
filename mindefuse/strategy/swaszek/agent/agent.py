#!/usr/bin/env python3.7

from abc import ABC, abstractmethod


class Agent(ABC):

    @property
    @abstractmethod
    def _type(self):
        """Agent type identifier"""
        pass

    @abstractmethod
    def agent_choice(self, possibilities):
        """
        Returns the choice of the specific agent
        :param possibilities: list of all possible solutions of which the agent will pick one
        """
        pass
