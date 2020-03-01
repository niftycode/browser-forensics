#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
show_help_image.py
Fetch data from the Safari browser.
Python 3.7
Date created: 09.05.2019
"""

from PIL import Image


def show_image():
    image = Image.open("browser_forensics/img/help.png", "r")
    image.show()
