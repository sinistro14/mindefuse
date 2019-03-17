#!/usr/bin/env python3.7

from abc import ABC, abstractmethod
from ..secret import Secret
from .sequence_generator import SequenceGenerator


class SecretGenerator(ABC):
    """
    Abstract Secret Generator
    The elements of the sequence are chosen from a set of possible options
    available only to this type of generator.
    Subclasses are only required to define the set of possible components
    and the type of secrets that they generate.
    """

    """default size of the sequence to create"""
    _default_size = 4

    @property
    @abstractmethod
    def _type(self):
        """
        Type of secret produced by this generator
        """
        pass

    @property
    @abstractmethod
    def _possible_elements(self):
        """
        List of elements that each component of a sequence can take
        """
        pass

    def register(self, factory):
        """
        Registers a generator to a factory
        :param factory: factory where this generator will be registered
        """
        factory.register(self._type, self)

    def generate(self, size=None) -> Secret:
        """
        Generates a Secret of a given size, if provided
        :param size: size of the secret sequence to produce
        :return: Secret
        """

        if not size:
            size = self._default_size

        sequence = SequenceGenerator.generate(possible_elements=self._possible_elements, sequence_size=size)

        return Secret(
            sequence=sequence,
            elements=len(sequence),
            types=len(self._possible_elements),
            possible_elements=self._possible_elements
        )
