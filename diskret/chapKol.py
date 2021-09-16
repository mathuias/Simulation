import numpy as np 

def solveChapKol(n, vector, P):
    results = list()
    results.append(vector)
    first = vector @ P
    results.append( first )
  
    for i in range(n+1):
        temp =  results[i] @ P 
        results.append(temp)

    print("k\tp(k)") 

    for i in range(n+1):
        print(str(i) + "\t" + str(results[i]))


if __name__ == "__main__":

    vector = np.array([1, 0, 0])

    P = np.array([
                    [0.82, 0.07, 0.11],
                    [0.16, 0.68, 0.16],
                    [0.04, 0.25, 0.71]
    ])

    n = 20

    # solve with Chapman Kolmogorov Method
    solveChapKol(n, vector, P)


