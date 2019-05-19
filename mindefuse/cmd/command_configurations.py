#! usr/bin/env python3.7


class CommandConfigurations:
    """
    Definition of arguments accepted by the parser
    """

    # Main cmd configuration
    APPLICATION = "mindefuse"

    # Parser configuration
    NAME = "run_strategy"
    DESCRIPTION = "Generates a problem, with the defined number of rounds and a secret of a given type and size. " \
                  "If --secret is provided, all other specifications, except the number of rounds and strategy, " \
                  "will be overridden."

    ALGORITHM = "algorithm"
    TYPE = "type"
    ROUNDS = "rounds"
    SIZE = "size"
    SECRET = "secret"
