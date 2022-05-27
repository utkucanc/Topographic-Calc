# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:36:42 2022

@author: PC
"""

from . import _version
__version__ = _version.__version__
del _version

_plugins = [
    "geodatic",
    "core",
    "basicalc"
    ]