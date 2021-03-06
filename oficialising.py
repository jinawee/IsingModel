#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#from __future__ import division
import numpy as np
from pylab import imshow, figure, grid, show
#----------------------------------------------------------------------#
#   Check periodic boundary conditions 
#----------------------------------------------------------------------#
def bc(i):
    if i+1 > SIZE-1:
        return 0
    if i-1 < 0:
        return SIZE-1
    else:
        return i

#----------------------------------------------------------------------#
#   Calculate internal energy
#----------------------------------------------------------------------#
def energy(system, N, M):
    return -1 * system[N,M] * (system[bc(N-1), M] \
                               + system[bc(N+1), M] \
                               + system[N, bc(M-1)] \
                               + system[N, bc(M+1)])

#----------------------------------------------------------------------#
#   Build the system
#----------------------------------------------------------------------#
def build_system():
    system = np.random.random_integers(0,1,(SIZE,SIZE))
    system[system==0] =- 1
    return system

#----------------------------------------------------------------------#
#   The Main monte carlo loop
#----------------------------------------------------------------------#
def main(T):
    system = build_system()

    for step, x in enumerate(range(STEPS)):
        M = np.random.randint(0,SIZE)
        N = np.random.randint(0,SIZE)

        E = -2. * energy(system, N, M)

        if E <= 0.:
            system[N,M] *= -1
        elif np.exp(-1./T*E) > np.random.rand():
            system[N,M] *= -1
    return system

#----------------------------------------------------------------------#
#   Run the menu for the monte carlo simulation
#----------------------------------------------------------------------#
#def run():
#    print '='*70
#    print '\tMonte Carlo Statistics for an ising model with'
#    print '\t\tperiodic boundary conditions'
#    print '='*70
#
#    print "Choose the temperature for your run (0.1-100)"
#    T = float(raw_input())
#    return main(T)

SIZE=150
STEPS=int(1e7)
final=main(0.1)

#figure(1)
#imshow(final, interpolation='nearest')
#grid(True)
#show()
