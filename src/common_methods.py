#!/usr/bin/env python3

"""
chrome_data.py
Common methods.
Python 3.7+
Date created: October 31st, 2018
"""

import sqlite3
import platform
import sys
from datetime import datetime as dt


def system_info():
    """
    Check the running operating system.
    :return: Operating system name (and Windows version).
    """
    if platform.system() == "Darwin":
        return "macOS"
    elif platform.system() == "Linux":
        return "Linux"
    elif platform.system() == "Windows":
        version = platform.system() + " " + platform.release()
        return version


def fetch_db_data(db, command):
    """
    Send queries to the sqlite database and return the results.
    :param db: The path to the database.
    :param command: The Sqlite command.
    :return:
    """
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(command)
        return cur.fetchall()
    except Exception as e:
        sys.exit("Error reading the database: %s" % e)


def convert_epoch(timestamp):
    """
    Convert epoch to human-readable date
    :param timestamp: The epoch timestamp.
    :return: The human-readable date.
    """
    try:
        rval = dt.fromtimestamp(timestamp / 1000000).ctime()
    except Exception as e:
        rval = "No date available (NULL value in database)."
        print(e)
    return rval
