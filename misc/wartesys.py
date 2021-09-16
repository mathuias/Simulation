import math 
import numpy as np 

def showMeanVarStd(listParam):
    if type(listParam) is list:
        meanArr = np.mean(listParam)
        varArr = np.var(listParam)
        stdArr = np.std(listParam)
        print("Mean: {}, Var: {}, Std: {}".format(meanArr, varArr, stdArr))


if __name__ == "__main__":

    #! Für M/M/1 Wartesystem
    arrivals =       [14, 22, 22, 8, 163, 165, 27, 25, 2, 31]
    operations =    [12, 20, 79, 34, 35, 23, 25, 49, 33, 49]

    # Ankunftsrate alpha
    meanArr = np.mean(arrivals)
    print("\n Mean of arrivals array: {}".format(meanArr))
    alpha = 1/meanArr
    print("\n Rate of arrivals: {}".format(alpha))

    # Bedienrate beta
    meanOp = np.mean(operations)
    print("\n Mean of Operations array: {}".format(meanOp))
    beta = 1/meanOp
    print("\n Rate of operations: {}".format(beta))

    # Verkehrsdichte p
    p = alpha/beta 
    print("\n Verkehrsdichte: {}".format(p))

    # stationäre Verteilung
    n = 10 
    pi = [ (p**i)*(1-p) for i in range(n+1) ]
    
    print("\n stationäre Verteilung")
    print("i\tpi(i)")
    for i in range(n+1):
        print(str(i)+"\t"+str(round(pi[i], 4)))

    # mittlere Kundenzahl
    E_N = round( (p / (1-p)), 3)

    print("\n mittlere Kundenzahl")
    print(" E(N): {} Menschen".format(E_N))

    # mittlere Verweildauer
    E_R = round((alpha / (beta*(beta-alpha))), 3)

    print("\n mittlere Verweildauer")
    print(" E(R): {} sekunden".format(E_R))

    #! M/M/1/K      k = 10 , begrenzter Warteraum 
    k = 10
    p = 0.75

    #stationäre Verteilung 
    pi_2 = [ (  (p**i) * ( (1-p) / (1-p**(k+1) ) ) ) for i in range(k+1)]

    print("\n stationäre Verteilung für k = {}".format(k))
    print("i\tpi(i)")
    for i in range(n+1):
        print(str(i)+"\t"+str(round(pi_2[i], 4)))

    # mittlere Kundenzahl
    E_N_2 = round( (    (p / (1-p)) - ( (k+1)*(p**(k+1)) )/( 1-p**(k+1))     ), 3)

    print("\n mittlere Kundenzahl für k = {}".format(k))
    print(" E(N): {} Menschen".format(E_N_2))

    # mittlere Verweildauer (Gesetz von Little)
    q = 0.2
    alpha_2 = alpha*(1-q)
    E_R_2 = E_N_2 / alpha_2  

    print("\n mittlere Verweildauer nach Little: q={}".format(q))
    print("E(R): {} sekunden".format(E_R_2))

    # mittlere Wartezeit