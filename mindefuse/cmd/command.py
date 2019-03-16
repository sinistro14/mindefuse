#! usr/bin/env python3.7

from cmd import Cmd


class Command(Cmd):

    __application = None

    def __init__(self, application):
        super().__init__()

        self.__application = application

        self.aliases = {
            "q":    self.do_exit,
        }

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
        cmd, arg, line = self.parseline(line)
        if cmd in self.aliases:
            self.aliases[cmd](arg)
        else:
            self.stdout.write("Unknown command: '{}'\n".format(line))

    def do_exit(self, args):
        """Exists the application"""
        print("Exiting {}...".format(self.shell_name()))
        raise SystemExit
