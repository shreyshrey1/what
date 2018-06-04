import logging
import sys

from what import __version__
from what.argparser import ArgParser


def set_log_level(parsed_args):
    logger = logging.getLogger()
    if parsed_args.verbose:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)


def run_action(action):
    print(f'Hello Python World! Action is: `{action}`!')


def main():
    parser = ArgParser()
    parsed_args = parser.parse()
    set_log_level(parsed_args)
    if parsed_args.help:
        parser.print_help()
    elif parsed_args.version:
        parser.print_version(__version__)
    # elif parsed_args.action:
    else:
        print("hello world")
