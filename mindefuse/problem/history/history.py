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

    def duration(self) -> int:
        """
        Provides the time taken to solve a problem, in seconds
        :return: time taken trying to solve the problem, or 0 if not yet run
        """
        if self.entries:
            return self.entries[-1].time
        return 0

    def rounds(self):
        """
        Provides the number of rounds that passed
        :return: rounds that passed
        """
        return len(self.entries)

    def __str__(self):
        final = "{}History{}\n".format(35 * "-", 35 * "-")
        final += "\n".join(str(entry) for entry in self.entries)
        return final
