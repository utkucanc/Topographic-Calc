# -*- coding: utf-8 -*-
"""
Created on Fri May 27 02:10:52 2022

@author: UCC
"""

a=[6377397.155,6378388.000,6378137.000]
b=[6356078.963,6356911.946,6356752.314]
c=[6398786.849,6399936.608,6399593.626]
f1=[299.1528,297,298.257222101]
e=[0.00667437,0.00672267,0.0066943800]
e2=[0.00671922,0.00676817,0.0067394968]
n=[0.00167418,0.00168634,0.0016792204]

class Bassel:
    na = a[1]
    nb = b[1]
    nc = c[1]
    nf1 = f1[1]
    ne = e[1]
    ne2 = e2[1]
    nn = n[1]
    def printveriable():
        na = a[1]
        nb = b[1]
        nc = c[1]
        nf1 = f1[1]
        ne = e[1]
        ne2 = e2[1]
        nn = n[1]
        print("a"+str(na))
        print("b"+str(nb))
        print("c"+str(nc))
        print("1/f"+str(nf1))
        print("e"+str(ne))
        print("e'^2"+str(ne2))
        print("n"+str(nn))
        
    def __init__(self):
        return self
    
class Hayford:
    na = a[2]
    nb = b[2]
    nc = c[2]
    nf1 = f1[2]
    ne = e[2]
    ne2 = e2[2]
    nn = n[2]
    def __init__(self):
        return self
    
class RS1980:
    na = a[3]
    nb = b[3]
    nc = c[3]
    nf1 = f1[3]
    ne = e[3]
    ne2 = e2[3]
    nn = n[3]
    def __init__(self):
        return self
    