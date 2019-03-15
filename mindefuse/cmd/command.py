#! usr/bin/env python3.7

from cmd import Cmd


class Command(Cmd):

    __application = None

    def __init__(self, application):
        super().__init__()

        self.__application = application

        self._shell_name = "mindefuse"
        self.intro = "Welcome to {}".format(self.shell_name())
        self.prompt = "({}) > ".format(self.shell_name())
        self.cmdloop('Starting prompt...')

    def shell_name(self):
        """Returns prompt name"""
        if self._shell_name is None:
            raise NotImplementedError("Attribute should be defined")
        return self._shell_name

    def default(self, line):
        """Overrides unknown command message"""
        self.stdout.write("Unknown command: '{}'\n".format(line))

    def do_exit(self, args):
        """Exists the application"""
        print("Exiting {}.".format(self.shell_name()))
        raise SystemExit

    def do_start(self, args):
        """Starts the application"""
        print("{} was started".format(self.shell_name()))
        self.__application.start()

    def do_stop(self, args):
        """Stops the application"""
        self.__application.stop()
        print("{} was stopped".format(self.shell_name()))
