#!/usr/bin/env python3.7

from typing import List
from .entry import Entry


class History:

    """entries that form the history of the game"""
    entries = List[Entry]

    def __init__(self):
        self.entries = []

    def add_entry(self, round_val, secret, guess, answer):
        """
        Add another round information to the history
        :param round_val: value of the round of the guess
        :param secret: value of the secret
        :param guess: guess submitted by the player
        :param answer: corresponding whites and reds
        """
        self.entries.append(
            Entry(round_val=round_val, secret=secret, guess=guess, answer=answer)
        )

    def __str__(self):
        final = "History\n"
        for entry in self.entries:
            final += str(entry)
        return final
