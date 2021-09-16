import math
import numpy as np

from scipy.stats import expon

import matplotlib.pyplot as plt
import seaborn as sns


def showExponCDF(value, mu, lower=True):
    lamb = 1/mu
    calc = expon(loc=lamb).cdf(value)
    if lower is True:
        print("P(X <= {}): {}\n".format(value, calc))
    elif lower is False:
        result = 1 - calc
        print("P(X >= {}): {}\n".format(value, result))

def showRangeExponCDF(value1, value2, mu):
    lamb = 1/mu
    upper_result = expon(loc=lamb).cdf(value2)
    lower_result = expon(loc=lamb).cdf(value1)
    result = upper_result - lower_result
    print("P({} <= X <= {}): {}\n".format(value1, value2, result))

def printExponTable(n, mu):
    lamb = 1 / mu
    x_values = list(np.arange(0, n+1, 0.01))
    dist = [expon.pdf(x, loc=lamb) for x in x_values]

    # printing the table 
    print("i\tp(i)") 
    print("-----------")
    for i in range(len(x_values)): 
        print(str(x_values[i]) + "\t" + str(dist[i])) 

    print("\n")
    plt.plot(x_values, dist)
    plt.show()

def showExponGraph(n, mu):
    k_values = list(range(n+1))
    dist = [ expon.pdf(k, mu) for k in k_values]

    sns.set_style('whitegrid')
    plt.title('Exponential Distribution for n: {} µ: {}'.format(n, mu))
    plt.xlabel('K-Values: Height')
    plt.ylabel('Y-Values: Probability Density Function (PDF) Heights')
    sns.barplot(x=k_values, y=dist, color='blue')
    plt.show()

def showExpoValue(mu, k, lower=True):
    if lower is True:
        result = 1 - math.exp(((-1/mu)*k))
        print("P(X ≤ k): {}".format(result))
    elif lower is False:
        result =  math.exp(((-1/mu)*k))
        print("P(X ≥ k): {}".format(result))


if __name__ == "__main__":

    # Enter data
    n = 120
    mu = 27


    print("Alle Ps")
    showExpoValue(mu, 20, lower=True)
    showExpoValue(mu, 40, lower=True)
    showExpoValue(mu, 60, lower=True)
    showExpoValue(mu, 60, lower=False)
    
    # graph
    showExponGraph(n, mu)



