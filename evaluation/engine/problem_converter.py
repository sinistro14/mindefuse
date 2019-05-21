#! usr/bin/env python3.7

from typing import Dict

from mindefuse.problem import Problem


class ProblemConverter:
    """
    Converter of test inputs and results into a simplified representation
    """

    @staticmethod
    def convert(secret: str, strategy, problem: Problem) -> Dict:
        """
        Convert the resultant test information into a simplified representation
        :param secret: secret to uncover
        :param strategy: strategy used to solve the problem
        :param problem: resultant problem
        :return: dict of the captured information
        """
        return {
            "secret": secret,
            "algorithm": strategy,
            "size": problem.secret_size(),
            "rounds": problem.turns_to_solve(),
            "solved": problem.solved(),
            "type": problem.secret_type(),
            "time": problem.time_to_solve(),
        }
