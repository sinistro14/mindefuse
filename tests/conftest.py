#! usr/bin/env python3.7

import pytest
from mindefuse import Mindefuse
from mindefuse.problem.history import History


class Helper:
    """
    Helper class used for more flexible access to helper methods and constants
    """

    @staticmethod
    def assert_knuth(history: History, expected):

        for entry, answer in zip(history.entries, expected):
            assert entry.guess == answer


@pytest.fixture(scope="class")
def helper():
    """
    Return Helper class
    """
    return Helper()


@pytest.fixture(scope="function")
def mindefuse():
    return Mindefuse()
