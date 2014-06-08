import abc

class PluginTypeBase(object):

    __metaclass__ = abc.ABCMeta

    @staticmethod
    def is_valid_file(file):
        """ """
        return file.endswith('.py')

    def __init__(self ):
        pass
