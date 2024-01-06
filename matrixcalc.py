# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:46:49 2023

@author: PC
"""

import math
from core import *
import numpy as np

class basic():
    def __init__(self):
        return self
    #Matrix Transpose 
    def MainTranspose(matris):
        if type(matris) != np.ndarray():
            if type(matris) == list:
                matris = np.array(matris)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris)
        result = [[j for j in i] for i in zip(*matris)]
        return result
    def SideTranspose(matris):
        if type(matris) != np.ndarray():
            if type(matris) == list:
                matris = np.array(matris)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris)
        result = [[j for j in i] for i in zip(*matris[::-1])][::-1]
        return result
    def VerticalTranspose(matris):
        if type(matris) != np.ndarray():
            if type(matris) == list:
                matris = np.array(matris)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris)
        result = [i[::-1] for i in matris]
        return result
    def HorizonalTranspose(matris):
        if type(matris) != np.ndarray():
            if type(matris) == list:
                matris = np.array(matris)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris)
        result = matris[::-1]
        return result
    #Matrix Basic Calc
    def MatrixDot(matris1,matris2):
        #Checking tp type
        if type(matris1) != np.ndarray():
            if type(matris1) == list:
                matris1 = np.array(matris1)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris1)
        if type(matris2) != np.ndarray():
            if type(matris2) == list:
                matris1 = np.array(matris2)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris2)        
            
        result = np.dot(matris1,matris2)
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
        
        return matris
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
        if type(matris1) != np.ndarray():
            if type(matris1) == list:
                matris1 = np.array(matris1)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris1)
        if type(matris2) != np.ndarray():
            if type(matris2) == list:
                matris1 = np.array(matris2)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris2)   
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
        if type(matris1) != np.ndarray():
            if type(matris1) == list:
                matris1 = np.array(matris1)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris1)
        if type(matris2) != np.ndarray():
            if type(matris2) == list:
                matris1 = np.array(matris2)
            else:
                print("You must be use Numpy array or Python List. Error:")
                print(matris2)   
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
    def getCofactor(A, temp, p, q, n):
 
        i = 0
        j = 0
     
        # Looping for each element of the matrix
        for row in range(n):
     
            for col in range(n):
     
                # Copying into temporary matrix only those element
                # which are not in given row and column
                if (row != p and col != q):
     
                    temp[i][j] = A[row][col]
                    j += 1
     
                    # Row is filled, so increase row index and
                    # reset col index
                    if (j == n - 1):
                        j = 0
                        i += 1
    
    # def MatrixDeterminant(A, n):
 
    #     temp1 = 0
         
    #     # Base case : if matrix contains single element
    #     if (n == 1):
    #         return A[0][0]
         
    #     temp = []   # To store cofactors
    #     for i in range(n):
    #         temp.append([None for _ in range(n)])
         
    #     sign = 1   # To store sign multiplier
         
    #     # Iterate for each element of first row
    #     for f in range(n):
         
    #         # Getting Cofactor of A[0][f]
    #         basic.getCofactor(A, temp, 0, f, n)
    #         temp1 += sign * A[0][f] * MatrixDeterminant(temp, n - 1)
         
    #         # terms are to be added with alternate sign
    #         sign = -sign
         
    #     return temp1
    # """
    # toplama
    # çıkarma
    # çarpma
    # tersi
    # determinant
    # tersi
    # üstü
    # """
class multi():
    def __init__(self):
    
        return self


# test = basic.CreatPMatrix(5,1544.256)
# print(test)