#!/usr/bin/env python3.7

from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Strategy used to solve a problem
    """

    @property
    @abstractmethod
    def _type(self):
        pass

    def __init__(self):
        pass

    def register(self, context):
        """
        Register the strategy to a given context
        :param context: context to which the strategy belongs
        """
        context.register(self._type, self)

    # TODO add problem solver method
