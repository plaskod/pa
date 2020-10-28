#!/usr/bin/env python3

import numpy as np

A=2
beta=0.035
Qd=0.05
Tp=0.01
tsim=12*3600
h0=0
N=int(tsim/Tp)

h=[]
h.append(h0)

for i in range(1,N):
    tmp =(1/A)*(-beta*np.sqrt(h[i-1])+Qd)*Tp+h[i-1]
    h.append(tmp)
