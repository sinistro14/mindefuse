#!/usr/bin/env python3.7

from typing import List

from .entry import Entry


class History:

    """entries that form the history of the game"""
    entries = List[Entry]

    def __init__(self):
        self.entries = []

    def add_entry(self, round_val, secret, guess, answer, time):
        """
        Add another round information to the history
        :param round_val: value of the round of the guess
        :param secret: value of the secret
        :param guess: guess submitted by the player
        :param answer: corresponding whites and reds
        :param time: time passed since the start of the problem
        """
        self.entries.append(
            Entry(round_val=round_val, secret=secret, guess=guess, answer=answer, time=time)
        )

    def __str__(self):
        final = (35 * "-") + "History" + (35 * '-') + "\n"
        final += "\n".join(str(entry) for entry in self.entries)
        return final
