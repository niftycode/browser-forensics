# browser_forensics

![](img/license-MIT-green.svg) ![](img/python-3.11-blue.svg) ![](https://img.shields.io/github/last-commit/niftycode/browser_forensics.svg?style=flat) ![](https://img.shields.io/github/issues/niftycode/browser_forensics.svg?style=flat) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is a forensic tool written in Python 3. Use this tool to fetch the content of the *history* file (Firefox, Chrome and Safari) on macOS and Windows 11 operating systems. *Currently only Firefox is supported.*

## Supported OS

* macOS (Firefox)
* ~~Windows 10~~
* Linux (Firefox)

## Supported Browser

* ~~Chrome~~
* Firefox
* ~~Safari~~

## Requirements

* pillow
* pytest

Use

    pip3 install -r requirements.txt

to install these packages.

## Usage

Change to the *browser_forensics* directory and start the program with

    # Firefox browser
    python browser_forensics.py -b firefox

Since this is a program written in Python 3 you may use

    python3 browser_forensics.py -b firefox

on UNIX-like systems.

**Note**: Mac users need access to the *Library* folder in order to read the database files. You can add access (for *Terminal* or *iTerm*) in

    > Settings > Security & Privacy > Privacy > Full Disk Access

## ToDo

* Add list with installed browsers
* ~~Add Linux support~~
* Add Chrome support (Linux)
* Add data export (CSV, JSON, Excel?)
* Add more Unit Tests
