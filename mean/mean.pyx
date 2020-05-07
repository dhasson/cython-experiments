# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:26:53 2020

@author: dhassona
"""

from functools import reduce

def cython_mean(double[:] x):

    cdef double total = 0

    for i in range(len(x)):

        total += x[i]

    return total / len(x)


def cython_Average(double[:] lst):
    cdef double total = 0
    total = reduce(lambda a, b: a + b, lst)
    return total / len(lst) 