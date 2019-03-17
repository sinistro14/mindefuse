#!/usr/bin/env python3.7

from .cmd import MainCommand
from .mindefuse import Mindefuse


def main():
    application = Mindefuse()
    MainCommand(application).run()
    exit(0)


if __name__ == "__main__":
    main()
