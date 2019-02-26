#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
import sqlite3
import os
from browser_forensics import firefox_data
from browser_forensics import common_methods


@pytest.fixture(scope='function')
def initialize_firefox_db(tmpdir):
    file = os.path.join(tmpdir.strpath, "test.db")
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS History;

    # (place_id, url, title, rev_host, visit_count, hidden, typed, frecency, last_visit_date,
         guid, foreign_count, url_hash, description, preview_image_url, origin_id)

    CREATE TABLE Urls (
    place_id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    url   TEXT UNIQUE,
    title    TEXT UNIQUE,
    rev_host    TEXT UNIQUE,
    visit_count     INTEGER,
    hidden      INTEGER,
    typed       INTEGER,
    frecency    INTEGER,
    last_visit_date     INTEGER,
    guid        TEXT UNIQUE,
    foreign_count       INTEGER,
    url_hash        INTEGER,
    description     TEXT UNIQUE,
    preview_image_url   TEXT UNIQUE,
    origin_id   INTEGER
    );
    ''')

    cur.execute('''INSERT OR IGNORE INTO History(place_id, url, title, rev_host, visit_count, 
        hidden, typed, frecency, last_visit_date, guid, foreign_count, url_hash, description, 
        preview_image_url, origin_id)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (20, 'https://google.com', 'Google', 
        'ed.esieh.www.', 1, 0, 0, 2000, 1551173630212966, 'rlmKqPTvlzYv', 0, 47359477497507, 'Google Search', 
        'https://google.com/test.png', 11))

    conn.commit()

    yield file
    conn.close()


def test_firefox_db(initialize_firefox_db):
    command = "SELECT * FROM urls"
    rval = firefox_data.read_history(initialize_firefox_db, command)
    assert rval == [(20, 'https://google.com', 'Google', 
        'ed.esieh.www.', 1, 0, 0, 2000, 1551173630212966, 'rlmKqPTvlzYv', 0, 47359477497507, 'Google Search', 
        'https://google.com/test.png', 11)]
