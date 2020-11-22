#!/usr/bin/python3
import numpy as np
import time
def sigmaFunction(r,n: float):
    rSum = np.float128(0)
    n = np.float128(n)
    r = np.float128(r)
    for i in range(1,int(r+1)):
        i = np.float128(i)
        rSum = np.add(rSum,np.divide(np.power((n-1),i),(np.multiply(i,(np.power(n,i))))))
    return(rSum)

def howCloseisIt(appro,n:float):
    n = np.float128(n)
    appro = np.float128(appro)
    actVal = np.log(n)
    return(actVal - appro)
while True:
    n = float(input("Enter x value for ln(x)"))
    r = int(input("Enter n value for Sigma"))
    out = sigmaFunction(r, n)
    print("Approximated Value: " + str(out))
    time.sleep(2)
    print("off by: " + str(howCloseisIt(out, n)))
