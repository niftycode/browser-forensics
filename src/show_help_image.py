#!/usr/bin/env python3


"""
show_help_image.py
Python 3.11+
Date created: May, 9th, 2019
Date modified: October 9th, 2024
"""

from PIL import Image


def show_image():
    image = Image.open("src/img/help.png", "r")
    image.show()
    image.close()
