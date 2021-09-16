from scipy.stats import geom

import matplotlib.pyplot as plt 
import seaborn as sns

import math
import numpy as np 

def showGeomTable(n, p):
    k_values = list(range(n+1))
    dist = [geom.pmf(k, p) for k in k_values]
    
    print("\nk\tp(k)")
    print("___________________")
    for i in range(n+1):
        if dist[i] > 0.0001:
            print(str(k_values[i])+"\t"+str(dist[i]))

def showGeomPMF(n, k, p, lower=True):
    k_values = list(range(n+1))
    dist = [ geom.pmf(k, p) for k in k_values if geom.pmf(k, p) > 0.0001]
    
    result = list()
    print("\nk\tp(k) :")
    print("___________________")

    if lower is True:
        for i in range(k+1):
            if dist[i] > 0.0001:
                print(str(i)+"\t"+str(dist[i]))
                result.append(dist[i])
        print("For P(X ≤ {}) with p={}: {}\n".format(k, round(p, 4), sum(result)))

    elif lower is False:
        for j in range(k, len(dist)):
            if dist[j] > 0.0001:
                print(str(j)+"\t"+str(dist[j]))
                result.append(dist[j])
        print("For P(X ≥ {}) with p={}: {}\n".format(k, round(p, 4), sum(result)))


def showGeomGraph(n, p):
    k_values = list(range(n+1))
    dist = [geom.pmf(k, p) for k in k_values]

    sns.set_style('whitegrid')
    plt.title('Geometric Distribution for n: {} p: {}'.format(n, round(p, 4))
    plt.xlabel('K-Values: Height')
    plt.ylabel('Y-Values: Probability Mass Function (PMF) Heights')
    sns.barplot(x=k_values, y=dist, color='blue')
    plt.show()


if __name__ == "__main__":
    n = 40
    p = 1/6
    k = 5

    # Table 
    showGeomTable(n, p)

    # Values 
    k = 10
    showGeomPMF(n, k, p, lower=True)

    k = 12
    showGeomPMF(n, k, p, lower=False)

    # Plot Graph
    showGeomGraph(n, p)
