#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_plugz
----------------------------------

Tests for `plugz` module.
"""

import pytest
import plugz
from plugz import errors
from plugz.pluginbase import PluginTypeBase

def test_loading_plugins_without_correct_arguments():
    """ Loading Plugins without giving valid arguments should fail.

    Make sure this is actually the case by going through different
    scenarios regarding invalid plugin types.

    """
    # if None is passed as type, the according error needs to be raised
    with pytest.raises(errors.NoValidPluginTypeError):
        plugins = plugz.load_plugins([], None)

    # create class object that is not a valid type
    # because it does not inherit from the correct class
    class MyInvalidType():
        pass

    # if an invalid PluginType is given, the according error is raised
    with pytest.raises(errors.InvalidPluginTypeError):
        plugins = plugz.load_plugins([], MyInvalidType)

    class MyValidType(PluginTypeBase):
        pass

    # if no paths are given, raise the according error
    with pytest.raises(errors.NoPluginPathsProvided):
        plugins = plugz.load_plugins([], MyValidType)

    # if paths are given but one is invalid, raise the error
    with pytest.raises(errors.InvalidPluginPath):
        plugins = plugz.load_plugins(['/invalid/path/' ], MyValidType)
