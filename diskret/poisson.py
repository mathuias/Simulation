from scipy.stats import poisson
import matplotlib.pyplot as plt
import seaborn as sns


def showPoissonTable(n, mu):
    k_values = list(range(n+1))
    dist = [poisson.pmf(k, mu) for k in k_values]

    print("\nk\tp(k)")
    for i in range(n+1):
        if dist[i] > 0.0001:
            print(str(k_values[i])+"\t"+str(dist[i]))

def showPoissonPMF(k, mu, lower=True):
    n = 40
    k_values = list(range(n+1))
    dist = [ poisson.pmf(k, mu) for k in k_values if poisson.pmf(k, mu) > 0.0001]
    
    result = list()
    print("\nk\tp(k) :")
    print("___________________")

    if lower is True:
        for i in range(k+1):
            if dist[i] > 0.0001:
                print(str(i)+"\t"+str(dist[i]))
                result.append(dist[i])
        print("For P(X ≤ {}) : {}\n".format(k , sum(result)))

    elif lower is False:
        for j in range(k, len(dist)):
            if dist[j] > 0.0001:
                print(str(j)+"\t"+str(dist[j]))
                result.append(dist[j])
        print("For P(X ≥ {}) : {}\n".format(k, sum(result)))

def showPoissonGraph(n, mu):
    k_values = list(range(n+1))
    dist = [poisson.pmf(k, mu) for k in k_values]

    sns.set_style('whitegrid')
    plt.title('Binomial Distribution for n: {} p: {}'.format(n, p))
    plt.xlabel('K-Values: Height')
    plt.ylabel('Y-Values: Probability Mass Function (PMF) Heights')
    sns.barplot(x=k_values, y=dist, color='blue')
    plt.show()

if __name__ == "__main__":

    n = 20
    mu = 8

    # Table
    showPoissonTable(n, mu)

    # values 
    k = 2
    showPoissonPMF(k, mu, lower=True)

    k = 5
    showPoissonPMF(k, mu, lower=False)





