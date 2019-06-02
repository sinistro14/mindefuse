#!/usr/bin/env python3

import sys
import importlib
from pip._internal import main as pipmain


def install_and_import(package_id, package):
    """
    Tries to load a package, if unable to do so,
    tries to install it using pip and load it afterwards.
    """
    try:
        importlib.import_module(package)
    except ImportError:
        pipmain(['install', '--user', '-q', package_id])
    finally:
        globals()[package] = importlib.import_module(package)


def run_make(targets):
    import pymake
    options = ['-s']
    try:
        pymake.main(options + targets)
    except (pymake.PymakeTypeError, pymake.PymakeKeyError):
        print("Caught exception while parsing makefile.")


def main(args):
    install_and_import('py-make', 'pymake')
    run_make(args)


if __name__ == '__main__':
    main(sys.argv[1:])
