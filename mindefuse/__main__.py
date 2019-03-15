#!/usr/bin/env python3.7

from .cmd import Command
from .mindefuse import Mindefuse


def main():
    application = Mindefuse()
    Command(application)
    exit(0)


if __name__ == "__main__":
    main()
