class PluginTypeBase(object):

    @staticmethod
    def is_valid_file(file):
        """
        """
        if file.endswith('.py'):
            return True
        else:
            return False

    def __init__(self, ):
        pass
