# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:28:40 2020

@author: dhassona
"""

from distutils.core import setup
from Cython.Build import cythonize

import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

setup(

    ext_modules=cythonize("mean.pyx", annotate=True),

)
