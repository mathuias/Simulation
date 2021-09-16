from scipy.stats import binom 
import matplotlib.pyplot as plt 
import seaborn as sns

from bicoeff import binomial

def showBinomTable(n, p):
    k_values = list(range(n+1))
    dist = [binom.pmf(k, n, p) for k in k_values]

    print("\nk\tp(k)")
    print("___________________")
    for i in range(n+1):
        if dist[i] > 0.0001:
            print(str(k_values[i])+"\t"+str(dist[i]))
    
def showBinomGraph(n, p):
    k_values = list(range(n+1))
    dist = [binom.pmf(k, n, p) for k in k_values]

    sns.set_style('whitegrid')
    plt.title('Binomial Distribution for n: {} p: {}'.format(n, p))
    plt.xlabel('K-Values: Height')
    plt.ylabel('Y-Values: Probability Mass Function (PMF) Heights')
    sns.barplot(x=k_values, y=dist, color='blue')
    plt.show()

def binomPmf(n, p, k):
    return binom.pmf(k, n, p)

def showBinomPMF(n, p, k, lower=True):
    k_values = list(range(n+1))
    dist = [binom.pmf(k, n, p) for k in k_values]
    
    result = list()
    print("\nk\tp(k) :")
    print("___________________")

    if lower is True:
        for i in range(k+1):
            if dist[i] > 0.0001:
                print(str(i)+"\t"+str(dist[i]))
                result.append(dist[i])
        print("For P(X <= {}) : {}\n".format(k , sum(result)))

    #! TODO be more precise
    elif lower is False:
        for j in range(k, len(dist)):
            if dist[j] > 0.0001:
                print(str(j)+"\t"+str(dist[j]))
                result.append(dist[j])
        print("For P(X >= {}) : {}\n".format(k, sum(result)))

def basicInfoBinom(n, p):
    E_X = n*p
    Var_X = n*p*(1-p)
    print("E(X): {}, Var(X): {} for n={} and p={}".format(E_X, Var_X, n, p))

if __name__ == "__main__":

    from bicoeff import binomial 

    # input data
    n = 5
    p = 0.74

    # show binomial coeffs 
    print("\n Binomial coefficients for n: {}".format(n))
    for i in range(n+1):
        print(binomial(n, i))

    #show table
    showBinomTable(n, p)

    # with values
    k = 4
    showBinomPMF(n, p, k, lower=True)
    
    k = 3
    showBinomPMF(n, p, k, lower=False)

    # Erwartungswert, Varianz
    basicInfoBinom(n, p)

    #show graph
    showBinomGraph(n, p)


