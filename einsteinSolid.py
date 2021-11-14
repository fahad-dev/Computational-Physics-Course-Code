# -*- coding: utf-8 -*-
# This code generates isotherms for the Van Der Waals gas equation at some specified temperatures.
"""
Created on Thu Oct 28 12:35:16 2021

@author: computer
"""

#import 
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from matplotlib import animation as am
from scipy.optimize import curve_fit

#functions
def energyFlow(eSolid,numExch):
    maxN = eSolid.size-1
    for i in range(numExch):
        gain = rnd.randint(0,maxN) 
        lose = rnd.randint(0,maxN) 
        while eSolid[lose] == 0:
            lose = rnd.randint(0,maxN)
        eSolid[gain] += 1
        eSolid[lose] -= 1

    return eSolid

def evolve(*args):
    energyFlow(solid,1000)
    imgPlot.set_data( np.reshape(solid, (L,L) ) )
    return [imgPlot]                      # return line object in a list


#set up solids
    
# Solid 1:
L1= 50
N1 = L1*L1
qavg1 = 15
solid1 = qavg1*np.ones(N1)

# Solid 2
N2 = 50*25 
qavg2 = 30
solid2 = qavg2*np.ones(N2)

# Combined System
solidsCombined = np.append(solid1,solid2)

#animations and plots

animate = False

if animate:
    fig = plt.figure(figsize=(10,10))
    
    img = np.reshape(solid, (L,L))
    
    imgPlot = plt.imshow(img, interpolation='none', vmin=0, vmax=50, cmap='coolwarm')
    plt.colorbar(imgPlot)
    
    anim = am.FuncAnimation(fig, evolve, \
    						interval=10, frames=500, repeat=False, blit=True)
        
else:
    solid1 = energyFlow(solid1, 2000*solid1.size)
    solid2 = energyFlow(solid2, 2000*solid2.size)
    solidsCombined = energyFlow(solidsCombined, 1000*solidsCombined.size)
    
    energy1, counts1 = np.unique(solid1, return_counts=True)
    energy2, counts2 = np.unique(solid2, return_counts=True)
    energyCombined, countsCombined = np.unique(solidsCombined, return_counts=True)
    
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    fig.suptitle("Energy Distribution of Atoms in an Einstein Solid")
    
    ax1.set_title("Energy Distribution of Solid 1 and Solid 2")
    ax2.set_title("Energy Distribution of Solids 1 and 2 Combined")
    
    
    ax1.set_xlabel("Energy Levels")
    ax1.set_ylabel("Number of Atoms")
    
    ax2.set_xlabel("Energy Levels")
    ax2.set_ylabel("Number of Atoms")
    
    ax1.plot(energy1,counts1,'bx', label="Solid 1")
    ax1.plot(energy2,counts2,'ro', label="Solid 2")
    
    ax2.plot(energyCombined, countsCombined, 'm*', label="Solids Combined")
    #ax2.semilogy(energy,counts,'ro')
    
    ax1.legend()
    ax2.legend()
    
    
    plt.savefig('twoSolids.png', dpi=1000)
