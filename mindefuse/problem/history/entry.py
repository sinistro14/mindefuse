#!/usr/bin/env python3.7

from typing import Tuple


class Entry:

    """round in which the guess was made"""
    round = int

    """secret sequence"""
    secret = str

    """guess submitted by the player"""
    guess = str

    """corresponding values of whites and reds"""
    answer = Tuple[int, int]

    """time passed since the problem started to be solved"""
    time = float

    def __init__(self, round_val: int, secret: str, guess: str, answer: Tuple[int, int], time: float):
        self.round = round_val
        self.secret = secret
        self.guess = guess
        self.answer = answer
        self.time = time

    def __str__(self):
        return "Round: {} | Secret: {} | Guess: {} | Result: ({}, {}) | Time: {:0>8.4f} s"\
            .format(self.round, self.secret, self.guess, self.answer[0], self.answer[1], self.time)
