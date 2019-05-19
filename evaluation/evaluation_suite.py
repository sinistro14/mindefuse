#! usr/bin/env python3.7

from mindefuse.strategy import StrategyTypes


class EvaluationSuite:
    """
    Parameters to use during the evaluation tests
    """

    suite = [
        # algorithm, rounds, secret
        (StrategyTypes.KNUTH, 12, "123"),
    ]
