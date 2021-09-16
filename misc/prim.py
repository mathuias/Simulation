import math 
import numpy as np 

from itertools import chain


def prims(m):
    results = list() 
    for i in chain([2], range(3, m//2 + 1, 2)):
        while m % i == 0:
            results.append(i)
            m = m // i 
        if i > m:  
            break
    return results

def singlePrims(primList):
    singlePrims = list()

    for i in range(len(primList)):
        if primList[i] not in singlePrims:
            singlePrims.append(primList[i])
    return singlePrims
        

if __name__ == "__main__":

    m = 686 

    primList = prims(m)

    singlePrims = singlePrims(primList)

    print(singlePrims)

