# -*- coding: utf-8 -*-
"""
Created on Fri May 27 00:48:54 2022

@author: UCC
"""

import math

def deg2grad(deg):
    grad = (deg/18)*20
    return grad
def rad2grad(rad):
    grad = (rad/math.pi)*200
    return grad
def deg2rad(deg):
    rad = (deg/180)*math.pi
    return rad
def grad2deg(grad):
    deg = (grad/20)*18
    return deg
def grad2rad(grad):
    rad = (grad/200)*math.pi
    return rad
def pow2(ver):
    res = math.pow(ver,2)
    return res
def pointcoordinate(y,x,angle,distance):
    ny = y+distance*math.sin(grad2rad(angle))
    print(grad2rad(angle))
    nx = x+distance*math.cos(grad2rad(angle))
    coordinate = []
    coordinate.append(ny)
    coordinate.append(nx)
    return coordinate
def gradangle(dy,dx):
    if dy > 0:
        if dx > 0:
            ngrad = math.atan(grad2rad(dy/dx))
        if dx < 0:
            ngrad = math.atan(grad2rad(dy/dx))+200
    if dy < 0:
        if dx > 0:
            ngrad = math.atan(grad2rad(dy/dx))+400
        if dx < 0:
            ngrad = math.atan(grad2rad(dy/dx))+200
    return ngrad
def nextangle(angle,beta,angletype = None):
        pi = math.pi
        nangle = angle+beta
        if angletype == None:
            angletype = "grad"
        if angletype == "grad":
            if 0 <= nangle<200:
                nangle = nangle+200
            elif 200<=nangle<400:
                nangle = nangle-200
            elif 400<=nangle<600:
                nangle = nangle-200
            elif 600<=nangle<800:
                nangle = nangle-600
        elif angletype == "deg":
            if 0 <= nangle<180:
                nangle = nangle+180
            elif 180<=nangle<360:
                nangle = nangle-180
            elif 360<=nangle<540:
                nangle = nangle-180
            elif 540<=nangle<720:
                nangle = nangle-540
        elif angletype == "rad":
            if  0<= nangle<pi:
                nangle = nangle+pi
            elif pi<=nangle<2*pi:
                nangle = nangle-pi
            elif 2*pi<=nangle<3*pi:
                nangle = nangle-pi
            elif 3*pi<=nangle<4*pi:
                nangle = nangle-3*pi
        return nangle

    