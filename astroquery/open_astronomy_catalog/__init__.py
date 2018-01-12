# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Open Astronomy Catalog Query Tool
======================================================

.. topic:: Revision History

    Created as part of the Hack Together Day at AAS 231 in 2018

    :Originally contributed by: Jeremy Lusk (jeremy.lusk@gmail.com)
"""

from astropy import config as _config

class Conf(_config.ConfigNamespace):
    """
    Configuration parameters for `astroquery.template_module`.
    """
    server = _config.ConfigItem(
            ['https://api.astrocats.space/'],
            'Name of the open_astronomy_catalog server to use.'
            )
    timeout = _config.ConfigItem(
              30,
              'Time limit for connecting to template_module server.'
              )

conf = Conf()
from .core import OAC, OACClass

__all__ = ['OAC', 'OACClass',
           'Conf', 'conf',
           ]
