#!/usr/bin/env python3.7

import os
import sys
from .cmd import MainCommand
from .mindefuse import Mindefuse


def main():
    application = Mindefuse()
    MainCommand(application).run()
    exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting application.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
