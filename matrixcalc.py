# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:46:49 2023

@author: PC
"""

import math
from . import core

class basic():
    def __init__(self):
        return self
    def MainTranspose(matris):
        result = [[j for j in i] for i in zip(*matris)]
        return result
    def SideTranspose(matris):
        result = [[j for j in i] for i in zip(*matris[::-1])][::-1]
        return result
    def VerticalTranspose(matris):
        result = [i[::-1] for i in matris]
        return result
    def HorizonalTranspose(matris):
        result = matris[::-1]
        return result
    def CreatPMatrix(row,distance = 1):
        """
        

        Parameters
        ----------
        row : NUMBER
            DESCRIPTION.
        distance : TYPE, optional
            DESCRIPTION. The default is 1.

        Returns
        -------
        result : TYPE
            DESCRIPTION.

        """
        matris = [[0 for _ in range(row)] for _ in range(row)]
        i = 0
        for i in range(row):
            matris[i][i] = 1/distance
            i = i+1
        result = 0
        return result
    
class multi():
    def __init__(self):
        return self