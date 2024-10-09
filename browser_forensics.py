#!/usr/bin/env python3

"""
browser_forensics.py
The main file with the entry point for this program.
Python 3.11+
Author: niftycode
Date created: October 28th, 2018
Date modified: October 9th, 2024
"""

import argparse
import logging.config
import sys

from logging.config import fileConfig

from src import chrome_data
from src import firefox_data
from src import safari_data

VERSION = "1.3.0"

# Add logger config
fileConfig("logging.ini")
logger = logging.getLogger()


def get_parser():
    """
    The options the user can choose.
    :return: The selected option.
    """
    parser = argparse.ArgumentParser(
        "browser_forensic.py: \
    A tool for reading the browser's history file.\n"
    )

    parser.add_argument(
        "-b",
        "--browser",
        help="Selected browser",
        nargs="?",
        choices=["Chrome", "Firefox", "Safari"],
    )

    """
    parser.add_argument(
        '-c', '--chrome', help="Select the Chrome browser", action='store_true')
    parser.add_argument('-f', '--firefox',
                        help="Select the Firefox browser", action='store_true')
    parser.add_argument('-s', '--safari',
                        help="Select the Safari browser", action='store_true')
    """

    parser.add_argument(
        "-o", "--output", help="Create output file", action="store_true"
    )

    parser.add_argument(
        "-v", "--version", help="Displays the current version", action="store_true"
    )

    args = parser.parse_args()
    return args


def evaluate(args):
    """
    Evaluate the given arguments.
    :param args: User's input
    """

    output = False

    if not args.output:
        if args.browser == "Chrome":
            # chrome_data.fetch_db_data()
            print("Chrome browser is not currently supported")
        elif args.browser == "Firefox":
            firefox_data.fetch_db_data()
        elif args.browser == "Safari":
            # safari_data.fetch_db_data()
            print("Safari browser is not currently supported.")
        elif args.version:
            print("This is version {0}.".format(VERSION))
            print()
        else:
            print("Missing argument! Type '-h' for available arguments.")
    else:
        output = True

    """
    if not args.output:
        if args.chrome:
            chrome_data.fetch_db_data()
        elif args.firefox:
            firefox_data.fetch_db_data()
        elif args.safari:
            safari_data.fetch_db_data()
        elif args.version:
            print('This is version {0}.'.format(VERSION))
            print()
        else:
            print("Missing argument! Type '-h' for available arguments.")
    else:
        print("Argument '-o' selected.")
    """


def main():
    """
    The entry point of this program.
    """
    args = get_parser()
    sys.stdout.write(str(evaluate(args)))


if __name__ == "__main__":
    print("\n\n    #### A Python script to analyze browser data ####")
    print("    #               Created by niftycode            #")
    print(f"    #                  Version {VERSION}                #")
    print("    #################################################\n\n")
    print()
    main()
