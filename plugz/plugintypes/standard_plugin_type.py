from abc import abstractmethod

from plugz import PluginTypeBase

class StandardPluginType(PluginTypeBase):
    """ Simple plugin type that requires an activate() method. """

    plugintype = 'StandardPluginType'

    def __init__(self, ):
        """ """
        super(StandardPluginType).__init__(self)

    @abstractmethod
    def activate(self):
        """ """
        raise NotImplementedError, self.__class__
