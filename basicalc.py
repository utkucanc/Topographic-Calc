# -*- coding: utf-8 -*-
"""
Created on Fri May 27 00:54:01 2022

@author: PC
"""

import core
import math

angtype = ["grad","rad","deg"]
class basicalc:
    def distance (x1,x2,y1,y2):
        dist = math.sqrt(core.pow2(x1-x2)+core.pow2(y1-y2))
        return dist
    def pointcoordinate(y,x,angle,distance):
        coordinate = core.pointcoordinate(y,x,angle,distance)
        return coordinate
    def gradangle(x1,x2,y1,y2):
        dy = y2-y1
        dx = x2-x1
        if dy > 0:
            if dx > 0:
                ngrad = math.atan(core.grad2rad(dy/dx))
            if dx < 0:
                ngrad = math.atan(core.grad2rad(dy/dx))+200
        if dy < 0:
            if dx > 0:
                ngrad = math.atan(core.grad2rad(dy/dx))+400
            if dx < 0:
                ngrad = math.atan(core.grad2rad(dy/dx))+200
        return ngrad
    def degangle(x1,x2,y1,y2):
        dy = y2-y1
        dx = x2-x1
        if dy > 0:
            if dx > 0:
                ngrad = math.atan(core.deg2rad(dy/dx))
            if dx < 0:
                ngrad = math.atan(core.deg2rad(dy/dx))+180
        if dy < 0:
            if dx > 0:
                ngrad = math.atan(core.deg2rad(dy/dx))+360
            if dx < 0:
                ngrad = math.atan(core.deg2rad(dy/dx))+180
        return ngrad
    def radangle(x1,x2,y1,y2):
        dy = y2-y1
        dx = x2-x1
        if dy > 0:
            if dx > 0:
                ngrad = math.atan(dy/dx)
            if dx < 0:
                ngrad = math.atan(dy/dx)+math.pi
        if dy < 0:
            if dx > 0:
                ngrad = math.atan(dy/dx)+(math.pi*2)
            if dx < 0:
                ngrad = math.atan(dy/dx)+math.pi
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
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
