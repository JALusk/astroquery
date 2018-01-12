from astropy import config as _config

class Conf(_config.ConfigNamespace):
    """
    Configuration parameters for `astroquery.template_module`.
    """
    server = _config.ConfigItem(
        ['http://dummy_server_mirror_1',
         'http://dummy_server_mirror_2',
         'http://dummy_server_mirror_n'],
        'Name of the template_module server to use.'
        )
    timeout = _config.ConfigItem(
        30,
        'Time limit for connecting to template_module server.'
        )

from .core import QueryClass

__all__ = ['QueryClass']
