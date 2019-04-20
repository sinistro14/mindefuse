#! usr/bin/env python3.7

import pytest
from mindefuse import Mindefuse
from mindefuse.problem import Problem


class Helper:
    """
    Helper class used for more flexible access to helper methods and constants
    """

    @staticmethod
    def assert_solved(problem: Problem, solved: bool):
        assert problem.solved() == solved


@pytest.fixture(scope="class")
def helper():
    """
    Return Helper class
    """
    return Helper()


@pytest.fixture(scope="function")
def mindefuse():
    return Mindefuse()
