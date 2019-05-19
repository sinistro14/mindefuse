#! usr/bin/env python3.7

from .engine import Engine
from .evaluation_suite import EvaluationSuite


def main():
    Engine.evaluate(EvaluationSuite.suite)
    exit(0)


if __name__ == "__main__":
    main()
