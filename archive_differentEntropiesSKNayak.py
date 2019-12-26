#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - 

Created on Sat Aug 17 15:38:01 2019
@author: k as root
"""

import numpy as np
import pyrem as pr                       #[1]
from pyentrp import entropy as ent       #[2]
import ite                               #[3]

a = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
# m =
# r = 
# tau = 
# de = 
std_a = np.std(a)
len_a = len(a)

#Approximate entropy [1]
pyrem.univariate.ap_entropy(a, m, R) 

#Sample entropy [1]
pyrem.univariate.samp_entopy(a, m, R, tau=1, relative_r=True)
sampleEntropy = ent.sample_entropy(a, 4, 0.2 * std_a)

#Fuzzy entropy

#Kolgomorov-smai entropy

#Multiscale entropy [2]
multiscaleEntropy = ent.multiscale_entropy(a, len_a)#, tolerance = None, maxscale = None)

#permutation entropy [2]
permutationEntropy = ent.permutation_entropy(a)#, order=3, delay=1, normalize=False)

#Shannon entropy [2]
ShannonEntropy = ent.shannon_entropy(a)

#Reniys entropy [3]

#Tsallis entropy [3]

#Wavelet entropy

#Hjorth parameter [1]
pyrem.univariate.hjorth(a)


##OTHERS
#Singular value decomposition entropy [1]
pyrem.univariate.svd_entropy(a, tau, de)
 
#Spectral entropy [1]
pyrem.univariate.spectral_entropy(a, sampling_freq, bands=None)




#1. http://gilestrolab.github.io/pyrem/pyrem.univariate.html
#download 1:https://github.com/gilestrolab/pyrem/blob/master/src/pyrem/univariate.py  
#2. https://github.com/nikdon/pyEntropy
#3. https://bitbucket.org/szzoli/ite-in-python/src/default/