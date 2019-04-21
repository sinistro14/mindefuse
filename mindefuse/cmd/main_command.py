#! usr/bin/env python3.7

from ..mindefuse import Mindefuse
from .command_base import CommandBase
from .command_parser import CommandParser
from .command_configurations import CommandConfigurations as Config


class MainCommand(CommandBase):
    """
    Mindefuse CLI
    """

    """application connected to this Cmd"""
    _application = Mindefuse

    """argument parser used for algorithm runs"""
    __command_parser = CommandParser

    def __init__(self, application, shell_name=Config.APPLICATION):

        super().__init__(application=application, shell_name=shell_name)

        # cmd introduction message
        self.intro = "Welcome to {}\nType help or ? to list the available commands\n".format(self._shell_name)

        self.__command_parser = CommandParser()

    def shell_name(self):
        """Returns prompt name"""
        if self._shell_name is None:
            raise NotImplementedError("Attribute should be defined.")
        return self._shell_name

    def do_generate_problem(self, args):
        """
        Generates a dummy problem and prints the secret sequence
        :param args: named tuple with construction arguments
        """
        args = self.__command_parser.parse(args)
        if args:
            problem = self._application.generate_problem(
                rounds=args.rounds,         # number of problem rounds
                secret_size=args.size,      # size of the secret sequence
                secret_type=args.type,      # type of secret, e.g. numeric, string...
                secret=args.secret          # secret directly provided by the user
            )
            problem.print_secret()

    def do_run_strategy(self, args):
        """
        Parses the input and builds a Problem with the provided set of arguments, solving it with a given strategy
        :param args: named tuple with construction arguments
        """
        args = self.__command_parser.parse(args)
        if args:
            self._application.solve_problem(
                rounds=args.rounds,         # number of problem rounds
                algorithm=args.algorithm,   # algorithm used ot solve the problem
                secret_size=args.size,      # size of the secret sequence
                secret_type=args.type,      # type of secret, e.g. numeric, string...
                secret=args.secret          # secret directly provided by the user
            )

    def help_run_strategy(self):
        """Helper for run_strategy command"""
        self.__command_parser.usage()
