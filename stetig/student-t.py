import math
import numpy as np

from scipy.stats import t
import matplotlib.pyplot as plt
import seaborn as sns


def showTstudentCDF(value, df_value, lower=True):
    calc = t(df=df_value).cdf(value)
    if lower is True:
        print("P(X <= {}): {}".format(value, calc))
    elif lower is False:
        result = 1 - calc
        print("P(X >= {}): {}".format(value, result))


def showRangeTstudentCDF(value1, value2, df_value):
    upper_result = t(df=df_value).cdf(value2)
    lower_result = t(df=df_value).cdf(value1)
    result = upper_result - lower_result
    print("P({} <= X <= {}): {}".format(value1, value2, result))


def printTstudentTable(n, df_value):
    x_values = list(np.arange(0, n+1, 0.01))
    dist = [t.pdf(x, df=df_value) for x in x_values]

    # printing the table 
    print("i\tp(i)") 
    print("-----------")
    for i in range(len(x_values)): 
        print(str(x_values[i]) + "\t" + str(dist[i])) 

def showTstudentGraph(n, df_value):
    x_values = list(np.arange(0, n+1, 0.01))
    dist = [t.pdf(x, df=df_value) for x in x_values]
    sns.set_style('whitegrid')
    sns.lineplot(x=x_values, y=dist, color='black')
    plt.title('Student-T Distribution for {}'.format(df_value))
    plt.xlabel('X-Values: Heights')
    plt.ylabel('Y-Values: Probability Density Function Height')
    plt.show()


if __name__ == "__main__":

    # Enter Data Mean (mu) and Std (sigma)
    n = 10
    df_value=2.76

    printTstudentTable(n, df_value)

    #new
    print("\n")
    showTstudentCDF(5.09, df_value, lower=True)
    showTstudentCDF(5.4, df_value, lower=False)
    showRangeTstudentCDF(4.54, 5.78, df_value)