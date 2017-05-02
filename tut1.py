# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:14:14 2017

@author: 214576460
"""

import numpy as np
from matplotlib import pyplot as plt

def points(n):
    x=np.arange(0 , np.pi/2, n)
    return x

def simpson_integral(n):
    dx=np.pi/2/(n-1)
    xx=np.cos(points(n))
    xx_even=xx[2:-1:2]
    xx_odd=xx[1::2]
    
    tot=(np.sum(xx_even)/3+np.sum(xx_odd)*2/3+xx[0]/6+xx[-1]/6)*dx
    return tot

if __name__=='__main__':
    
    print 'answer to question 3: simple intergration'
    c=[11, 31, 101, 301, 1001]
    for n in c:
        dx=np.pi/2/n
        x=np.arange(0 , np.pi/2, dx)
        y=np.cos(x)
        tot1=y.sum()*dx
        tot1err=np.abs(tot1-1)
        
        print tot1, tot1err
    
    print 'Answer to question 5: Simpson intergration'    
    
    print 'Value of 11 points with simpson intergration'
    value11=simpson_integral(11)
    print value11    
    

    for n in c:
        simp_inter=simpson_integral(n)
        simp_inter_err=np.abs(simp_inter-1)
        
        print  simp_inter, simp_inter_err
    
    c=[11, 31, 101, 301, 10001]
    c=np.array(c)
    tot1err=np.zeros(c.size)
    simp_inter_err=(c.size)
    for i in range(c.size):
        n=c[i]
        tot1err=np.abs(tot1-1)
        simp_inter_err=np.abs(simp_inter-1)
     
    plt.plot(c, tot1err)
    plt.plot(c, simp_inter_err)
    ax=plt.gca()
    
    ax.set_xaxis('log')
    ax.set_yaxis('log')
    plt.show()
    
    
