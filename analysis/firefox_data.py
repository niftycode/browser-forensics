#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
chrome_data.py
Fetch data from the Chrome browser.
Python 3.7
Date created: 31.10.2018
"""

import os
import sys
from analysis import common_methods


def fetch_db_data():
    """
    Check the current operating system.
    Invoke the functions that check the database path,
    read the database file and
    print the data.
    """
    os_version = common_methods.system_info()
    history_file = 'places.sqlite'
    db = firefox_db_path(os_version, history_file)
    print("The path to the database is: {}".format(db))
    print()
    history_data = read_history(db)

    print("Show the id, the URL and the last visit date:")

    for line in history_data:

        (place_id, url, title, rev_host, visit_count, hidden, typed, frecency, last_visit_date,
         guid, foreign_count, url_hash, description, preview_image_url, origin_id) = line

        date = common_methods.convert_epoch(last_visit_date)

        print(f"id: {str(place_id)}\nURL: {url}\nDate: {str(date)}")
        print()


def firefox_db_path(operating_system, db_file):
    """
    Check the path to the history database file file.
    :param operating_system: The current operating system.
    :param db_file: The name of the database file.
    :return: The full path to the database.
    """
    profile_path = ''

    # Dictionary with the platform specific data paths
    platform_paths = {'Windows 7': 'C:\\Users\\{0}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(os.getlogin()),
            'Windows 8': 'C:\\Users\\{0}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(os.getlogin()),
            'Windows 10': 'C:\\Users\\{0}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(os.getlogin()),
            'Linux': '/home/{0}/.mozilla/firefox/'.format(os.getlogin()),
            'Darwin': '/Users/{0}/Library/Application Support/Firefox/Profiles'.format(os.getlogin())}

    # Check the operating system
    if operating_system == 'Windows 7':
        print('Sorry, this Windows 7 is currently not supported!')
    elif operating_system == 'Windows 8':
        print('Sorry, this Windows 8 is currently not supported!')
    elif operating_system == 'Windows 10':
        profile_path = platform_paths['Windows 10']
    elif operating_system == 'Linux':
        print('Sorry, this Windows 8 is currently not supported!')
    elif operating_system == 'macOS':
        profile_path = platform_paths['Darwin']
    else:
        print('Error: Unknown Operating System!')

    # Try to find the x.default directory
    # in Firefox' Profiles folder.
    try:
        for item in os.listdir(profile_path):
            # Check for the x.default directory
            # and return the database file's path
            if os.path.isdir(os.path.join(profile_path, item)) and 'default' in item:
                if os.path.isfile(os.path.join(profile_path, item, db_file)):
                    return os.path.join(profile_path, item, db_file)
    except FileNotFoundError as e:
        print(e)
        sys.exit("Could not find Firefox Profiles folder! Are you sure Firefox is installed on this system?")


def read_history(history_db):
    """
    Read the history database file (places.sqlite) and
    show the id, the url and the last visit date.
    :param history_db: The name of the database file.
    """

    sql_command = "SELECT * FROM moz_places"
    rval = common_methods.fetch_db_data(history_db, sql_command)
    return rval
