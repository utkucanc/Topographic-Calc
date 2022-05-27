# -*- coding: utf-8 -*-
"""
Created on Fri May 27 02:10:52 2022

@author: UCC
"""
import math
import core
a=[6377397.155,6378388.000,6378137.000]
b=[6356078.963,6356911.946,6356752.314]
c=[6398786.849,6399936.608,6399593.626]
f1=[299.1528,297,298.257222101]
e=[0.00667437,0.00672267,0.0066943800]
e2=[0.00671922,0.00676817,0.0067394968]
n=[0.00167418,0.00168634,0.0016792204]

class Bassel:
    def printdata():
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
    def Ncalc(phi):
        """
        

        Parameters
        ----------
        phi : degree
            DESCRIPTION.

        Returns
        -------
        N : TYPE = M
            DESCRIPTION.

        """
        ne2 = e2[1]
        nc = c[1]
        v = math.sqrt(1+ne2*math.cos(core.deg2rad(phi)))
        N = nc/v
        return N
    def Gc2GOC(phi,lamda,h):
        """
        

        Parameters
        ----------
        phi : Degree
            DESCRIPTION.
        lamda : Degree
            DESCRIPTION.
        h : Meter
            DESCRIPTION.

        Returns
        -------
        GOC : TYPE List
            Bassel
            [1] x
            [2] y
            [3] z

        """
        ne2 = e2[1]
        x = (Bassel.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.cos(core.deg2rad(lamda))
        y = (Bassel.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.sin(core.deg2rad(lamda))
        z = ((Bassel.Ncalc(phi)/(1+ne2))+h)*math.sin(core.deg2rad(phi))
        GOC = []
        GOC.append(x)
        GOC.append(y)
        GOC.append(z)
        
        return GOC
    def __init__(self):
        return self
    
class Hayford:
    def printdata():
        na = a[2]
        nb = b[2]
        nc = c[2]
        nf1 = f1[2]
        ne = e[2]
        ne2 = e2[2]
        nn = n[2]
        print("a"+str(na))
        print("b"+str(nb))
        print("c"+str(nc))
        print("1/f"+str(nf1))
        print("e"+str(ne))
        print("e'^2"+str(ne2))
        print("n"+str(nn))
    def Ncalc(phi):
        ne2 = e2[2]
        nc = c[2]
        v = math.sqrt(1+ne2*math.cos(core.deg2rad(phi)))
        N = nc/v
        return N
    def Gc2GOC(phi,lamda,h):
        """
        

        Parameters
        ----------
        phi : Degree
            DESCRIPTION.
        lamda : Degree
            DESCRIPTION.
        h : Meter
            DESCRIPTION.

        Returns
        -------
        GOC : TYPE List
            Hayford
            [1] x
            [2] y
            [3] z
            """
        ne2 = e2[2]
        x = (Hayford.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.cos(core.deg2rad(lamda))
        y = (Hayford.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.sin(core.deg2rad(lamda))
        z = ((Hayford.Ncalc(phi)/(1+ne2))+h)*math.sin(core.deg2rad(phi))
        GOC = []
        GOC.append(x)
        GOC.append(y)
        GOC.append(z)
        return GOC
    def __init__(self):
        return self
    
class RS80:
    def printdata():
        na = a[3]
        nb = b[3]
        nc = c[3]
        nf1 = f1[3]
        ne = e[3]
        ne2 = e2[3]
        nn = n[3]
        print("a"+str(na))
        print("b"+str(nb))
        print("c"+str(nc))
        print("1/f"+str(nf1))
        print("e"+str(ne))
        print("e'^2"+str(ne2))
        print("n"+str(nn))
    def Ncalc(phi):
        ne2 = e2[3]
        nc = c[3]
        v = math.sqrt(1+ne2*math.cos(core.deg2rad(phi)))
        N = nc/v
        return N
    def Gc2GOC(phi,lamda,h):
        """
        

        Parameters
        ----------
        phi : Degree
            DESCRIPTION.
        lamda : Degree
            DESCRIPTION.
        h : Meter
            DESCRIPTION.

        Returns
        -------
        GOC : TYPE List
            RS80
        [1]: x
        [2]: y
        [3]: z
            """
        ne2 = e2[3]
        x = (RS80.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.cos(core.deg2rad(lamda))
        y = (RS80.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.sin(core.deg2rad(lamda))
        z = ((RS80.Ncalc(phi)/(1+ne2))+h)*math.sin(core.deg2rad(phi))
        GOC = []
        GOC.append(x)
        GOC.append(y)
        GOC.append(z)
        return GOC
    def __init__(self):
        return self
    
