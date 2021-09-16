import numpy as np 

def solvePageRank(n, vector, P):
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

    #vector = np.array([0, 1, 0, 0])
    vector = np.array([0.25, 0.25, 0.25, 0.25])

    P = np.array([
                    [0,     0,      1,      0],
                    [0.5,   0,      0,      0.5],
                    [0.5,   0.5,    0,      0],
                    [0.5,   0,      0.5,    0]
                ])

    n = 20

    # solve
    solvePageRank(n, vector, P)