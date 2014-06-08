import os
import sys
from collections import defaultdict

from pluginbase import PluginTypeBase
import errors

_loaded_plugins = defaultdict(list)

def register_plugin(f):
    """

    will be used as decorator
    """
    # add tests here TODO

    # register the plugin in the system
    _loaded_plugins[f.type].append(f)
    # now just return the collable which is a plugin class in this case
    return f


def load_plugins(paths, plugintype):
    """
    """

    # check if the given path is None
    if not plugintype:
        raise errors.NoValidPluginTypeError()

    # check if the given PluginType really is a subclass
    # of the provided PluginTypeBase
    elif not issubclass(plugintype, PluginTypeBase):
        raise errors.InvalidPluginTypeError()

    # if no paths are given, complain.
    elif not paths:
        raise errors.NoPluginPathsProvided()

    # if an invalid path is given, report that problem
    else:
        for path in paths:
            if not os.path.isdir(path):
                raise errors.InvalidPluginPath()

    # otherwise all data is valid for loading some plugins
    for path in paths:
        # find all the files and try to register them as plugins
        sys.path.insert(0, path)
        for pf in os.listdir(path):
            if plugintype.is_valid_file(pf):
                try:
                    base = os.path.basename(pf).split(os.path.extsep)[0]
                    _load_plugin(base)
                except IndexError:
                    # this should never happen if the is_valid_file() method
                    # checks proper file extensions. Just check next file.
                    continue
        sys.path.pop(0)


def _load_plugin(plugin_name):
    # TODO, make this proper logged stuff. -- Matti.
    print 'trying to load', plugin_name
    p = __import__(plugin_name)
    print 'list of plugins now:', plugin_name
