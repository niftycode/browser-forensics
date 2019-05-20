#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from browser_forensics import common_methods

"""
def test_convert_epoch_is_equal():
    timestamp = 1551173630212966
    rval = common_methods.convert_epoch(timestamp)
    assert rval == "Tue Feb 26 10:33:50 2019"
"""

def test_convert_epoch_is_not_equal():
    timestamp = 1551173629692660
    rval = common_methods.convert_epoch(timestamp)
    assert rval != "Tue Feb 26 10:33:50 2019"
