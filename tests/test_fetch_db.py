#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import os
import sqlite3
from src import common_methods


@pytest.fixture(scope="function")
def initialize_db(tmpdir):
    file = os.path.join(tmpdir.strpath, "test.db")
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    cur.executescript(
        """
    DROP TABLE IF EXISTS Urls;

    CREATE TABLE Urls (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    url    TEXT UNIQUE
    );
    """
    )

    cur.execute(
        """INSERT OR IGNORE INTO Urls(id, name, url)
        VALUES ( ?, ?, ?)""",
        (101, "Google", "https://google.com"),
    )

    conn.commit()

    yield file
    conn.close()


def test_fetch_db_data(initialize_db):
    command = "SELECT * FROM urls"
    rval = common_methods.fetch_db_data(initialize_db, command)  # returns a list
    assert rval == [(101, "Google", "https://google.com")]
