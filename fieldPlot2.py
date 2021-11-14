# Computational Exercise 1 for PHYS*2330 - Fall 2021
# fieldPlot.py - scaffold code
#
# HEY!  Notice there is a fair bit of un-commented code here?
#       It's worth looking at some of these functions/operations and seeing
#       if you can make sense of them, or look up the documentation online!
# MVM
#------------------------------------------------------------------------------


""" Section 1:  Start by importing relevant libraries
#---------------------------------------------------------------------------"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""
# Return the electric potential, V, due to a charge "q" located at position 
# r0 = (x0,y0).  Evaluate V at the given position (x,y)
def potential(Q, r0, x, y):
    k = 8.99e9
    
    denom = np.sqrt( (x - r0[0])**2 + (y - r0[1])**2 )
    numer = k*Q
    
    return numer/denom

def eFieldx(q0, r0, x, y):
    k = 8.99e9
    
    TotalDistance = ((x-r0[0])**2 + (y-r0[1])**2)
    TotalEField = k*q0 / TotalDistance
    XComponent = (x-r0[0]) / np.sqrt(TotalDistance)
    YComponent = (y-r0[1]) / np.sqrt(TotalDistance)
    
    Ex = TotalEField*XComponent
    #Ey = TotalEField*YComponent
    return Ex

def eFieldy(q0, r0, x, y):
    k = 8.99e9
    
    TotalDistance = ((x-r0[0])**2 + (y-r0[1])**2)
    TotalEField = k*q0 / TotalDistance
    XComponent = (x-r0[0]) / np.sqrt(TotalDistance)
    YComponent = (y-r0[1]) / np.sqrt(TotalDistance)
    
    #Ex = TotalEField*XComponent
    Ey = TotalEField*YComponent
    return Ey


""" Section 3a:  Main body of code - using np.meshgrid for 2D plots
#---------------------------------------------------------------------------"""
# Create a 2D grid of x, y points using numpy's meshgrid function
nx, ny = 60,60
x = np.linspace(-5, 5, nx)
y = np.linspace(-5, 5, ny)
X, Y = np.meshgrid(x, y)

# create a data set for a scalar field to plot using a contour plot
# PLAY AROUND WITH THIS - CHANGE S(X,Y) TO SEE IF THE CONTOUR PLOT DOES WHAT
# YOU EXPECT IT TO DO!
S = np.zeros(X.shape)
S = 1/(1 + (X)**2 + (Y)**2)

# Let's plot the vector field that was given in Question 1 on the pre-quiz
# create a vector field in 2D - we need separate arrays for x- and y-components
E1x = X
E1y = Y

""" Section 3b:  Main body of code - compute fields from point charges
#---------------------------------------------------------------------------"""
# Define the charges (charge & position) that make up the electric dipole
q1 = +1.0; x1 =  1.0; y1 = 0.0
q2 = -1.0; x2 = -1.0; y2 = 0.0
q3 = +2.0; x3 = -1.0; y3 = 2.0

# For each gridpoint in X, Y, we will need to calculate the electric potential
# using our function potential().  The total potential is the sum of contributions
# from each charge.

# We are using '+=' to add to the existing values within the V array
V = potential(q1, [x1,y1], X, Y)
V += potential(q2, [x2,y2], X, Y)
V += potential(q3, [x3,y3], X, Y)

ETotalx = eFieldx(q1, [x1,y1], X, Y)
ETotalx += eFieldx(q2, [x2,y2], X, Y)
ETotalx += eFieldx(q3, [x3,y3], X, Y)

ETotaly = eFieldy(q1, [x1,y1], X, Y)
ETotaly += eFieldy(q2, [x2,y2], X, Y)
ETotaly += eFieldy(q3, [x3,y3], X, Y)

""" Section 4:  Plot your results using various 2D plotting functions
#---------------------------------------------------------------------------"""
# The following line creates 'handles' fig and ax, which allow us to direct 
# formatting commands to the figure and the axes within the figure, respectively.
# [This is useful when creating multiple plots, but also works for a single plot]

# create a single figure with multiple axes using 'subplots'
fig = plt.figure( figsize = (50,70) )
ax1 = fig.add_subplot(221)

# I have added more subplots here, showing all the plots that we put together
# just keep in mind what we discussed about the meshgrid size and how that
# affects the different plot types!  I've set it to 20 in this script just to
# find a balance between the two cases (it's not great though)

ax1.set_title("EField Plot for System of Three Charges", fontsize=20)
#ax2.set_title("Y meshgrid", fontsize=20)

# contour plot of S(XY)
im1 = ax1.streamplot(X,Y,ETotalx,ETotaly)

# contour plot of the electric potential from 3 point charges
im2 = ax1.contour(X,Y,V,50, colors='black')


# Display your plot on screen
plt.show()

# Save your plot
plt.savefig('chargeFieldPlot.png', dpi=1000)
