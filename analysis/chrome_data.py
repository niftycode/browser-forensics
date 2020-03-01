#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
chrome_data.py
Fetch data from the Chrome browser.
Python 3.7
Date created: 22.10.2018
"""

import os
import sys
from analysis import common_methods


def fetch_db_data():
    """
    Check the current operating system.
    Invoke the functions that check the database path and read the database file.
    """

    os_version = common_methods.system_info()

    history_file = ''

    if os_version == 'Windows 10':
        history_file = 'History'
    elif os_version == 'macOS':
        history_file = 'history'
    elif os_version == 'Linux':
        print('Sorry, Linux is not supported!')

    db = chrome_db_path(os_version, history_file)
    print("The path to the database is: {}".format(db))
    print()

    history_data = read_history(db)

    for line in history_data:
        (id, url, title, visit_count, typed_count, last_visit_time, hidden) = line

        print(f"id: {str(id)}\nURL: {url}")
        print()


def chrome_db_path(operating_system, db_file):
    """
    Check the path to the history database file file.
    :param operating_system: The current operating system.
    :param db_file: The name of the database file.
    :return: The full path to the database.
    """

    default_path = ''

    # Dictionary with the platform specific data paths
    platform_paths = {'Windows 10': 'C:\\Users\\{0}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'.format(os.getlogin()),
                      'Linux': '/home/{0}/.config/google-chrome/Default/databases/'.format(os.getlogin()),
                      'Darwin': '/Users/{0}/Library/Application Support/Google/Chrome/Default/'.format(os.getlogin())}

    # Check the operating system
    if operating_system == 'Windows 7':
        print('Sorry, Windows 7 is currently not supported!')
    elif operating_system == 'Windows 8':
        print('Sorry, Windows 8 is currently not supported!')
    elif operating_system == 'Windows 10':
        default_path = platform_paths['Windows 10']
    elif operating_system == 'Linux':
        print('Sorry, Linux is currently not supported!')
    elif operating_system == 'macOS':
        default_path = platform_paths['Darwin']
        print(default_path)
    else:
        print('Error: Unknown Operating System!')

    # Create the full path to the db file and return this path.
    if os.path.isfile(os.path.join(default_path, db_file)):
        return os.path.join(default_path, db_file)
    else:
        sys.exit("Could not find Chrome's Default folder! \
            Are you sure Chrome is installed on this system?")


def read_history(history_db):
    """
    Read the history database file.
    :param history_db: The name of the database file. 
    """
    sql_command = "SELECT * FROM urls"
    rval = common_methods.fetch_db_data(history_db, sql_command)
    return rval

    """
    for i in rval:
        print(i)
    """
