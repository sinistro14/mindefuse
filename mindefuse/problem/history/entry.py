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

    def __init__(self, round_val: int, secret: str, guess: str, answer: Tuple[int, int]):
        self.round = round_val
        self.secret = secret
        self.guess = guess
        self.answer = answer

    def __str__(self):
        return "Round: {} | Secret: {} | Guess: {} | ({}, {})"\
            .format(self.round, self.secret, self.guess, self.answer[0], self.answer[1])
