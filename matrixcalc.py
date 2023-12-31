# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:46:49 2023

@author: PC
"""

import math
from . import core
import numpy as np

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
    def GetMatrixFromFile(file):
        """
        

        Parameters
        ----------
        file : Txt File Folder
        Example txt file:
            
            0,0,0,0,0,0,0,0,0,0
            0,0,0,0,0,0,0,0,0,0
            0,0,0,0,0,0,0,0,0,0
            0,0,0,0,0,0,0,0,0,0
            0,0,0,0,0,0,0,0,0,0
            0,0,0,0,0,0,0,0,0,0
            0,0,2,1,0,2,0,0,0,0
            0,0,2,1,1,2,2,0,0,1
            0,0,1,2,2,1,1,0,0,2
            1,0,1,1,1,2,1,0,2,1

        Returns
        -------
        matris : TYPE
            Matris

        """
        with open(file, 'r') as f:
            matris = [[int(num) for num in line.split(',')] for line in f]
        return matris
    def Matrixadd(matris1,matris2):
        """
        

        Parameters
        ----------
        matris1 : Matrix
            
        matris2 : Matrix
            DESCRIPTION.

        Returns
        -------
        result : TYPE
            DESCRIPTION.

        """
        sh1 = np.array(matris1).shape
        sh2 = np.array(matris2).shape
        row = sh1[0]
        result = [[0 for _ in range(row)] for _ in range(row)]
        if sh1 == sh2 :
            i,j = 0
            for i in range(sh1[0]):
                for j in range(sh1[0]):
                    result[i][j] = matris1[i][j] + matris2[i][j]
           # print(result)
        
        return result
    def MatrixSubtraction(matris1,matris2):
        """
        

        Parameters
        ----------
        matris1 : Matrix
            
        matris2 : Matrix
            DESCRIPTION.

        Returns
        -------
        result : TYPE
            DESCRIPTION.

        """
        sh1 = np.array(matris1).shape
        sh2 = np.array(matris2).shape
        row = sh1[0]
        result = [[0 for _ in range(row)] for _ in range(row)]
        if sh1 == sh2 :
            i,j = 0
            for i in range(sh1[0]):
                for j in range(sh1[0]):
                    result[i][j] = matris1[i][j] - matris2[i][j]
            
        
        return result
class multi():
    def __init__(self):
        return self