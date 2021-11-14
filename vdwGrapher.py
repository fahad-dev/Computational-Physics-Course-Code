# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:58:13 2021

@author: computer
"""


import matplotlib.pylab as plt
import numpy as np

#function(s)
def vdwEqn(v, t):
    return 8*t/((3*v)-1) - (3/(v**2))

#array(s)
volumeArray = np.arange(0.5, 1.55, 0.01)
isothermOne = np.zeros(volumeArray.size)
isothermTwo = np.zeros(volumeArray.size)
isothermThree = np.zeros(volumeArray.size)

#calculate output
isothermOne = vdwEqn(volumeArray, 0.95)
isothermTwo = vdwEqn(volumeArray, 1.00)
isothermThree = vdwEqn(volumeArray, 1.05)


#plot graphs
plt.plot(volumeArray, isothermOne, '#2cbdfe', label = 't=0.95' )
plt.plot(volumeArray, isothermTwo, '#6e6cd8', label = 't=1.00' )
plt.plot(volumeArray, isothermThree, '#b01bb3', label = 't=1.05')

plt.title('isotherms of the Van Der Waals equation')
plt.xlabel('reduced volume v')
plt.ylabel('reduced pressure p')
plt.legend()

#save plot and display plot
plt.savefig('vdwGraph.png')

plt.show()
