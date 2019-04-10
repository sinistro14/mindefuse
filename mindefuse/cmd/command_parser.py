#! usr/bin/env python3.7

import argparse
from .command_configurations import CommandConfigurations as Config
from ..problem import SecretTypes
from ..strategy import StrategyTypes


class CommandParser:
    """
    Mindefuse CLI Parser
    """

    def __init__(self):

        # argument parser
        self.__parser = argparse.ArgumentParser(
            prog=Config.NAME,
            description=Config.DESCRIPTION,
        )

        # number of rounds
        self.__parser.add_argument(
            self.__set_sopt(Config.ROUNDS),
            self.__set_opt(Config.ROUNDS),
            action="store",
            type=int,
            required=True
        )

        # algorithm identifier
        self.__parser.add_argument(
            self.__set_sopt(Config.ALGORITHM),
            self.__set_opt(Config.ALGORITHM),
            action="store",
            default=None,
            choices=[StrategyTypes.KNUTH, StrategyTypes.GENETIC, StrategyTypes.SWASZEK]
        )

        # type of secret
        self.__parser.add_argument(
            self.__set_sopt(Config.TYPE),
            self.__set_opt(Config.TYPE),
            action="store",
            default=None,
            choices=[SecretTypes.NUMERIC, SecretTypes.LSTRING, SecretTypes.STRING]
        )

        # size of secret
        self.__parser.add_argument(
            self.__set_sopt(Config.SIZE),
            self.__set_opt(Config.SIZE),
            action="store",
            type=int,
            default=None
        )

        # user provided secret
        self.__parser.add_argument(
            self.__set_opt(Config.SECRET),
            action="store",
            default=None
        )

    @staticmethod
    def __set_opt(option):
        """
        Generates a cmd argument identifier of a given option
        :param option: option to use as argument identifier
        :return: argument identifier
        """
        return "--" + option

    @staticmethod
    def __set_sopt(option):
        """
        Generates a shortened cmd argument identifier of a given option
        :param option: option to use as shortened argument identifier
        :return: shortened argument identifier
        """
        return "-" + option[0]

    def usage(self):
        """
        Prints the parser usage information
        """
        self.__parser.print_help()

    def parse(self, args):
        """
        Parses a set of arguments
        :param args: arguments to parse into Problem specs
        :return: Problem if arguments are successfully parsed, None, otherwise
        """
        try:
            return self.__parser.parse_args(args.split())
        except SystemExit:
            return None
