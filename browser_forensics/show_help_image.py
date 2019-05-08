#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
safari_data.py
Fetch data from the Safari browser.
Python 3.7
Date created: 14.11.2018
"""

from PIL import Image


def show_image():
    image = Image.open("browser_forensics/img/help.png", "r")
    image.show()
