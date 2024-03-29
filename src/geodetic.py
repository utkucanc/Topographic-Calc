# -*- coding: utf-8 -*-
"""
Created on Fri May 27 02:10:52 2022

@author: UCC
"""
import math
from core import *
a=[6377397.155,6378388.000,6378137.000]
b=[6356078.963,6356911.946,6356752.314]
c=[6398786.849,6399936.608,6399593.626]
f1=[299.1528,297,298.257222101]
e=[0.00667437,0.00672267,0.0066943800]
e2=[0.00671922,0.00676817,0.0067394968]
n=[0.00167418,0.00168634,0.0016792204]
alfa = [366742.519778,6367654.500058,6367449.14571]
beta = [15988.639219,16107.034679,16038.508742]
fi = [16.729955,16.976211,16.832613]
gama = [0.021785,0.022266,0.021984]
el = [0.000031,0.000032,0.000031]
beta1 = [0.002511273350,0.002529506915,0.002518826597]
fi1 = [0.000003678786,0.000003732401,0.000003700949]
gama1 = [0.000000007381,0.000000007543,0.000000007448]
el1 = [0.000000000017,0.000000000017,0.000000000017]
class Bassel:
    def __init__(self):
        """
        Author : Utku Can CANATAN
        """
        return self
    def printdata():
        """
        ALL GEODESIC DATA PRINT

        Returns
        -------
        None

        """
        na = a[0]
        nb = b[0]
        nc = c[0]
        nf1 = f1[0]
        ne = e[0]
        ne2 = e2[0]
        nn = n[0]
        nalfa = alfa[0]
        nbeta = beta[0]
        nfi = fi[0]
        ngama = gama[0]
        nel = el[0]
        nbeta1 = beta1[0]
        nfi1 = fi1[0]
        ngama1 = gama1[0]
        nel1 = el1[0]
        print("a = "+str(na))
        print("b = "+str(nb))
        print("c = "+str(nc))
        print("1/f = "+str(nf1))
        print("e = "+str(ne))
        print("e'^2 = "+str(ne2))
        print("n = "+str(nn))
        print("α = "+str(nalfa))
        print("β = "+str(nbeta))
        print("γ = "+str(nfi))
        print("δ = "+str(ngama))
        print("ε = "+str(nel))
        print("β`- = "+str(nbeta1))
        print("γ`- = "+str(nfi1))
        print("δ`- = "+str(ngama1))
        print("ε`- = "+str(nel1))
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
        ne2 = e2[0]
        nc = c[0]
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
        ne2 = e2[0]
        x = (Bassel.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.cos(core.deg2rad(lamda))
        y = (Bassel.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.sin(core.deg2rad(lamda))
        z = ((Bassel.Ncalc(phi)/(1+ne2))+h)*math.sin(core.deg2rad(phi))
        GOC = []
        GOC.append(x)
        GOC.append(y)
        GOC.append(z)
        
        return GOC
    def MeridianLeg(phi):
        """
        

        Parameters
        ----------
        phi : TYPE DEGREE
            DESCRIPTION.

        Returns
        -------
        G : TYPE METER
            MERIDIAN ARC LENGTH

        """
        nalfa = alfa[0]
        nbeta = beta[0]
        nfi = fi[0]
        ngama = gama[0]
        nel = el[0]
        G =nalfa-(nbeta*math.sin(2*core.deg2rad(phi)))+(nfi*math.sin(4*core.deg2rad(phi)))-(ngama*math.sin(6*core.deg2rad(phi)))+(nel*math.sin(8*core.deg2rad(phi)))
        return G
    def Curvature(A):
        """
        

        Parameters
        ----------
        A : TYPE
            DESCRIPTION.

        Returns
        -------
        k : TYPE
            DESCRIPTION.

        """
        ne2 = e2[0]
        n = ne2*core.pow2(math.cos(core.deg2rad(A)))
        cs = core.pow2(math.cos(core.deg2rad(A)))
        p = 1+(n*cs)
        k = p/Bassel.Ncalc(A)
        return k
    def LGS(phi1,phi2,lamda1,lamda2,h1,h2):
        """
        

        Parameters
        ----------
        phi1 : TYPE
            DESCRIPTION.
        phi2 : TYPE
            DESCRIPTION.
        lamda1 : TYPE
            DESCRIPTION.
        lamda2 : TYPE
            DESCRIPTION.
        h1 : TYPE
            DESCRIPTION.
        h2 : TYPE
            DESCRIPTION.

        Returns
        -------
        coordinate: TYPE list
            DESCRIPTION.

        """
        coordinate = []
        ne2 = e2[0]
        def sin(x):
            rs = math.sin(core.deg2rad(x))
            return rs
        def cos(x):
            rs = math.cos(core.deg2rad(x))
            return rs
        def N(x):
            rs = Bassel.Ncalc(x)
            return rs
        x = (-1)*sin(phi1)*(N(phi2)*cos(phi2)*cos(lamda2-lamda1)-N(phi1)*cos(phi1))+(cos(phi1)/(1+ne2))*(N(phi2)*sin(phi2)-N(phi1)*sin(phi1))
        y = N(phi2)*cos(phi2)*sin(lamda2-lamda1)
        z = cos(phi1)(N(phi2)*cos(phi2)*cos(lamda2-lamda1)-N(phi1)*cos(phi1))+((sin(phi1)/(1+ne2))*N(phi2*sin(phi2)-N(phi1)*sin(phi1)))
        x1 = x*(1+(h2/N(phi2)))+ne2*cos(phi1)*(h2/N(phi2)*(x*cos(phi1)+z*sin(phi1)))
        y1 = y*(1+(h2/N(phi2)))
        z1 = z*(1+(h2/N(phi2)))+N(phi1)*((h2/N(phi2))-(h1/N(phi1)))+ne2*sin(phi1)*(h2/N(phi2))*(x*cos(phi1)+z*sin(phi1))
        coordinate.append(x1)
        coordinate.append(y1)
        coordinate.append(z1)
        return coordinate
    
    
class Hayford:
    def __init__(self):
        """
        Author : Utku Can CANATAN
        """
        return self
    def printdata():
        """
        ALL GEODESIC DATA PRINT

        Returns
        -------
        None.

        """
        na = a[1]
        nb = b[1]
        nc = c[1]
        nf1 = f1[1]
        ne = e[1]
        ne2 = e2[1]
        nn = n[1]
        nalfa = alfa[1]
        nbeta = beta[1]
        nfi = fi[1]
        ngama = gama[1]
        nel = el[1]
        nbeta1 = beta1[1]
        nfi1 = fi1[1]
        ngama1 = gama1[1]
        nel1 = el1[1]
        print("a = "+str(na))
        print("b = "+str(nb))
        print("c = "+str(nc))
        print("1/f = "+str(nf1))
        print("e = "+str(ne))
        print("e'^2 = "+str(ne2))
        print("n = "+str(nn))
        print("α = "+str(nalfa))
        print("β = "+str(nbeta))
        print("γ = "+str(nfi))
        print("δ = "+str(ngama))
        print("ε = "+str(nel))
        print("β`- = "+str(nbeta1))
        print("γ`- = "+str(nfi1))
        print("δ`- = "+str(ngama1))
        print("ε`- = "+str(nel1))
    def Ncalc(phi):
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
            Hayford
            [1] x
            [2] y
            [3] z
            """
        ne2 = e2[1]
        x = (Hayford.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.cos(core.deg2rad(lamda))
        y = (Hayford.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.sin(core.deg2rad(lamda))
        z = ((Hayford.Ncalc(phi)/(1+ne2))+h)*math.sin(core.deg2rad(phi))
        GOC = []
        GOC.append(x)
        GOC.append(y)
        GOC.append(z)
        return GOC
    def MeridianLeg(phi):
        """
        

        Parameters
        ----------
        phi : TYPE DEGREE
            DESCRIPTION.

        Returns
        -------
        G : TYPE METER
            MERIDIAN ARC LENGTH

        """
        nalfa = alfa[1]
        nbeta = beta[1]
        nfi = fi[1]
        ngama = gama[1]
        nel = el[1]
        G =nalfa-(nbeta*math.sin(2*core.deg2rad(phi)))+(nfi*math.sin(4*core.deg2rad(phi)))-(ngama*math.sin(6*core.deg2rad(phi)))+(nel*math.sin(8*core.deg2rad(phi)))
        return G
    def Curvature(A):
        """
        

        Parameters
        ----------
        A : TYPE
            DESCRIPTION.

        Returns
        -------
        k : TYPE
            DESCRIPTION.

        """
        ne2 = e2[1]
        n = ne2*core.pow2(math.cos(core.deg2rad(A)))
        cs = core.pow2(math.cos(core.deg2rad(A)))
        p = 1+(n*cs)
        k = p/Bassel.Ncalc(A)
        return k
    def LGS(phi1,phi2,lamda1,lamda2,h1,h2):
        """
        

        Parameters
        ----------
        phi1 : TYPE
            DESCRIPTION.
        phi2 : TYPE
            DESCRIPTION.
        lamda1 : TYPE
            DESCRIPTION.
        lamda2 : TYPE
            DESCRIPTION.
        h1 : TYPE
            DESCRIPTION.
        h2 : TYPE
            DESCRIPTION.

        Returns
        -------
        coordinate: TYPE list
            DESCRIPTION.

        """
        coordinate = []
        ne2 = e2[1]
        def sin(x):
            rs = math.sin(core.deg2rad(x))
            return rs
        def cos(x):
            rs = math.cos(core.deg2rad(x))
            return rs
        def N(x):
            rs = Bassel.Ncalc(x)
            return rs
        x = (-1)*sin(phi1)*(N(phi2)*cos(phi2)*cos(lamda2-lamda1)-N(phi1)*cos(phi1))+(cos(phi1)/(1+ne2))*(N(phi2)*sin(phi2)-N(phi1)*sin(phi1))
        y = N(phi2)*cos(phi2)*sin(lamda2-lamda1)
        z = cos(phi1)(N(phi2)*cos(phi2)*cos(lamda2-lamda1)-N(phi1)*cos(phi1))+((sin(phi1)/(1+ne2))*N(phi2*sin(phi2)-N(phi1)*sin(phi1)))
        x1 = x*(1+(h2/N(phi2)))+ne2*cos(phi1)*(h2/N(phi2)*(x*cos(phi1)+z*sin(phi1)))
        y1 = y*(1+(h2/N(phi2)))
        z1 = z*(1+(h2/N(phi2)))+N(phi1)*((h2/N(phi2))-(h1/N(phi1)))+ne2*sin(phi1)*(h2/N(phi2))*(x*cos(phi1)+z*sin(phi1))
        coordinate.append(x1)
        coordinate.append(y1)
        coordinate.append(z1)
        return coordinate
    
class RS80:
    def __init__(self):
        """
        Author : Utku Can CANATAN
        """
        return self
    def printdata():
        """
        ALL GEODESIC DATA PRINT

        Returns
        -------
        None.

        """
        na = a[2]
        nb = b[2]
        nc = c[2]
        nf1 = f1[2]
        ne = e[2]
        ne2 = e2[2]
        nn = n[2]
        nalfa = alfa[2]
        nbeta = beta[2]
        nfi = fi[2]
        ngama = gama[2]
        nel = el[2]
        nbeta1 = beta1[2]
        nfi1 = fi1[2]
        ngama1 = gama1[2]
        nel1 = el1[2]
        print("a = "+str(na))
        print("b = "+str(nb))
        print("c = "+str(nc))
        print("1/f = "+str(nf1))
        print("e = "+str(ne))
        print("e'^2 = "+str(ne2))
        print("n = "+str(nn))
        print("α = "+str(nalfa))
        print("β = "+str(nbeta))
        print("γ = "+str(nfi))
        print("δ = "+str(ngama))
        print("ε = "+str(nel))
        print("β`- = "+str(nbeta1))
        print("γ`- = "+str(nfi1))
        print("δ`- = "+str(ngama1))
        print("ε`- = "+str(nel1))
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
            RS80
        [1]: x
        [2]: y
        [3]: z
            """
        ne2 = e2[2]
        x = (RS80.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.cos(core.deg2rad(lamda))
        y = (RS80.Ncalc(phi)+h)*math.cos(core.deg2rad(phi))*math.sin(core.deg2rad(lamda))
        z = ((RS80.Ncalc(phi)/(1+ne2))+h)*math.sin(core.deg2rad(phi))
        GOC = []
        GOC.append(x)
        GOC.append(y)
        GOC.append(z)
        return GOC
    def MeridianLeg(phi):
        """
        

        Parameters
        ----------
        phi : TYPE DEGREE
            DESCRIPTION.

        Returns
        -------
        G : TYPE METER
            MERIDIAN ARC LENGTH

        """
        nalfa = alfa[2]
        nbeta = beta[2]
        nfi = fi[2]
        ngama = gama[2]
        nel = el[2]
        G =nalfa-(nbeta*math.sin(2*core.deg2rad(phi)))+(nfi*math.sin(4*core.deg2rad(phi)))-(ngama*math.sin(6*core.deg2rad(phi)))+(nel*math.sin(8*core.deg2rad(phi)))
        return G
    def Curvature(A):
        """
        

        Parameters
        ----------
        A : TYPE
            DESCRIPTION.

        Returns
        -------
        k : TYPE
            DESCRIPTION.

        """
        ne2 = e2[2]
        n = ne2*core.pow2(math.cos(core.deg2rad(A)))
        cs = core.pow2(math.cos(core.deg2rad(A)))
        p = 1+(n*cs)
        k = p/Bassel.Ncalc(A)
        return k
    def LGS(phi1,phi2,lamda1,lamda2,h1,h2):
        """
        

        Parameters
        ----------
        phi1 : TYPE
            DESCRIPTION.
        phi2 : TYPE
            DESCRIPTION.
        lamda1 : TYPE
            DESCRIPTION.
        lamda2 : TYPE
            DESCRIPTION.
        h1 : TYPE
            DESCRIPTION.
        h2 : TYPE
            DESCRIPTION.

        Returns
        -------
        coordinate: TYPE list
            DESCRIPTION.

        """
        coordinate = []
        ne2 = e2[2]
        def sin(x):
            rs = math.sin(core.deg2rad(x))
            return rs
        def cos(x):
            rs = math.cos(core.deg2rad(x))
            return rs
        def N(x):
            rs = Bassel.Ncalc(x)
            return rs
        x = (-1)*sin(phi1)*(N(phi2)*cos(phi2)*cos(lamda2-lamda1)-N(phi1)*cos(phi1))+(cos(phi1)/(1+ne2))*(N(phi2)*sin(phi2)-N(phi1)*sin(phi1))
        y = N(phi2)*cos(phi2)*sin(lamda2-lamda1)
        z = cos(phi1)(N(phi2)*cos(phi2)*cos(lamda2-lamda1)-N(phi1)*cos(phi1))+((sin(phi1)/(1+ne2))*N(phi2*sin(phi2)-N(phi1)*sin(phi1)))
        x1 = x*(1+(h2/N(phi2)))+ne2*cos(phi1)*(h2/N(phi2)*(x*cos(phi1)+z*sin(phi1)))
        y1 = y*(1+(h2/N(phi2)))
        z1 = z*(1+(h2/N(phi2)))+N(phi1)*((h2/N(phi2))-(h1/N(phi1)))+ne2*sin(phi1)*(h2/N(phi2))*(x*cos(phi1)+z*sin(phi1))
        coordinate.append(x1)
        coordinate.append(y1)
        coordinate.append(z1)
        return coordinate
Hayford.printdata()