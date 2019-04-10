#! usr/bin/env python3.7

from .command_base import CommandBase
from .command_parser import CommandParser
from ..mindefuse import Mindefuse
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
        self.intro = "Welcome to {}\nType help or ? to list commands\n".format(self._shell_name)

        self.__command_parser = CommandParser()

    def shell_name(self):
        """Returns prompt name"""
        if self._shell_name is None:
            raise NotImplementedError("Attribute should be defined")
        return self._shell_name

    def __create_problem(self, args):
        """
        Creates a problem with a given set of arguments
        :param args: named tuple with Problem construction arguments
        """
        problem = self._application.solve_problem(
            rounds=args.rounds,         # number of problem rounds
            secret_size=args.size,      # size of the secret sequence
            secret_type=args.type,      # type of secret, e.g. numeric, string...
            secret=args.secret          # secret directly provided by the user
        )
        print(problem.check_secret())  # TODO remove later

    def do_run_strategy(self, args):
        """
        Parses the input and builds a Problem with the provided set of arguments
        :param args: named tuple with construction arguments
        """
        args = self.__command_parser.parse(args)  # returns a Problem or None
        if args:
            self.__create_problem(args)

    def help_run_strategy(self):
        """Helper for run_strategy command"""
        self.__command_parser.usage()
