#! usr/bin/env python3.7


class CommandConfigurations:
    """
    Definition of arguments accepted by the parser
    """

    # Main cmd configuration
    APPLICATION = "Mindefuse"

    # Parser configuration
    NAME = "run_strategy"
    DESCRIPTION = "Generates a problem, with the defined number of rounds and a secret of a given type and size" \
                  "TODO adapt later"

    ALGORITHM = "algorithm"
    TYPE = "type"
    ROUNDS = "rounds"
    SIZE = "size"
    SECRET = "secret"
