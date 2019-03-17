#!/usr/bin/env python3.7

from typing import List


class Secret:
    """
    Representation of a secret sequence
    """

    """list of all possible elements for this type of Secret"""
    possible_elements = List[str]

    """number of elements in this secret"""
    elements = int

    """number of possible types of an element in the sequence"""
    types = int

    """secret sequence"""
    sequence = str

    def __init__(self, possible_elements, elements, types, sequence):
        self.possible_elements = possible_elements
        self.elements = elements
        self.types = types
        self.sequence = sequence
