#! usr/bin/env python3.7

from cmd import Cmd


class CommandBase(Cmd):
    """
    Base skeleton for Mindefuse CLI
    """

    def __init__(self, application, shell_name: str, sub_shell_name=None):
        super().__init__()

        self._application = application

        self._shell_name = "{}".format(shell_name, sub_shell_name)

        if sub_shell_name:
            self._shell_name = "{}-{}".format(self._shell_name, sub_shell_name)

        self.prompt = "({}) > ".format(self._shell_name)

    def run(self):
        """Starts the cmd input loop"""
        self.cmdloop()

    def _stop(self):
        """Stops and exits the cmd"""
        return True

    def _help(self):
        """Prints the cmd help information"""
        self.onecmd('help')

    def do_exit(self, args):
        """Exists the application"""
        print("Exiting the application...")
        raise SystemExit

    def shell_name(self):
        """Returns prompt name"""
        if self._shell_name is None:
            raise NotImplementedError("Attribute should be defined")
        return self._shell_name

    def default(self, line):
        """Overrides unknown command message"""
        self.stdout.write("Unknown command: '{}'\n".format(line))
        self._help()

    def emptyline(self):
        """Overrides the default behaviour of an empty line repeating the previous command"""
        pass
