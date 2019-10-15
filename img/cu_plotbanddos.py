# -*- coding: utf-8 -*-
"""
@author: yyyu200@163.com
"""

import numpy as np

feig=open('bd.dat')
ymin=-10
ymax=10
nband=4 # this is the valence band number, for insulators only
dline=50 # vertical line intervals

l=feig.readline()
nbnd=int(l.split(',')[0].split('=')[1])
nks=int(l.split(',')[1].split('=')[1].split('/')[0])

eig=np.zeros((nks,nbnd),dtype=float)
for i in range(nks):
    l=feig.readline()
    count=0
    for j in range((nbnd-1)//10+1):
        l=feig.readline()
        for k in range(len(l.split())):
            eig[i][count]=l.split()[k]
            count=count+1
            
feig.close()

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

F=plt.gcf()
F.set_size_inches([8,4])

p1=plt.subplot(1, 2, 1)

lw=1.2 # line width

plt.xlim([0,nks-1]) # 201 points
plt.ylim([ymin,ymax])
#plt.xlabel(r'$k (\AA^{-1})$',fontsize=16)
plt.ylabel(r' E (eV) ',fontsize=16)

Ef=12.5663
for i in range(nbnd):
    line1=plt.plot( eig[:,i]-Ef,color='r',linewidth=lw ) 

vline=[0,50,100,120,170]
for x in vline:
    plt.axvline(x, ymin=ymin, ymax=ymax,linewidth=lw,color='black')

plt.xticks( (0,50,100,120,170), ('L', r'${\Gamma}$', 'X', 'U|K', r'${\Gamma}$') )

p2=plt.subplot(1, 2, 2)
plt.xlim([0,6])
plt.ylim([ymin,ymax])
plt.xlabel(r'DOS(States/atom/eV)',fontsize=16)
d=np.loadtxt('cu.dos',comments='#')
plt.plot(d[:,1],d[:,0]-Ef,color='r',linewidth=lw)

plt.tight_layout()
plt.savefig('pwbanddos.png',dpi=500)

