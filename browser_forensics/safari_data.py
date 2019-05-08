#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
safari_data.py
Fetch data from the Safari browser.
Python 3.7
Date created: 14.11.2018
"""

import os
import sys
from browser_forensics import common_methods
from browser_forensics import show_help_image


def fetch_db_data():
    """
    Check the current operating system.
    Invoke the functions that check the database path and
    read the database file.
    """
    os_version = common_methods.system_info()
    history_file = 'History.db'

    if os_version != 'macOS':
        print("Safari's history file is only on macOS available.")
        sys.exit()

    print("Your Terminal application needs full disc access to read Safari's database file.")
    print("You can add this access in the 'Secure & Privacy' section.")
    print()
    answer = input("Do you need additional help? (y/N): ")

    if answer == 'n' or ' ':
        db = safari_db_path(history_file)
        print()
        print("The path to the database is: {}".format(db))
        print()
        read_history(db)
    else:
        show_help_image.show_image()
        print()
        print("Add full disk access as shown in the image and restart.")
        print()
        sys.exit()
        # TODO - 08.05.2019: Add a conf file with default value.


def safari_db_path(db_file):

    default_path = '/Users/{0}/Library/Safari/'.format(os.getlogin())

    # Create the full path to the db file and return this path.
    if os.path.isfile(os.path.join(default_path, db_file)):
        return os.path.join(default_path, db_file)
    else:
        print()
        sys.exit("Could not find Safari's 'History.db' database.\n"
                 "Did you really copy the database to your Documents folder?")


def read_history(history_db):
    """
        Read the history database file.
        :param history_db: The name of the database file.
        """
    sql_command = "SELECT * FROM history_items"
    # sql_command = "SELECT * FROM history_visits"
    rval = common_methods.fetch_db_data(history_db, sql_command)

    for i in rval:
        print(i)
