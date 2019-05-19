#! usr/bin/env python3.7

import csv
from typing import List, Tuple
from collections import namedtuple

from mindefuse import Mindefuse
from .problem_converter import ProblemConverter
from .engine_config import EngineConfig as Config


class Engine:

    @staticmethod
    def evaluate(tests: List[Tuple]):
        """
        Evaluates and writes the results of a test suite into a CSV file
        :param tests: list of tuples with arguments to use during testing
        """

        Args = namedtuple('Args', Config.TEST_FIELDS)

        with open(Config.OUTPUT_FILE, mode=Config.EDIT_MODE) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=Config.FIELD_NAMES)

            writer.writeheader()

            for test in tests:
                args = Args(*test)

                Engine.feedback(args)

                result = Mindefuse(verbose=False).solve_problem(
                    rounds=args.rounds,
                    algorithm=args.algorithm,
                    secret=args.secret,
                )
                writer.writerow(ProblemConverter.convert(args.secret, args.algorithm, result))

    @staticmethod
    def feedback(args):
        """
        Provide information about the currently active test
        :param args: named tuple of arguments used in the test
        """
        print("Running - Strategy: {}, Rounds: {}, Secret: {}".format(args.algorithm, args.rounds, args.secret))
