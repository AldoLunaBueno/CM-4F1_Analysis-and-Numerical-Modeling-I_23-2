#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:48:10 2019

@author: miller
"""

import numpy as np
#import scipy.linalg as sl
#Para resolver sistema triangular superior

def sumS(k,nrow,A,x):
    n=nrow-1
    sums=0
    if k==0:
        return sums
    else:
        for r in range(n-k+1,nrow):
            sums=sums+A[n-k][r]*x[r][0]
        return sums

def SupSolve(A,b):
    nrow=np.shape(A)[0]
    n=nrow-1
    x=np.zeros(nrow).reshape(nrow, 1)
    for k in range(nrow):
        x[n-k][0]=(b[n-k][0]-sumS(k,nrow,A,x))/A[n-k][n-k]
    return x    
    
def elimGauss(A,b):
    nrow=np.shape(A)[0]
    k=0
    print(np.insert(A, A.shape[1],b.transpose(), 1),"\n")
    while A[k,k]!=0 and k<nrow-1:
        for j in range(k+1,nrow): 
            m=(A[j,k]/A[k,k])
            A[j,:]=A[j,:]-A[k,:]*m
            b[j]=b[j]-b[k]*m    
        k=k+1
        bt=b.transpose()
        print(np.insert(A, A.shape[1],bt, 1),"\n")
    if A[k,k]==0 :
        print("Necesita Pivoteo")
    else:
        return SupSolve(A,b)

#A=np.array([2,1,1,0,0,0,2,2,0,1,1,1,0,0,0,2]).reshape(4,4)
#b=np.array([1,8,6,6]).reshape(4,1)
A=np.array([1,1,0,-1,0,1,0,0,0,-1, 4,4,1,-2,-4,0,1,0,0,-2,0,0,2,0,0]).reshape(5,5)        
b=np.array([0,2,8,0,4]).reshape(5,1)
#A=np.array([2,1,1,0,4,3,3,1,8,7,9,5,6,7,9,8]).reshape(4,4)
#b=np.array([1,8,30,41]).reshape(4,1)
#bt=b.transpose()
#print(sl.det(A),"\n")

elimGauss(A,b)