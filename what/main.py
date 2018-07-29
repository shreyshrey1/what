import logging
import sys
from what import __version__
from what.argparser import ArgParser
from .rerun import getLastOutput, getError
import webbrowser

def set_log_level(parsed_args):
    logger = logging.getLogger()
    if parsed_args.verbose:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

def main():
    parser = ArgParser()
    parsed_args = parser.parse()
    set_log_level(parsed_args)
    if parsed_args.help:
        parser.print_help()
    elif parsed_args.version:
        parser.print_version(__version__)
    elif parsed_args.action:
        if parsed_args.action == "google":
            x = getLastOutput()
            webbrowser.open("https://www.google.com/search?q=" + x)
        elif parsed_args.action == "stack":
            x = getLastOutput()
            print(x)
            webbrowser.open("https://stackoverflow.com/search?q=" + x)
        else:
            print("Invalid Argument, please try again")     
    else:
        return "hi"
        x = getError()
        print(x)
        webbrowser.open("https://www.google.com/search?q=" + x)