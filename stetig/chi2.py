from scipy.stats import chi2
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

import numpy as np

n = 20
df = 55
mean, var, = chi2.stats(df, moments='mv')

k_values = list(range(n+1))

# chi2 probabilities
dist = [chi2.pdf(k, df) for k in k_values]

x = np.linspace(chi2.ppf(0.01, df),
                chi2.ppf(0.99, df), 100)

ax.plot(x, chi2.pdf(x, df),
       'r-', lw=5, alpha=0.6, label='chi2 pdf')

# printing the table 
print("k\tp(k)") 
for i in range(n + 1): 
    print(str(k_values[i]) + "\t" + str(dist[i])) 

# printing mean and variance 
print("mean = "+str(mean)) 
print("variance = "+str(var))

plt.bar(k_values, dist) 
plt.show()

# single values
print(chi2.pdf(0, df))