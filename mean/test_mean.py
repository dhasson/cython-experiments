# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:30:18 2020

@author: dhassona
"""

#!python setup.py build_ext --inplace --force

import mean
import numpy as np
import time

# Python program to get average of a list 
# Using reduce() and lambda 

# importing reduce() 
from functools import reduce

def Average(lst): 
	return reduce(lambda a, b: a + b, lst) / len(lst) 

np.random.seed(0)

n_reps = 50
avg_cython = 0
avg_python = 0
avg_numpy = 0
t_cython, t_python, t_numpy = 0,0,0


size = int(1e6)

for i in range(n_reps):
    x = np.random.rand(size)
    
    t0 = time.time()
    avg_cython = mean.cython_mean(x)
    t_cython += time.time()-t0
        
    t0 = time.time()
    avg_python = Average(x) 
    t_python += time.time()-t0
    
#    t0 = time.time()
#    avg_numpy = np.mean(x)
#    t_numpy += time.time()-t0

print("speedup = ", t_python/t_cython)