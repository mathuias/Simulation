import numpy as np
import math

from scipy.stats import norm
import matplotlib.pyplot as plt 
import seaborn as sns

def normPdf(x, mean, sd):
    """Returns the Probability Density Function value of a given Value with its Mean and Standarddeviation"""
    return (1/(2*np.pi*sd**2) ) * np.exp(-0.5*((x-mean)/sd)**2)

def showNormPdf(f, t, s):
    """Range: f is from, t is to, s are the steps"""
    # data 
    x = np.linspace(f, t, s)

    # mean and std
    mean= np.mean(x)
    std = np.std(x)
    print("Data Characteristics: Mean is {}, Std is {}".format(mean, std))
    
    # apply to data
    pdf = normPdf(x, mean, std)

    # visualize by plotting 
    plt.plot(x, pdf, color='red')
    plt.xlabel('Data points')
    plt.ylabel('Probability Density')

def showNormCDF(value, mean, std, lower=True):
    calc = norm(loc=mean, scale=std).cdf(value)
    if lower is True:
        print("P(X <= {}): {}".format(value, calc))
    elif lower is False:
        result = 1 - calc
        print("P(X >= {}): {}".format(value, result))

def showRangeNormCDF(value1, value2, mean, std):
    upper_result = norm(loc=mean, scale=std).cdf(value2)
    lower_result = norm(loc=mean, scale=std).cdf(value1)
    result = upper_result - lower_result
    print("P({} <= X <= {}): {}".format(value1, value2, result))


def printNormTable(n, mu, sigma):
    x_values = list(np.arange(0, n+1, 0.01))
    dist = [norm.pdf(x, loc=mu, scale=sigma) for x in x_values]

    # printing the table 
    print("i\tp(i)") 
    print("-----------")
    for i in range(len(x_values)): 
        print(str(x_values[i]) + "\t" + str(dist[i])) 

def showGraph(n, mu, sigma):
    x_values = list(np.arange(0, n+1, 0.01))
    dist = [norm.pdf(x, loc=mu, scale=sigma) for x in x_values]

    sns.set_style('whitegrid')
    sns.lineplot(x=x_values, y=dist, color='black')
    plt.title('Normal Distribution for mu {} with sigma {}'.format(mu, sigma))
    plt.xlabel('X-Values: Heights')
    plt.ylabel('Y-Values: Probability Density Function Height')
    plt.show()


if __name__ == "__main__":

    # Enter Data Mean (mu) and Std (sigma)
    n = 8
    mu = 206.625
    sigma = 26.6689777

    # table
    printNormTable(n, mu, sigma)

    # values 
    print("\n")
    print("Stdnormalverteilung P(X<5.22): ")
    showNormCDF(349, mu, sigma, lower=True)
    print("\n")
    print("Stdnormalverteilung P(X>5.53): ")
    showNormCDF(390.5, mu, sigma, lower=False)
    print("\n")
    print("Stdnormalveretilung P(4.54≤X≤5.78)")
    showRangeNormCDF(4.54, 5.78, mu, sigma)

    # show graph
    #showGraph(n, mu, sigma)





